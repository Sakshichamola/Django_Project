from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  
    path('signup/', views.signup_view, name='signup'),  
    path('index/', views.index_view, name='index'),  
    path('logout/', views.logout_view, name='logout'),  
    path('update-account/', views.update_account_view, name='update_account'),
    path('delete-account/', views.delete_account_view, name='delete_account'),
    path('submit-blog/', views.blog_form, name='blog_form'),  # Page to create a blog
    path('view-blogs/', views.blog_list, name='blog_list'),  # Page to view all blog
]
