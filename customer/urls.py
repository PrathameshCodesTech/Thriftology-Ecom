from django.urls import path
from . import views  # Import your views module
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from customer.forms import LoginForm, MyPasswordChangeForm, PasswordResetForm, MySetPasswordForm

urlpatterns = [
    # URL for the registration page
    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view
         (template_name='login.html', authentication_form=LoginForm), name='login'),
    # Django's built-in login view

    path('logout/', auth_views.LogoutView.as_view(next_page='Home-Page'),
         name='logout'),  # Django's built-in logout view

    path('password-change/',
         auth_views.PasswordChangeView.as_view(
             template_name='passwordchange.html',
             form_class=MyPasswordChangeForm,
             # Redirect to profile page after successful change
             success_url=reverse_lazy('login')
         ),
         name='password_change'
         ),


    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=PasswordResetForm), name="password_reset"),


    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),



    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name="password_reset_confirm"),


    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name="password_reset_complete"),

]
