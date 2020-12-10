from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Main
    path('', views.home, name="home"),
    path('user/', views.userPage, name="user"),
    path('account/', views.accountSettings, name="account"),
    path('products/', views.products, name="products"),
    path('customer/<str:_id>', views.customer, name="customer"),

    # Api Crud System
    path('create_order/<str:_id>', views.createOrder, name="create_order"),
    path('update_order/<str:_id>', views.updateOrder, name="update_order"),
    path('delete_order/<str:_id>', views.deleteOrder, name="delete_order"),

    # Login System
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    #Reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset_password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete")
]