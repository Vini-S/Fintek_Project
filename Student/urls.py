from django.contrib import admin
from django.urls import path, include 
from Student import views


urlpatterns = [

	    path('studentview', views.studentview,name="studentview"),
	    path('facultyview', views.facultyview,name="facultyview"),
	    path('courseview', views.courseview,name="courseview"),
	    path('moduleview', views.moduleview,name="moduleview"),
	   	path('s_view_after_search/', views.studentsearch,name="s_view_after_search"),
	   	path('applyleave', views.sleave, name="sleave"),
	   	path('sfviewleave', views.Sfviewleave, name="sfviewleave"),
	   	path('sviewleave', views.sviewleave, name="sviewleave"),
	   	path('scalender', views.scalender, name="scalender"),
	   	path('addl', views.addl, name="addl"),
	   	path('studentdashboard', views.studentdashboard, name='studentdashboard')
    	

]