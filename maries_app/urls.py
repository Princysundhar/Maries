"""maries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from maries_app import views

urlpatterns = [
    path('', views.Log),
    path('Login_post', views.Login_post),
    path('Send_reply/<id>',views.Send_reply),
    path('send_reply_post/<id>',views.send_reply_post),
    path('Service_provider', views.Service_provider),
    path('approve_service_provider/<id>', views.approve_service_provider),
    path('reject_service_provider/<id>',views.reject_service_provider),
    path('Service_subcat_manag', views.Service_subcat_manag),
    path('view_service_subcat_manag',views.view_service_subcat_manag),
    path('add_service_type_post',views.add_service_type),
    path('Service_type_management', views.Service_type_management),
    path('view_Service_type_management',views.view_Service_type_management),
    path('add_service_type', views.add_service_type),
    path('add_service_post', views.add_service_post),
    path('add_service_subcat_post',views.add_service_subcat_post),
    path('View_approved_service_provider', views.View_approved_service_provider),
    path('View_complaint', views.View_complaint),
    path('delete_service_type/<id>',views.delete_service_type),
    path('delete_subcategory/<id>',views.delete_subcategory),
    path('update_service_type',views.update_service_type),
    path('View_rating', views.View_rating),
    path('home',views.home),
###################################################################################


    path('sevice_provider_register',views.sevice_provider_register),
    path('service_provider_register_post',views.service_provider_register_post),
    path('view_profile_post',views.view_profile_post),
    path('view_profile',views.view_profile),
    path('edit_profile/<id>',views.edit_profile),
    path('view_service_type_and_subcategories',views.view_service_type_and_subcategories),
    path('edit_my_service/<id>',views.edit_my_service),
    path('edit_my_service_post/<id>',views.edit_my_service_post),
    path('add_service_management/<id>',views.add_service_management),
    path('add_service_management_post/<id>',views.add_service_management_post),
    path('view_service_management/<id>',views.view_service_management),
    path('my_service',views.my_service),
    path('update_view_service_management/<id>',views.update_view_service_management),
    path('delete_view_service_management/<id>',views.delete_view_service_management),
    path('view_rq_from_user_and_approve',views.view_rq_from_user_and_approve),
    path('req_from_user_reject/<id>',views.req_from_user_reject),
    path('req_from_user_approve/<id>',views.req_from_user_approve),
    path('view_approved_rq',views.view_approved_rq),
    path('view_rating',views.view_rating),
    path('service_provider_view_subcat/<id>',views.service_provider_view_subcat),
    path('service_provider_home',views.service_provider_home),
    path('About',views.About),

###################################################################################################

    path('and_login',views.and_login),
    path('and_register',views.and_register),
    path('and_view_profile',views.and_view_profile),
    path('and_view_service_provider',views.and_view_service_provider),
    path('and_view_service',views.and_view_service),
    path('and_send_request',views.and_send_request),
    path('and_view_service_type',views.and_view_service_type),
    path('and_feed_back',views.and_feed_back),
    path('and_view_request_status',views.and_view_request_status)
]