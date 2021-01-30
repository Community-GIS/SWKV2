from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.HomePage, name = 'homepage'),
    path('aboutus/', views.AboutUs, name = 'aboutus'),
    path('formlayout/',views.formLayout,name='formlayout'),
    path('trackform/', views.TracksheetPage, name = "trackform"),
    path('dutyentryform/', views.DutyEntryPage, name = "dutyentryform"),
    path('login/', views.user_login, name='login'),
    path("logout", views.logout_request, name="logout"),
    path('show/',views.show, name='show'),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy), 
    path('feedback/',views.Feedback, name = 'feedback'),
    path('faq/',views.FAQ, name = 'faq'),
   
]

