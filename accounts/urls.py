from django.urls import path

from django.contrib.auth import views as auth_views

from .views import (
    home,
    products,
    customer, 
    createOrder, 
    updateOrder,
    deleteOrder,
    registerPage,
    loginPage,
    logoutUser,
    userPage,
    accountSettings,
)


urlpatterns = [
    path('register/', registerPage, name='register' ),
    path('login/', loginPage, name='login' ),
    path('logout/', logoutUser, name='logout' ),
    
    path('', home, name='home'),
    path('user/', userPage, name='user-page'),
    
    path('accounts/', accountSettings, name='account'),
    
    path('products/', products, name='products'),
    path('customer/<int:pk>/', customer, name='customer'),
    
    path('create_order/<int:pk>/', createOrder, name='create_order'),
    path('update_order/<int:pk>/', updateOrder, name='update_order'),
    path('delete_order/<int:pk>/', deleteOrder, name='delete_order'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    
    
]


'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''
