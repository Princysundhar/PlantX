"""Krishibhavan URL Configuration

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

from my_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.log),
    path('log_post',views.log_post),
    path('admin_home',views.admin_home),
    path('logout',views.logout),
    path('add_agriculture_office',views.add_agriculture_office),
    path('add_agriculture_office_post',views.add_agriculture_office_post),
    path('view_agriculture_office',views.view_agriculture_office),
    path('update_agriculture_office/<id>',views.update_agriculture_office),
    path('update_agriculture_office_post/<id>',views.update_agriculture_office_post),
    path('delete_agriculture_office/<id>',views.delete_agriculture_office),
    path('send_notification_office',views.send_notification_office),
    path('send_notification_office_post',views.send_notification_office_post),
    path('view_notification_office',views.view_notification_office),
    path('delete_notification_office/<id>',views.delete_notification_office),
    path('view_complaint',views.view_complaint),
    path('send_reply/<id>',views.send_reply),
    path('send_reply_post/<id>',views.send_reply_post),
    path('view_feedback',views.view_feedback),
    path('forgot_password',views.forgot_password),
    path('forgot_password_post',views.forgot_password_post),

#..........................................................................................
    path('officer_home',views.officer_home),
    path('view_notification',views.view_notification),
    path('add_subsidy',views.add_subsidy),
    path('add_subsidy_post',views.add_subsidy_post),
    path('view_subsidy',views.view_subsidy),
    path('update_subsidy/<id>',views.update_subsidy),
    path('update_subsidy_post/<id>',views.update_subsidy_post),
    path('delete_subsidy/<id>',views.delete_subsidy),
    path('add_stock',views.add_stock),
    path('add_stock_post',views.add_stock_post),
    path('view_stock',views.view_stock),
    path('update_stock/<id>',views.update_stock),
    path('update_stock_post/<id>',views.update_stock_post),
    path('delete_stock/<id>',views.delete_stock),
    path('view_stock_request',views.view_stock_request),
    path('view_order_sub/<id>',views.view_order_sub),
    path('add_fertilizer',views.add_fertilizer),
    path('add_fertilizer_post',views.add_fertilizer_post),
    path('view_fertilizer',views.view_fertilizer),
    path('update_fertilizer/<id>',views.update_fertilizer),
    path('update_fertilizer_post/<id>',views.update_fertilizer_post),
    path('delete_fertilizer/<id>',views.delete_fertilizer),
    path('add_success_story',views.add_success_story),
    path('add_success_story_post',views.add_success_story_post),
    path('view_success_story',views.view_success_story),
    path('delete_success_story/<id>',views.delete_success_story),
    path('send_notification',views.send_notification),
    path('send_notification_post',views.send_notification_post),
    path('chatt/<u>',views.chatt),
    path('chatsnd/<u>',views.chatsnd),
    path('chatrply',views.chatrply),

#............................................................................................USER(ANDROID)

    path('and_login',views.and_login),
    path('and_user_registration',views.and_user_registration),
    path('and_view_profile',views.and_view_profile),
    path('and_view_agriculture_office',views.and_view_agriculture_office),
    path('and_view_notification',views.and_view_notification),
    path('and_view_fertilizer',views.and_view_fertilizer),
    path('and_view_reply',views.and_view_reply),
    path('and_send_complaint',views.and_send_complaint),
    path('and_view_success_story',views.and_view_success_story),
    path('and_send_Feedback',views.and_send_Feedback),
    path('android_add_chat',views.android_add_chat),
    path('android_view_chat',views.android_view_chat),
    path('and_view_stock',views.and_view_stock),
    path('and_add_quantity',views.and_add_quantity),
    path('and_view_cart',views.and_view_cart),
    path('and_cart_cancel',views.and_cart_cancel),
    path('and_offline_payment',views.and_offline_payment),
    path('android_online_payment',views.android_online_payment),
    path('and_view_orders',views.and_view_orders),

]
