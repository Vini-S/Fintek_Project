from django.shortcuts import render, redirect
from Faculty.daofaculty import Student, Course, Faculty, Module



def facultydashboard(request):
	return render(request, 'Faculty/faculty_dashboard.html')

def applyleave(request):
	if "emailid" in request.session:
		emailid = request.session['emailid']
		dao = Faculty()
		row = dao.viewfleavebysession(emailid)
		context = {
			'row':row
		}
		return render(request, 'Faculty/leaveform.html',context)
	else:
		return redirect('index-page')

def addleave(request):
	if "emailid" in request.session:
		emailid = request.session['emailid']
		dao = Faculty()
		row = dao.viewfleavebysession(emailid)
		context = {
			'row':row
		}
		return render(request, 'Faculty/fviewleave.html',context)
	else:
		return redirect('index-page')

def fstudentview(request):
	if "emailid" in request.session:
		dao = Student()
		row = dao.studentview()
		context = {
			'row':row
		}
		if dao.studentview():
			return render(request,'Faculty/fstudentview.html',context)
		else:
			return render(request,'Faculty/faculty_dashboard.html')
	else:
		return redirect('index-page')		

def facultyviewf(request):
	if "emailid" in request.session:
		dao = Faculty() 
		row = dao.facultyview()
		context = {
			'row':row 
		}
		if dao.facultyview():
			return render(request,'Faculty/facultyviewf.html',context)
		else:
			return render(request,'Faculty/faculty_dashboard.html')
	else:
		return redirect('index-page')

def fvstudent(request):
	if "emailid" in request.session:
		dao = Student()
		row = dao.studentview()  
		context = {
			'row':row
		}
		return render(request, 'Faculty/fstudentview.html',context)
	else:
		return redirect('index-page')

def fvfaculty(request):
	if "emailid" in request.session:
		dao = Faculty()
		row = dao.facultyview()
		context = {
			'row':row
		}
		return render(request, 'Faculty/facultyviewf.html',context)
	else:
		return redirect('index-page')

def fcourseview(request):
	if "emailid" in request.session:
		dao = Course()
		row = dao.courseview()
		context = {
			'row':row
		}
		if dao.courseview():
			return render(request,'Faculty/fcourseview.html',context)
		else:
			return render(request,'Faculty/faculty_dashboard.html')
	else:
		return redirect('index-page')


def fvcourse(request):
	if "emailid" in request.session:
		dao = Course()
		row = dao.courseview()
		context = {
			'row':row
		}
		return render(request, 'Faculty/fcourseview.html',context)
	else:
		return redirect('index-page')


def fmoduleview(request):
	if "emailid" in request.session:
		dao = Module()
		row = dao.moduleview()
		context = {
			'row':row
		}
		if dao.moduleview():
			return render(request,'Faculty/fmoduleview.html',context)
		else:
			return render(request,'Faculty/faculty_dashboard.html')
	else:
		return redirect('index-page')

def fvmodule(request):
	if "emailid" in request.session:
		dao = Module()
		row = dao.moduleview()
		context = {
			'row':row
		}
		return render(request, 'Faculty/fmoduleview.html',context)
	else:
		return redirect('index-page')

def facultysearch(request):
	if "emailid" in request.session:
		name = request.POST.get('name')
		dao = Student()
		dao1 = Faculty()
		dao2 = Course()
		row = dao.studentsearch(name)
		row1 = dao1.facultysearch(name)
		row2 = dao2.coursesearch(name)
		context = {
				'row':row
		}
		context1 = {
				'row1':row1
		}
		context2 = {
				'row2':row2
		}
		if dao.studentsearch(name):
			return render(request,'faculty/studentfaculty_view_after_search.html',context)
		elif dao1.facultysearch(name):
			return render(request, 'Faculty/faculty_view_after_search.html', context1)
		elif dao2.coursesearch(name):
			return render(request, 'Faculty/coursefaculty_view_after_search.html', context2)
		else:
			return render(request, 'Faculty/faculty_dashboard.html')
	else:
		return redirect('index-page')


def addfleave(request):
	emailid = request.session['emailid']
	start_date = request.POST.get('start')
	end_date = request.POST.get('end')
	reason = request.POST.get('reason')
	dao = Faculty()
	if dao.addleave(emailid, start_date, end_date, reason) > 0:
		return redirect('fviewleave')

def apply_for_leave(request):										#for applying leave (forms)
	if "emailid" in request.session:
		emailid = request.session['emailid']
		dao = Faculty()
		row = dao.viewfleavebysession(emailid)
		context = {
			'row':row
		} 
		return render(request, 'Faculty/leaveform.html',context)
	else:
		return redirect('index-page')


def fviewleave(request):									#for viewing leaves (tables)
	if "emailid" in request.session:
		dao = Faculty()
		row = dao.viewleave()
		context = {
			'row':row
		}
		if dao.viewleave():
			return render(request,'Faculty/fviewleave.html',context)
		else:
			return render(request,'Faculty/faculty_dashboard.html')	
	else:
		return redirect('index-page')


def Sviewleave(request):									#for viewing leaves (tables)
	if "emailid" in request.session:
		dao = Student()
		row = dao.sviewleave()
		context = {
			'row':row
		}
		if dao.sviewleave():
			return render(request,'Faculty/fsviewleave.html',context)
		else: 
			return render(request,'Faculty/faculty_dashboard.html')	
	else:
		return redirect('index-page')


def fcalender(request):
	if "emailid" in request.session:
		return render(request, 'Faculty/fcalender.html')
	else:
		return redirect('index-page')

