from django.contrib import admin
from django.urls import path, include
from superadmin import views

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('login/', views.loginPage.as_view(), name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('changepassword/', views.changePassword.as_view(), name="changepassword"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="dashboard/reset_password.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="dashboard/reset_password_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="dashboard/reset_password_confirm.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="dashboard/reset_password_complete.html"),
         name="password_reset_complete"),
         

    path('dashboard/', views.Dashboard, name='dashboard'),
    # ****************** Category ***********************

    path('dashboard/category/', views.Category, name='category'),
    path('dashboard/category/add/', views.CategoryAdd, name='category-add'),
    path('dashboard/category/edit/<str:slug>',
         views.CategoryEdit, name='category-edit'),
    path('dashboard/category/update/<str:slug>',
         views.CategoryUpdate, name='category-update'),
    path('dashboard/category/delete/<str:slug>',
         views.CategoryDelete, name='category-delete'),

    # *************************************************

    # ****************** Project ***********************

    path('dashboard/project/', views.Project, name='project'),
    path('dashboard/project/add/', views.ProjectAdd, name='project-add'),
    path('dashboard/project/edit/<str:slug>/',
         views.ProjectEdit, name='project-edit'),
    path('dashboard/project/update/<str:slug>/',
         views.ProjectUpdate, name='project-update'),
    path('dashboard/project/delete/<str:slug>/',
         views.ProjectDelete, name='project-delete'),

    # *************************************************

    # ****************** Progress ***********************

    path('dashboard/progress/', views.Progress, name='progress'),
    path('dashboard/progress/add/', views.ProgressAdd, name='progress-add'),
    path('dashboard/progress/edit/<str:slug>/',
         views.ProgressEdit, name='progress-edit'),
    path('dashboard/progress/update/<str:slug>/',
         views.ProgressUpdate, name='progress-update'),
    path('dashboard/progress/delete/<str:slug>/',
         views.ProgressDelete, name='progress-delete'),

    # *************************************************

    # ****************** MasterPlan ***********************

    path('dashboard/masterplan/', views.MasterPlan, name='masterplan'),
    path('dashboard/masterplan/add/', views.MasterPlanAdd, name='masterplan-add'),
    path('dashboard/masterplan/edit/<str:slug>/',
         views.MasterPlanEdit, name='masterplan-edit'),
    path('dashboard/masterplan/update/<str:slug>/',
         views.MasterPlanUpdate, name='masterplan-update'),
    path('dashboard/masterplan/delete/<str:slug>/',
         views.MasterPlanDelete, name='masterplan-delete'),

    # *************************************************


    # ****************** Blog ***********************

    path('dashboard/amenitiesview/', views.BlogView, name='blogview'),
    path('dashboard/amenities/add/', views.BlogAdd, name='blog-add'),
    path('dashboard/amenities/edit/<str:slug>/', views.BlogEdit, name='blog-edit'),
    path('dashboard/amenities/update/<str:slug>/',
         views.BlogUpdate, name='blog-update'),
    path('dashboard/amenities/delete/<str:slug>/',
         views.BlogDelete, name='blog-delete'),

    # *************************************************


    # ****************** Contact Us ***********************

    path('contactinfo/', views.ContactInfo, name='contactinfo'),
    path('contact/add/', views.ContactAdd, name='contact-add'),
    path('contact/edit/<str:slug>/', views.ContactEdit, name='contact-edit'),
    path('contact/update/<str:slug>/',
         views.ContactUpdate, name='contact-update'),
    path('contact/delete/<str:slug>/',
         views.ContactDelete, name='contact-delete'),

    # *************************************************

    # ****************** Slider ***********************

    path('slider/', views.Slider, name='slider'),
    path('slider/add/', views.SliderAdd, name='slider-add'),
    path('slider/edit/<str:slug>/', views.SliderEdit, name='slider-edit'),
    path('slider/update/<str:slug>/', views.SliderUpdate, name='slider-update'),
    path('slider/delete/<str:slug>/', views.SliderDelete, name='slider-delete'),

    # *************************************************

    # ****************** CustomerPreview ***********************

    path('customerreview/', views.CustomerReview, name='customerreview'),
    path('customerreview/add/', views.CustomerReviewAdd, name='customerreview-add'),
    path('customerreview/edit/<str:slug>/',
         views.CustomerReviewEdit, name='customerreview-edit'),
    path('customerreview/update/<str:slug>/',
         views.CustomerReviewUpdate, name='customerreview-update'),
    path('customerreview/delete/<str:slug>/',
         views.CustomerReviewDelete, name='customerreview-delete'),

    # *************************************************

    # ****************** CallBack ***********************

    path('booking/', views.Booking, name='booking'),
    path('booking/add/', views.BookingAdd, name='booking-add'),
    path('booking/edit/<str:slug>/', views.BookingEdit, name='booking-edit'),
    path('booking/update/<str:slug>/',
         views.BookingUpdate, name='booking-update'),
    path('booking/delete/<str:slug>/',
         views.BookingDelete, name='booking-delete'),

    # *************************************************



    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('privacypolicy/', views.PrivacyPolicy, name='privacypolicy'),
    path('termscondition/', views.TermsCondition, name='termscondition'),
    path('amenities/', views.Blog, name='blog'),
    path('amenities/<str:slug>', views.BlogSingle, name='blog'),
    path('progress/', views.ProgressPage, name='prog'),
    path('progress/<str:slug>', views.ProgressSingle, name='prog'),
    path('project/<str:slug>', views.ProjectSingle, name='project'),
    path('<str:slug>', views.CategoryDetail, name='category-detail'),
    path('projectdesc/<str:slug>', views.CategorySingle, name='category-single'),
    path('contact/', views.Contact, name='contact'),
    path('review/', views.Review, name='review'),

]
