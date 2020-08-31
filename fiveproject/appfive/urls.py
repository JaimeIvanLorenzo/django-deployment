from django.urls import path
from .views import index,register,user_login,user_logout

app_name='app_five'
urlpatterns = [

    path('',index,name='home_page'),
    path('form/',register,name='form_page'),
    path('user_login/',user_login,name='user_login'),
]