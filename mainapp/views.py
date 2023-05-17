from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, DeleteView, CreateView, View
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from .forms import *
from .models import *


def render_index(request):
    сlient = User.objects.all()
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
    seller = User.objects.get(id=current_announcement.user.id)
    return render(request, 'inform.html', {'announcement': current_announcement,
                                           'seller': seller})


def render_profile(request, id):
    seller = User.objects.get(id=id)
    announcement = Announcement.objects.all()
    announcement_user = Announcement.objects.filter(user=id)
    category = Category.objects.all()
    cities = Cities.objects.all()
    region = Region.objects.all()
    moderation = ModerationAd.objects.all()
    return render(request, "profile.html", {'seller': seller, 'announcement': announcement,
                                            'category': category,
                                            'cities': cities,
                                            'region': region,
                                            'moderation': moderation,
                                            'announcement_user': announcement_user})


class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'add.html'
    form_class = UserForm
    permission_required = ''
    raise_exception = True      # для вывода ошибки

    def get_success_url(self):
        # для возвращения на главную страницу
        return reverse_lazy('mainapp:index')


class UserUpdateView(UpdateView):
    template_name = 'add.html'
    model = User
    form_class = UserForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


class UserDeleteView(DeleteView):
    template_name = 'add.html'
    model = User
    form_class = UserForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


class AnnouncementCreateView(CreateView):
    template_name = 'add.html'
    model = Announcement
    form_class = AnnouncementForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


class AnnouncementUpdateView(UpdateView):
    template_name = 'add.html'
    model = Announcement
    form_class = AnnouncementForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


class AnnouncementDeleteView(DeleteView):
    template_name = 'add.html'
    model = Announcement
    form_class = AnnouncementForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


class CategoryCreateView(CreateView):
    template_name = 'add.html'
    form_class = CategoryForm
    permission_required = ''
    raise_exception = True      # для вывода ошибки

    def get_success_url(self):
        # для возвращения на главную страницу
        return reverse_lazy('mainapp:index')


class CategoryUpdateView(UpdateView):
    template_name = 'add.html'
    model = Category
    form_class = CategoryForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


class CategoryDeleteView(DeleteView):
    template_name = 'add.html'
    model = Category
    form_class = CategoryForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


class CitiesCreateView(CreateView):
    template_name = 'add.html'
    form_class = CitiesForm
    permission_required = ''
    raise_exception = True      # для вывода ошибки

    def get_success_url(self):
        # для возвращения на главную страницу
        return reverse_lazy('mainapp:index')


class CitiesUpdateView(UpdateView):
    template_name = 'add.html'
    model = Cities
    form_class = CitiesForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


class CitiesDeleteView(DeleteView):
    template_name = 'add.html'
    model = Cities
    form_class = CitiesForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


class RegionCreateView(CreateView):
    template_name = 'add.html'
    form_class = RegionForm
    permission_required = ''
    raise_exception = True      # для вывода ошибки

    def get_success_url(self):
        # для возвращения на главную страницу
        return reverse_lazy('mainapp:index')


class RegionUpdateView(UpdateView):
    template_name = 'add.html'
    model = Region
    form_class = RegionForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


class RegionDeleteView(DeleteView):
    template_name = 'add.html'
    model = Region
    form_class = RegionForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


class ModerationAdCreateView(CreateView):
    template_name = 'add.html'
    form_class = ModerationAdForm
    permission_required = ''
    raise_exception = True      # для вывода ошибки

    def get_success_url(self):
        # для возвращения на главную страницу
        return reverse_lazy('mainapp:index')


class ModerationAdUpdateView(UpdateView):
    template_name = 'add.html'
    model = ModerationAd
    form_class = ModerationAdForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


class ModerationAdDeleteView(DeleteView):
    template_name = 'add.html'
    model = ModerationAd
    form_class = ModerationAdForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('mainapp:index')


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
            gr = Group.objects.get(name="Пользователь")
            new_user.username = form.cleaned_data['username']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.patronymic = form.cleaned_data['patronymic']
            new_user.email = form.cleaned_data['email']
            new_user.phone = form.cleaned_data['phone']
            new_user.convenient_time = form.cleaned_data['convenient_time']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            gr.user_set.add(new_user)
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')                        # если все правильно возвращаем на главную страницу
        return render(request, 'registration.html', {'form':form})  # иначе на ту же самую
