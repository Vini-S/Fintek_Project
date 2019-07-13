from django.shortcuts import render, redirect
from Student.dao import Student, Course, Faculty, Module



def studentdashboard(request):
	return render(request,'Students/students_dashboard.html')

def applyleave(request):
	if "emailid" in request.session:
		emailid = request.session['emailid']
		dao = Student()
		row = dao.viewsleavebysession(emailid)
		context = {
			'row':row
		}
		return render(request, 'Student/sleave.html',context)
	else:
		return redirect('index-page')

def addleave(request):
	if "emailid" in request.session:
		emailid = request.session['emailid']
		dao = Student()
		row = dao.viewsleavebysession(emailid)
		context = {
			'row':row
		} 
		return render(request, 'Student/sleave.html',context)
	else:
		return redirect('index-page')


def studentview(request):
	if "emailid" in request.session:
		dao = Student()
		row = dao.studentview()
		context = {
			'row':row
		} 
		if dao.studentview():
			return render(request,'Student/sviewstudent.html',context)
		else:
			return render(request,'Student/students_dashboard.html')
	else:
		return redirect('index-page')		

def facultyview(request):
	if "emailid" in request.session:
		dao = Faculty() 
		row = dao.facultyview()
		context = {
			'row':row
		}
		if dao.facultyview():
			return render(request,'Student/sviewfaculty.html',context)
		else:
			return render(request,'Student/students_dashboard.html')
	else:
		return redirect('index-page')

def studentv(request):
	if "emailid" in request.session:
		dao = Student()
		row = dao.studentview()
		context = {
			'row':row
		}
		return render(request, 'Student/sviewstudent.html',context)
	else:
		return redirect('index-page')

def facultyv(request):
	if "emailid" in request.session:
		dao = Faculty()
		row = dao.facultyview()
		context = {
			'row':row
		}
		return render(request, 'Student/sviewfaculty.html',context)
	else:
		return redirect('index-page')

def courseview(request):
	if "emailid" in request.session:
		dao = Course()
		row = dao.courseview()
		context = {
			'row':row
		}
		if dao.courseview():
			return render(request,'Student/sviewcourse.html',context)
		else:
			return render(request,'Student/students_dashboard.html')
	else:
		return redirect('index-page')


def coursev(request):
	if "emailid" in request.session:
		dao = Course()
		row = dao.courseview()
		context = {
			'row':row
		}
		return render(request, 'Student/sviewcourse.html',context)
	else:
		return redirect('index-page')


def moduleview(request):
	if "emailid" in request.session:
		dao = Module()
		row = dao.moduleview()
		context = {
			'row':row
		}
		if dao.moduleview():
			return render(request,'Student/sviewmodule.html',context)
		else:
			return render(request,'Student/students_dashboard.html')
	else:
		return redirect('index-page')

def modulev(request):
	if "emailid" in request.session:
		dao = Module()
		row = dao.moduleview()
		context = {
			'row':row
		}
		return render(request, 'Student/sviewmodule.html',context)
	else:
		return redirect('index-page')

def studentsearch(request):
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
			return render(request,'Student/student_view_after_search.html',context)
		elif dao1.facultysearch(name):
			return render(request, 'Student/facultystudent_view_after_search.html', context1)
		elif dao2.coursesearch(name):
			return render(request, 'Student/coursestudent_view_after_search.html', context2)
		else:
			return render(request, 'Student/students_dashboard.html')
	else:
		return redirect('index-page')

def sleave(request):										#for applying leave (forms)
	if "emailid" in request.session:
		emailid = request.session['emailid']
		dao = Student()
		row = dao.viewsleavebysession(emailid)
		context = {
			'row':row
		} 
		return render(request, 'Student/sleave.html')
	else:
		return redirect('index-page')

def addl(request):
	emailid = request.session['emailid']
	start_date = request.POST.get('start')
	end_date = request.POST.get('end')
	reason = request.POST.get('reason')
	dao = Student()
	if dao.addleave(emailid, start_date, end_date, reason) > 0:
		return redirect('sviewleave')

def sviewleave(request):									#for viewing leaves (tables)
	if "emailid" in request.session:
		dao = Student()
		row = dao.viewleave()
		context = {
			'row':row
		}
		if dao.viewleave():
			return render(request,'Student/sviewleave.html',context)
		else:
			return render(request,'Student/students_dashboard.html')	
	else:
		return redirect('index-page')

def Sfviewleave(request):									#for viewing leaves (tables)
	if "emailid" in request.session:
		dao = Faculty()
		row = dao.fviewleave()
		context = {
			'row':row
		}
		if dao.fviewleave():
			return render(request,'Student/sfviewleave.html',context)
		else:
			return render(request,'Student/students_dashboard.html')	
	else:
		return redirect('index-page')


def scalender(request):
	if "emailid" in request.session:
		return render(request, 'Student/scalender.html')
	else:
		return redirect('index-page')
