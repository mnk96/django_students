from django.contrib.auth.views import LogoutView
from django.urls import path, include

from menu_university.views import (index, get_user,
                                   get_about, get_salary,
                                   get_scholarship)

app_name = 'menu'
urlpatterns = [
    path('', index, name='main_page'),
    path('auth/login/', get_user, name='login'),
    path('auth/logout/', LogoutView.as_view(
        template_name='registration/logged_out.html'), name='logout'),
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', get_about, name='about'),
    path('scholar/', get_scholarship, name='scholar'),
    path('salary/', get_salary, name='salary')
]
