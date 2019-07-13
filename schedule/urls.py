from django.contrib import admin
from django.urls import path, include 
from django.urls import path
from schedule import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login', views.login),
    path('logout/', views.logout, name='logout-page'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index-page'), 
    path('Dashboard/', views.login, name='dashboard-home'),
    path('dashboard/',views.dashboard, name='dashboard'),
    
    path('password_reset_complete/', views.p_complete, name='password_reset_complete'),
    path('password_reset_confirm/', views.p_confirm, name='password_reset_confirm'),
    path('password_reset_done/', views.reset, name='password_reset_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'schedules/forget.html'), name='password_reset'),

    path('Planner-form/',views.Plannerform,name="Planner-form"),
    path('Planner-form/<c_code_selected>', views.Plannerform, name="Planner-form"),
    path('generateplanner/', views.generateplanner, name="generateplanner"),
    path('session_display/', views.Plannerform, name="session_display"),
    
    path('view_after_search/', views.search,name="view_after_search"),
    
    path('addstudent/', views.addstudent, name='addstudent'),
    path('vstudent/', views.vstudent, name='vstudent'),
    path('estudent/',views.estudent,name='estudent'), 
    path('studentleave/',views.sviewleave, name='studentleave'),
    path('accepts/',views.accepts, name='accepts'),
    path('rejects/',views.rejects, name='rejects'),

    path('addfaculty/', views.addfaculty, name='addfaculty'),
    path('vfaculty/', views.vfaculty, name='vfaculty'),
    path('efaculty/',views.efaculty,name='efaculty'),
    path('facultyleave/', views.fviewleave, name='facultyleave'),
    path('acceptf/', views.acceptf, name='acceptf'),
     path('rejectf/', views.rejectf, name='rejectf'),

    path('addcourse/', views.addcourse, name='addcourse'),
    path('vcourse/', views.vcourse, name='vcourse'),
    path('ecourse/',views.ecourse,name='ecourse'),

    path('addmodule/',views.addmodule,name='addmodule'),
    path('vmodule',views.vmodule,name='vmodule'),
    path('emodule/',views.emodule,name='emodule'),

    path('assigncm/',views.assigncm, name='assigncm'),
    path('vassign/', views.vassign, name='vassign'),
    path('eassign/',views.eassign, name='eassign'),

    path('add', views.add, name="adds"),
    path('addc', views.addc, name="addcode"),
    path('addf', views.addf, name="addsf"),
    path('addm', views.addm,name="addm"),
    path('assignmodule', views.assignmodule, name="assignmodule"),
    path('acceptsleave',views.acceptsleave, name='acceptsleave'),
    path('rejectsleave',views.rejectsleave, name='rejectsleave'),
    path('acceptfleave',views.acceptfleave, name='acceptfleave'),
    path('rejectfleave',views.rejectfleave, name='rejectfleave'),

    path('viewstudent', views.viewstudent,name="viewstudent"),
    path('viewfaculty', views.viewfaculty,name="viewfaculty"),
    path('viewcourse', views.viewcourse,name="viewcourse"),
    path('viewmodule',views.viewmodule,name="viewmodule"),
    path('viewassign',views.viewassign, name="viewassign"),
    path('viewleave/', views.viewleave, name='viewleave'),
   
    path('editstudent',views.editstudent,name="editstudent"),
    path('editfaculty',views.editfaculty, name="editfaculty"),
    path('editcourse',views.editcourse, name="editcourse"),
    path('editassign',views.editassign, name="editassign"),
    path('editmodule',views.editmodule,name="editmodule"),

    path('deletestudent', views.deletestudent,name="deletestudent"),
    path('deletefaculty', views.deletefaculty,name="deletefaculty"),
    path('deletecourse', views.deletecourse,name="deletecourse"),
    path('deleteassign', views.deleteassign, name="deleteassign"),
    path('deletemodule', views.deletemodule,name="deletemodule"),

    
    path('leave/', views.leave, name='leave'),

    path('calender/', views.calender, name='calender'),


]