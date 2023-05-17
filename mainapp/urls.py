from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mainapp import views
from django.contrib.auth.views import LogoutView

app_name = "mainapp"
urlpatterns = [
    path('', views.render_index, name='index'),
    path('announcement/<int:id>/', views.render_announcement, name='announcement'),
    path('profile/<int:id>/', views.render_profile, name='profile'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('reg/', views.RegistrationView.as_view(), name='reg'),
    path('add/', views.AnnouncementCreateView.as_view(), name='add'),
    path('<slug:pk>/edit/', views.AnnouncementUpdateView.as_view(), name='update'),
    path('<slug:pk>/remove/', views.AnnouncementDeleteView.as_view(), name='delete'),
    path('<slug:pk>/edit_info/', views.UserUpdateView.as_view(), name='info_update'),
    path('<slug:pk>/remove_info/', views.UserDeleteView.as_view(), name='info_delete')
]
