from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('back', views.back),
    path('log_in', views.log_in_page_render),
    path('home_page', views.home_page_render),
    path('register_page', views.register_page_render),
    path('user_profile_page/<int:user_id>', views.user_profile_page),
    path('top_ten_page', views.top_ten_page),
    path('add_entry_page', views.add_entry_page),
    path('dieties_by_religion', views.deities_by_religion_page),
    path('dieties_by_location', views.deities_by_location_page),
    path('diety_info_page/<int:diety_id>', views.deity_info_page),
    path('register', views.register),
    path('logout', views.logout),
    path('login', views.login),
]