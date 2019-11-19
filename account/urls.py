from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
app_name = 'tutorial'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('register/',views.register,name='register'),
    path('profile/',views.view_profile,name='view_profile'),
    path('profile/<int:num>/',views.view_profile,name='view_profile_with_id'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('changepassword/',views.change_password,name='change_password'),
    path('resetpassword/',PasswordResetView.as_view(template_name='account/reset_password.html'), name='reset_password'),
    path('resetpassword/done/',PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('resetpassword/complete/',PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    re_path(r'^resetpassword/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),


]
