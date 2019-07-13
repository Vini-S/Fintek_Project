from django.contrib import admin
from django.urls import path, include 
from Faculty import views


urlpatterns = [

	    path('fstudentview', views.fstudentview,name="fstudentview"),
	    path('facultyviewf', views.facultyviewf,name="facultyviewf"),
	    path('fcourseview', views.fcourseview,name="fcourseview"),
	    path('fmoduleview', views.fmoduleview,name="fmoduleview"),
	   	path('faculty_view_after_search/', views.facultysearch,name="faculty_view_after_search"),
	   	path('fviewleave', views.fviewleave, name="fviewleave"),
	   	path('fsviewleave', views.Sviewleave, name="fsviewleave"),
	   	path('apply_for_leave', views.apply_for_leave, name="apply_for_leave"),
	   	path('fcalender', views.fcalender, name="fcalender"),
	   	path('addfleave', views.addfleave, name="addfleave"),
	   	path('applyleave', views.applyleave, name="applyleave")


]