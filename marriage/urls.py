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
from django.urls import path,include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.log),
    path('login_post', views.login_post),
    path('admin_home', views.admin_home),
    path('logout', views.logout),
    path('view_service_provider', views.view_service_provider),
    path('view_approved_service_provider/<id>', views.view_approved_service_provider),
    path('approved_service_provider', views.approved_service_provider),
    path('view_reject_service_provider/<id>', views.view_reject_service_provider),
    path('view_complaint', views.view_complaint),
    path('send_reply/<id>', views.send_reply),
    path('send_reply_post/<id>', views.send_reply_post),
    path('view_rating/<id>', views.view_rating),
    path('service_type_add', views.service_type_add),
    path('service_type_add_post', views.service_type_add_post),
    path('service_type_view', views.service_type_view),
    path('delete_service_type/<id>', views.delete_service_type),
    path('service_subcategory_add', views.service_subcategory_add),
    path('service_subcategory_add_post', views.service_subcategory_add_post),
    path('service_subcategory_view', views.service_subcategory_view),
    path('service_subcategory_update/<id>', views.service_subcategory_update),
    path('service_subcategory_update_post/<id>', views.service_subcategory_update_post),
    path('delete_service_subcategory/<id>', views.delete_service_subcategory),

#.......................................................................................................

    path('serviceprovider_home',views.serviceprovider_home),
    path('register',views.register),
    path('register_post',views.register_post),
    path('view_profile',views.view_profile),
    path('edit_profile/<id>',views.edit_profile),
    path('edit_profile_post/<id>',views.edit_profile_post),
    path('view_service_type_subcategory/<id>',views.view_service_type_subcategory),
    path('add_service',views.add_service),
    path('add_service_post',views.add_service_post),
    path('view_service',views.view_service),
    path('update_service/<id>/<sid>',views.update_service),
    path('update_service_post/<id>/<sid>',views.update_service_post),
    path('delete_service/<id>',views.delete_service),
    path('view_request_from_user',views.view_request_from_user),
    path('view_service_for_request/<id>',views.view_service_for_request),
    path('view_approved_request/<rid>',views.view_approved_request),
    path('view_request_approve',views.view_request_approve),
    path('view_reject_request/<id>',views.view_reject_request),
    path('view_payment',views.view_payment),
    path('view_ratings',views.view_ratings),

# ..............................................................................for
    path('android_login',views.android_login),
    path('android_user_registration',views.android_user_registration),
    path('android_view_profile',views.android_view_profile),
    path('android_view_nearby_serviceprovider',views.android_view_nearby_serviceprovider),
    path('android_view_rating',views.android_view_rating),
    path('android_view_servicetype_subcategory',views.android_view_servicetype_subcategory),
    path('android_view_service',views.android_view_service),
    path('android_user_request',views.android_user_request),
    path('android_view_service_cart',views.android_view_service_cart),
    path('android_cart_placeorder',views.android_cart_placeorder),
    path('android_cancel_order',views.android_cancel_order),
    path('android_view_request_status',views.android_view_request_status),
    path('android_make_payment',views.android_make_payment),            # payment
    path('android_online_payment',views.android_online_payment),            # payment
    path('android_view_serviceprovider_history',views.android_view_serviceprovider_history),
    path('android_send_rate',views.android_send_rate),
    path('android_add_chat',views.android_add_chat),
    path('android_view_chat',views.android_view_chat),
    path('android_view_request_sub_items',views.android_view_request_sub_items),
    path('and_view_category',views.and_view_category),
    path('chatt/<u>',views.chatt),
    path('chatsnd/<u>',views.chatsnd),
    path('chatrply',views.chatrply),
    path('android_send_complaint',views.android_send_complaint),
    path('android_view_complaint',views.android_view_complaint),




]
