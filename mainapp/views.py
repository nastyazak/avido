from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, DeleteView, CreateView, View
from django.urls import reverse_lazy
from .forms import *
from .models import *


def render_index(request):
    сlient = Client.objects.all()
    announcement = Announcement.objects.all()
    category = Category.objects.all()
    cities = Cities.objects.all()
    region = Region.objects.all()
    moderation = ModerationAd.objects.all()
    return render(request, 'index.html',
                  {'сlient': сlient,
                   'announcement': announcement,
                   'category': category,
                   'cities': cities,
                   'region': region,
                   'moderation': moderation})


def render_announcement(request, id):
    current_announcement = Announcement.objects.get(id=id)
    seller = Client.objects.get(id=current_announcement.user.id)
    return render(request, 'inform.html', {'announcement': current_announcement,
                                           'seller': seller})

"""
def render_profile(request, id):
    seller = Client.objects.get(id=id)
    return render(request, "profile.html", {'seller': seller})
"""

"""
class PersonCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'add.html'
    form_class = ClientForm
    permission_required = ''
    raise_exception = True      # для вывода ошибки

    def get_success_url(self):
        # для возвращения на главную страницу
        return reverse_lazy('mainapp:index')


class PersonUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'add.html'
    model = Client
    form_class = ClientForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


class PersonDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'add.html'
    model = Client
    form_class = ClientForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')
"""

class LoginView(View):
    def get(self, request, *args, **kwargs):
        # получение данных
        form = LoginForm(request.POST or None)
        return render(request, 'login.html', {'form':form})

    def post(self, request, *args, **kwargs):
        # отправка данных в БД
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')                # если все правильно возвращаем на главную страницу
        return render(request, 'login.html', {'form':form})     # иначе на ту же самую


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        return render(request, 'registration.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.name = form.cleaned_data['name']
            new_user.surname = form.cleaned_data['surname']
            """
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
                        """
            new_user.save()

            #user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            #login(request, user)
            return HttpResponseRedirect('/')                        # если все правильно возвращаем на главную страницу
        return render(request, 'registration.html', {'form':form})  # иначе на ту же самую
