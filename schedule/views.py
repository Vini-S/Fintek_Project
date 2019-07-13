from django.shortcuts import render, redirect
from schedule.forms import UsersForm
from schedule.models import Users, Course
from schedule.dao import Dao, Student, p_reset, p_update, Student, Faculty, Course, Module, Assign, Session
from django.http import HttpResponse
import jwt
from datetime import datetime, timedelta, date
import requests
import smtplib, ssl
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
import re 
import PyPDF2
from django.core.files.storage import FileSystemStorage

 
def dashboard(request): 
		return render(request,'schedules/Dashboard.html')

def forget(request):
	if "emailid" in request.session:
		return render(request, 'schedules/forget.html')
	else:
		return redirect('index-page')

def index(request):
	return render(request, 'schedules/index.html')

def Plannerform(request, c_code_selected=None):
	dao1 = Student()  
	dao2 = Course()
	dao3 = Faculty()
	lst1 = dao1.selectcourse()
	lst2 = dao2.selectmodule(c_code_selected)
	lst3 = dao3.selectfaculty()
	context={
		'c_code_selected':c_code_selected,
		'lst1':lst1,
		'lst2':lst2,
		'lst3':lst3
	}
	return render(request,'schedules/session.html',context)

def generateplanner(request):
	course = request.POST.get('c_code')
	module = request.POST.get('mid')
	s_date = request.POST.get('date')
	a = datetime.strptime(s_date, '%Y-%m-%d').date()
	faculty = request.POST.get('f_id')
	batch = request.POST.get('Batch')
	dao2 = Course()
	dao = Session()
	mod = 0
	list1 = []
	if module != "0":
		mod = dao.modulesession(module)
		a1 = mod[0][0]
		if batch == "1":
			i = 1
			while i <= a1:
			    a += timedelta(days = 1)
			    if(a.strftime('%A') == 'Monday' or a.strftime('%A') == 'Wednesday' or a.strftime('%A') == 'Friday'):
			        list1.append(str(a))
			        i += 1

		if batch == "2":
			i = 1
			while i <= a1:
			    a += timedelta(days = 1)
			    if(a.strftime('%A') == 'Tuesday' or a.strftime('%A') == 'Thursday' or a.strftime('%A') == 'Saturday'):
			        list1.append(str(a))
			        i += 1

		if batch == "3":
			i = 1
			while i <= a1:
			    a += timedelta(days = 1)
			    if(a.strftime('%A') == 'Saturday' or a.strftime('%A') == 'Sunday'):
			        list1.append(str(a))
			        i += 1

		if batch == "4":
			i = 1
			while i <= a1:
			    a += timedelta(days = 1)
			    list1.append(str(a))
			    i += 1

		row1 = list(dao.sessiondisplay(module))
		print(row1)
		lst2 = []

		for i in range(len(row1)):
			lst = []
			for j in row1[i]:
				lst.append(j)
			lst.append(list1[i])
			lst2.append(lst)

		context ={
		'lst2':lst2,

		}
		return render(request, 'schedules/session_display.html', context)
	else:
		lst1 = dao2.selectmodule(course)
		for i,j in lst1:
			k = 0
			a = [i]
			l = dao.modulesession(a)
			mod = mod + l[k][k]
			k = k+1
		print(mod)
		row1 = dao.session_display()
		context = {
			'row1':row1
		}
		return render(request, 'schedules/session_display.html', context)

	return redirect('Planner-form')

def addstudent(request):
	if "emailid" in request.session:
		dao = Student()
		lst1 = dao.selectcourse()
		context ={ 
			'lst1':lst1
		}
		return render(request, 'schedules/addstudent.html',context)
	else:
		return redirect('index-page')

def vstudent(request):
	if "emailid" in request.session:
		dao = Student()
		row = dao.viewstudent()
		context = {
			'row':row
		}
		return render(request, 'schedules/viewstudent.html',context)
	else:
		return redirect('index-page')

def estudent(request):
	if "emailid" in request.session:
		sid = request.GET.get('sid')
		dao = Student()
		lst1 = dao.selectcourse()
		row = dao.viewstudentbyid(sid)
		context = {
			'lst1':lst1,
			'row':row
		}
		return render(request, 'schedules/editstudent.html',context)
	else:
		return redirect('index-page')

def accepts(request):
	if "emailid" in request.session:
		l_id = request.GET.get('l_id')
		print("l_id",l_id)
		dao = Student()
		a = dao.acceptstudent('l_id')
		print("a",a)
		row = dao.viewleave()
		context={
			'a':a,
			'row':row
		}
		if dao.acceptstudent(l_id) > 0:
			print("printed")
			return render(request,'schedules/studentleave.html',context)
	else:
		return redirect('index-page')

def rejects(request):
	if "emailid" in request.session:
		l_id = request.GET.get('l_id')
		dao = Student()
		a = dao.rejectstudent('l_id')
		print(a)
		row = dao.viewleave()
		context={
			'a':a,
			'row':row
		}
		if dao.rejectstudent(l_id) > 0:
			return render(request,'schedules/studentleave.html',context)
	else:
		return redirect('index-page')


def addfaculty(request):
	if "emailid" in request.session:
		return render(request, 'schedules/addfaculty.html')
	else:
		return redirect('index-page')

def vfaculty(request):
	if "emailid" in request.session:
		dao = Faculty()
		row = dao.viewfaculty()
		context = {
			'row':row
		}
		return render(request, 'schedules/viewfaculty.html',context)
	else:
		return redirect('index-page')

def efaculty(request):
	if "emailid" in request.session:
		fid = request.GET.get('fid')
		dao = Faculty()
		row = dao.viewfacultybyid(fid)
		context ={
			'row':row
		}
		return render(request, 'schedules/editfaculty.html',context)
	else:
		return redirect('index-page')

def acceptf(request):
	if "emailid" in request.session:
		l_id = request.GET.get('l_id')
		dao = Faculty()
		a = dao.acceptfaculty('l_id')
		row = dao.fviewleave()
		context={
			'a':a,
			'row':row
		}
		if dao.acceptfaculty(l_id) > 0:
			return render(request,'schedules/facultyleave.html',context)
	else:
		return redirect('index-page')

def rejectf(request):
	if "emailid" in request.session:
		l_id = request.GET.get('l_id')
		dao = Faculty()
		a = dao.rejectfaculty('l_id')
		row = dao.fviewleave()
		context={
			'a':a,
			'row':row
		}
		if dao.rejectfaculty(l_id) > 0:
			return render(request,'schedules/facultyleave.html',context)
	else:
		return redirect('index-page')	

def addcourse(request):
	if "emailid" in request.session:
		return render(request, 'schedules/addcourse.html')
	else:
		return redirect('index-page')

def vcourse(request):
	if "emailid" in request.session:
		dao = Course()
		row = dao.viewcourse()
		context = {
			'row':row
		}
		return render(request, 'schedules/viewcourse.html',context)
	else:
		return redirect('index-page')


def ecourse(request):
	if "emailid" in request.session:
		c_code = request.GET.get('c_code')
		dao = Course()
		row = dao.viewcoursebyid(c_code)
		context ={
			'row':row
		}
		return render(request, 'schedules/editcourse.html',context)
	else:
		return redirect('index-page')


def addmodule(request):
	if "emailid" in request.session:
		return render(request, 'schedules/addmodule.html')
	else:
		return redirect('index-page')

def vmodule(request):
	if "emailid" in request.session:
		dao = Module()
		row = dao.viewmodule()
		context = {
			'row':row
		}
		return render(request, 'schedules/viewmodule.html',context)
	else:
		return redirect('index-page')

def emodule(request):
	if "emailid" in request.session:
		mid = request.GET.get('mid')
		dao = Module()
		row = dao.viewmodulebyid(mid)
		context ={
			'row':row
		}
		return render(request, 'schedules/editmodule.html',context)
	else:
		return redirect('index-page')

def assigncm(request):
	if "emailid" in request.session:
		dao = Assign()
		lst1 = dao.selectcourse()
		lst2 = dao.selectmodule()
		context ={
			'lst1':lst1,
			'lst2':lst2
		}
		return render(request, 'schedules/assignmodule.html',context)
	else:
		return redirect('index-page')	

def vassign(request):
	if "emailid" in request.session:
		dao = Assign()
		row = dao.viewassign()
		context = {
			'row':row
		}
		return render(request, 'schedules/viewassign.html',context)
	else:
		return redirect('index-page')

def eassign(request):
	if "emailid" in request.session:
		cmid = request.GET.get('cmid')
		dao = Assign()
		row = dao.viewassignbyid(cmid)
		lst1 = dao.selectcourse()
		lst2 = dao.selectmodule()
		context ={
			'row':row,
			'lst1':lst1,
			'lst2':lst2
		}
		return render(request, 'schedules/editassign.html',context)
	else:
		return redirect('index-page')


def logout(request):
	try:
		del request.session['emailid']
		print(request.session['emailid'])
	except KeyError:
		pass
	return render(request, 'schedules/index.html')

def p_complete(request):
	
	if request.method == "POST":
		usertype = request.POST['usertype']
		emailid = request.POST['emailid']
		password = request.POST['new_password']
		confirm_password = request.POST['confirm_password']
		if confirm_password == password:	
			dao = p_update()
			if dao.update(usertype, emailid, password) > 0:
				return render(request,'schedules/password_reset_complete.html')
			else:
				return render(request, 'schedules/forget.html')
		else:
			return render(request, 'schedules/forget.html')
			

def p_confirm(request):
	return render(request, 'schedules/password_reset_confirm.html')

def reset(request):
	emailid = request.POST.get('emailid')
	dao = p_reset()
	if dao.reset(emailid) > 0:
		sender_email = "fintekschedule@gmail.com"
		receiver_email = emailid
		password = "passwd!Q123"
		message = MIMEMultipart("alternative")
		message["Subject"] = "multipart test"
		message["From"] = sender_email
		message["To"] = receiver_email
		# Create the plain-text and HTML version of your message
		html = """\
			<html>
			<body style="background-color: #f4f4f4;">
			<table cellpadding="0" cellspacing="0" width="100%">
			     <tr><td bgcolor="#a4e2f2" align="center"  style="padding: 50px 10px 40px 10px;">    
			        </td></tr><tr><td bgcolor="#a4e2f2" align="center" style="padding: 0px 10px 0px 10px;">
			            <table border="0" cellpadding="0" cellspacing="0" width="480" >
			                <tr><td bgcolor="#ffffff" align="center" valign="top" style="padding: 20px 20px 20px 20px; color: #111111; font-family:Arial; font-size: 48px; font-weight: 400; letter-spacing: 4px;">
			                      <h1 style="font-size: 32px; font-weight: 400; margin: 0;">Forgot password ?</h1>
			                    </td></tr></table></td></tr><tr>
			        <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
			            <table border="0" cellpadding="0" cellspacing="0" width="480" ><tr>
			                <td bgcolor="#ffffff" align="left" style="padding: 20px 30px 40px 30px; color: #666666; font-family:Arial; font-size: 18px; line-height: 25px;" >
			                  <p>You're receiving this email because you requested a password reset for your user account at Fintek Schedule.</p>
			                  <p>Follow the link bellow to reset your password.</p></td></tr><tr>
			                <td bgcolor="#ffffff" align="left">
			                  <table width="100%" border="0" cellspacing="0" cellpadding="0">
			                    <tr><td bgcolor="#ffffff" align="center" style="padding: 20px 30px 60px 30px;">
			                        <table border="0" cellspacing="0" cellpadding="0">
			                          <tr><td align="center" style="border-radius: 3px;" bgcolor="#a4e2f2"><a href="http://127.0.0.1:8080/password_reset_confirm/" target="_blank" style="font-size: 20px; font-family:Arial; color: #111111; text-decoration: none; color: #111111; text-decoration: none; padding: 15px 25px; border-radius: 2px; border: 1px solid #111111; display: inline-block;">Reset Password</a></td></tr>
			                        </table></td></tr></table></td></tr></table></td></tr><tr>
			        <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
			            <table border="0" cellpadding="0" cellspacing="0" width="480" >
			                <!-- HEADLINE -->
			                <tr><td bgcolor="#111111" align="center" style="padding: 30px 30px 30px 30px; color: #ffffff; font-family:Arial; font-size: 18px; font-weight: 400; line-height: 25px;" >
			                    <h2 style="font-size: 24px; font-weight: 400; margin: 0;">Thank you for using our site.</h2> </td></tr></table></td></tr></table></body>
			</html>
				"""

		# Turn these into plain/html MIMEText objects
		part2 = MIMEText(html, "html")
		# Add HTML/plain-text parts to MIMEMultipart message
		# The email client will try to render the last part first
		
		message.attach(part2)

		# Create secure connection with server and send email
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		    server.login(sender_email, password)
		    server.sendmail(
		    sender_email, receiver_email, message.as_string()
		    )	

		return render(request, 'schedules/password_reset_done.html')
	else:
		return render(request, 'schedules/forget.html')

def addsession(request):
	dao = Session()
	lst1 = dao.selectcourse()
	context ={
		'lst1':lst1
	}
	return render(request, 'schedules/sessionform.html',context)

def login(request):
	emailid = request.POST.get('emailid')
	password = request.POST.get('password')
	dao = Dao()
	userdetails = dao.login(emailid, password)
	if userdetails is not None :
		time1 = datetime.now()
		request.session.set_expiry(600)
		request.session["emailid"] = emailid
		emailid = request.session["emailid"]
		usertype = userdetails[0][0]
		if (usertype == 1):
			return render(request, 'schedules/Dashboard.html')
		elif(usertype == 2):
			return render(request, 'Faculty/faculty_dashboard.html')
		elif(usertype == 3):
			return render(request, 'Student/students_dashboard.html')
		else:
			return render(request, 'schedules/index.html')
	else:
		return render(request, 'schedules/index.html')

def add(request):
	if "emailid" in request.session:
		f_name = request.POST.get('f_name')
		l_name = request.POST.get('l_name')
		emailid = request.POST.get('emailid')
		password = request.POST.get('password')
		c_code = request.POST.get('c_code')
		dao = Student()
		lst1 = dao.selectcourse()
		context={
		 	'lst1':lst1,
		'addstudent':"addstudent"
		}
		if dao.add(f_name, l_name, emailid, password, c_code) > 0:
			return redirect('viewstudent')
		else:
			return redirect('dashboard')
	else:
		return redirect('index-page')

def viewstudent(request):
	if "emailid" in request.session:
		dao = Student()
		row = dao.viewstudent()
		context = {
			'row':row
		}
		if dao.viewstudent():
			return render(request,'schedules/viewstudent.html',context)
		else:
			return render(request,'schedules/Dashboard.html')
	else:
		return redirect('index-page')

def editstudent(request):
	if "emailid" in request.session:
		sid = request.POST.get('sid')
		f_name = request.POST.get('f_name')
		l_name = request.POST.get('l_name')
		emailid = request.POST.get('emailid')
		c_code = request.POST.get('c_code')

		dao = Student()
		lst1 = dao.selectcourse()
		row = dao.viewstudentbyid(sid)
		context ={
			'lst1':lst1,
			'row': row,
		'estudent': "estudent"
		}
		if dao.editstudent(f_name, l_name, emailid, c_code, sid) > 0:
			return redirect('viewstudent')
	else:
		return redirect('index-page')


def deletestudent(request):
	if "emailid" in request.session:

		# sid = request.GET.get('sid')
		email = request.GET.get('email')
		dao = Student()
		lst1 = dao.deletestudent(email)
		print(lst1)
		context = {
			'lst1':lst1
		# 'deletestudent':"deletestudent"
		}
		if dao.deletestudent(email) > 0:
			return redirect('viewstudent')
	else:
		return redirect('index-page')

def sviewleave(request):									#for viewing leaves (tables)
	if "emailid" in request.session:
		dao = Student()
		row = dao.viewleave() 
		context = {
			'row':row
		}
		if dao.viewleave():
			return render(request,'schedules/studentleave.html',context)
		else:
			return redirect('dashboard')
	else:
		return redirect('index-page')

def acceptsleave(request):                              
	if "emailid" in request.session:
		l_id = request.POST.get('l_id')
		print("l_id1:",l_id)
		dao = Student()
		a = dao.acceptstudent(l_id)
		print("a1:",a)
		row = dao.viewleave()
		context={
			'a':a,
			'row':row
		}
		if dao.acceptstudent() > 0:
			print("def")
			return redirect('studentleave')
	else:
		return redirect('index-page')

def rejectsleave(request):
	if "emailid" in request.session:
		l_id = request.POST.get('l_id')
		print("l_id1:",l_id)
		dao = Student()
		a = dao.rejectstudent(l_id)
		print("a1:",a)
		row = dao.viewleave()
		context = {
			'a':a,
			'row':row
		}
		if dao.rejectstudent() > 0:
			print("def")
			return redirect('studentleave')
	else:
		return redirect('index-page')

def search(request):
	if "emailid" in request.session:
		name = request.POST.get('name')
		dao = Student()
		dao1 = Faculty()
		dao2 = Course()
		row = dao.searchstudent(name)
		row1 = dao1.searchfaculty(name)
		row2 = dao2.searchcourse(name)
		context = {
				'row':row
		}
		context1 = {     
				'row1':row1
		}
		context2 = {
				'row2':row2
		}	
		if dao.searchstudent(name):
			print(name)
			return render(request,'schedules/view_after_search.html',context)
		elif dao1.searchfaculty(name):
			return render(request, 'schedules/f_view_after_search.html', context1)
		elif dao2.searchcourse(name):
			return render(request, 'schedules/c_view_after_search.html', context2)
		else:
			return render(request, 'schedules/Dashboard.html')
	else:
		return redirect('index-page')


def addf(request):
	if "emailid" in request.session:
		# fid = request.POST.get('fid')
		f_name = request.POST.get('f_name')
		l_name = request.POST.get('l_name')
		emailid = request.POST.get('emailid')
		password = request.POST.get('password')
		phno = request.POST.get('phno')
		dao = Faculty()
		context={
		'addfaculty':"addfaculty"
		}
		if dao.addf(f_name, l_name, emailid, password, phno) > 0:
			return redirect('viewfaculty')
		else:
			return render(request, 'schedules/Dashboard.html')
	else:
		return redirect('index-page')


def viewfaculty(request):
	if "emailid" in request.session:
		dao = Faculty()
		row = dao.viewfaculty()
		context = {
			'row':row
		}
		if dao.viewfaculty():
			return render(request,'schedules/viewfaculty.html',context)
		else:
			return render(request,'schedules/Dashboard.html')
	else:
		return redirect('index-page')



def editfaculty(request):
	if "emailid" in request.session:
		fid = request.POST.get('fid')
		f_name = request.POST.get('f_name')
		l_name = request.POST.get('l_name')
		emailid = request.POST.get('emailid')
		phno = request.POST.get('phno')
		dao = Faculty()
		row = dao.viewfacultybyid(fid)
		context ={
			'row': row,
		'editfaculty': "editfaculty"
		}
		if dao.editfaculty(f_name, l_name, emailid, phno, fid) > 0:
			return redirect('viewfaculty')
	else:
		return redirect('index-page')

def deletefaculty(request):
	if "emailid" in request.session:
		email = request.GET.get('email')
		dao = Faculty()
		lst1 = dao.deletefaculty(email)
		context = {
			'lst1':lst1,
		'deletefaculty':"deletefaculty"
		}
		if dao.deletefaculty(email) > 0:
			return redirect('viewfaculty')
	else:
		return redirect('index-page')

def fviewleave(request):									#for viewing leaves (tables)
	if "emailid" in request.session:
		dao = Faculty()
		row = dao.fviewleave()
		context = {
			'row':row
		}
		if dao.fviewleave():
			return render(request,'schedules/facultyleave.html',context)
		else:
			return redirect('dashboard')	
	else:
		return redirect('index-page')
		


def acceptfleave(request):                              
	if "emailid" in request.session:
		l_id = request.POST.get('l_id')
		# print("l_id1:",l_id)
		dao = Faculty()
		a = dao.acceptfaculty(l_id)
		# print("a1:",a)
		row = dao.fviewleave()
		context={
			'a':a,
			'row':row
		}
		if dao.acceptfaculty() > 0:
			# print("def")
			return redirect('facultyleave')
	else:
		return redirect('index-page')

def rejectfleave(request):
	if "emailid" in request.session:
		l_id = request.POST.get('l_id')
		# print("l_id1:",l_id)
		dao = Faculty()
		a = dao.rejectfaculty(l_id)
		# print("a1:",a)
		row = dao.fviewleave()
		context = {
			'a':a,
			'row':row
		}
		if dao.rejectfaculty() > 0:
			print("def")
			return redirect('facultyleave')
	else:
		return redirect('index-page')

def addc(request):
	if "emailid" in request.session:
		c_code = request.POST.get('c_code')
		name = request.POST.get('name')
		dao = Course()
		context = {
		'addcourse':"addcourse"
		}		
		if dao.addc(c_code, name) > 0:
			return redirect('viewcourse')
		else:
			return redirect('dashboard')
	else:
		return redirect('index-page')

def viewcourse(request):
	if "emailid" in request.session:
		dao = Course()
		row = dao.viewcourse()
		context = {
			'row':row
		}
		if dao.viewcourse():
			return render(request,'schedules/viewcourse.html',context)
		else:
			return redirect('dashboard')
	else:
		return redirect('index-page')

def editcourse(request):
	if "emailid" in request.session:
		c_code = request.POST.get('c_code')
		name = request.POST.get('name')
		dao = Course()
		row = dao.viewcoursebyid(c_code)
		context ={
			'row': row,
		'editcourse': "editcourse"
		}
		if dao.editcourse(name, c_code) > 0:
			return redirect('viewcourse')
	else:
		return redirect('index-page')

def deletecourse(request):
	if "emailid" in request.session:
		c_code = request.GET.get('c_code')
		dao = Course()
		lst1 = dao.deletecourse(c_code)
		context = {
			'lst1': lst1,
		'deletecourse':"deletecourse"
		}
		if dao.deletecourse(c_code) > 0:
			return redirect('viewcourse')
	else:
		return redirect('index-page')


def addm(request):
	mid = request.POST.get('mid')
	file = request.FILES['mfile']
	fs = FileSystemStorage()
	filename = fs.save(file.name, file)
	uploaded_file_url = fs.url(filename)
	object = open(uploaded_file_url, 'rb')
	reader = PyPDF2.PdfFileReader(object)
	length = reader.numPages
	reg6 = []
	allSessions = []
	for i in range(3, length):
	    page = reader.getPage(i)
	    s = page.extractText()
	    if(re.search("Session Coverage", s)):
	        pIndex = i
	        for i in range(pIndex,length):            # to extract the content of pdf in fixed range
	            page = reader.getPage(i)
	            s1 = page.extractText()                     
	            reg = re.sub("-", "", s1)                # page formating 
	            s1 = re.sub("\n", "", s1)                  # page formating 
	            allSessions += s1.split()
	            reg5 = re.findall("T\d{1,}|TL\d{1,}", s1)                        # to extract number of modules TL                     
	            reg6 += reg5      #appends Module name of all pages in one list i.e reg6        
	sessions = []
	for i in allSessions:                    # code to search TG or Workshop for the sessions dictionary
	    if(re.search("TG", i)):
	        re1 = re.findall("TG", i)
	        sessions += re1           
	    elif(re.search("workshop|Lab",i)):
	        re2 = re.findall("workshop|Lab",i)
	        sessions += re2    
	for n, i in enumerate(sessions):    # code for replacing REG with Sessions
	    if i == "TG":
	        sessions[n] = "Sessions"
	    elif i == "Lab":
	        sessions[n] = "Workshop"
	dictionary = dict(zip(reg6, sessions))  #final converted  dictionary
	data = []
	for k,v in (dictionary.items()):
		tpl = (mid, k, v)
		data.append(tpl)
	dao = Module()
	context = {
	'addmodule':"addmodule"
	}
	if dao.addm(data) > 0:
		return render(request,'schedules/addmodule.html',context)
	else:
		return render(request, 'schedules/index.html')
	
def viewmodule(request):
	if "emailid" in request.session:
		dao = Module()
		row = dao.viewmodule()
		context = {
			'row':row
		}
		if dao.viewmodule():
			return render(request,'schedules/viewmodule.html',context)
		else:
			return render(request,'schedules/Dashboard.html')
	else:
		return redirect('index-page')

def editmodule(request):
	if "emailid" in request.session:
		mid = request.POST.get('mid')
		name = request.POST.get('name')
		dao = Module()
		row = dao.viewmodulebyid(mid)
		context ={
			'row': row,
		'emodule': "emodule"
		}
		if dao.editmodule(name, mid) > 0:
			return redirect('viewmodule')
	else:
		return redirect('index-page')

def deletemodule(request): 
	if "emailid" in request.session:
		mid = request.GET.get('mid')
		dao = Module()
		lst1 = dao.deletemodule(mid)
		context = {
			'lst1':lst1,
		'deletemodule':"deletemodule"
		}
		if dao.deletemodule(mid) > 0:
			return redirect(viewmodule)
	else:
		return redirect('index-page')

def assignmodule(request):
	if "emailid" in request.session:
		c_code = request.POST.get('c_code')
		mid_list = []
		a=0	
		while True:
			temp ="mid"+ str(a)
			if request.POST.get(temp):
				mid_list.append(request.POST.get(temp))
				a=a+1
			else:
				break
		dao = Assign()
		for i in mid_list:
			result = dao.assignm(c_code,i)
			if result != 1:
				return render(request, 'schedules/Dashboard.html')
		return redirect('viewassign')
	else:
		return redirect('index-page')

def viewassign(request):
	if "emailid" in request.session:
		dao = Assign()
		row = dao.viewassign()
		context = {
			'row':row
		}
		if dao.viewassign():
			return render(request,'schedules/viewassign.html',context)
		else:
			return redirect('dashboard')
	else:
		return redirect('index-page')

def editassign(request):
	if "emailid" in request.session:
		cmid = request.POST.get('cmid')
		c_code = request.POST.get('c_code')
		mid = request.POST.get('mid')
		dao = Assign()
		row = dao.viewassignbyid(cmid)
		lst1 = dao.selectcourse()
		lst2 = dao.selectmodule()
		context ={
			'row': row,
			'lst1':lst1,
			'lst2':lst2
		}
		if dao.editassign(c_code, mid, cmid) > 0:
			return redirect('viewassign')
	else:
		return redirect('index-page')

def deleteassign(request): 
	if "emailid" in request.session:
		cmid = request.GET.get('cmid')
		dao = Assign()
		lst1 = dao.deleteassign(cmid)
		context = {
			'lst1':lst1
		}
		if dao.deleteassign(cmid) > 0:
			return redirect('viewassign')
	else:
		return redirect('index-page')

def addse(request):
	
	seid = request.POST.get('id')
	sedate = request.POST.get('sedate')
	sedetail = request.POST.get('sedetail')
	seowner = request.POST.get('seowner')
	c_code = request.POST.get('c_code')
	fid = request.POST.get('fid')
	mid = request.POST.get('mid')
	dao = Session()
	lst1 = dao.selectcourse()
	context={
	 	'lst1':lst1,
	'sessionform':"addstudent"
	}
	if dao.add(name, emailid, password, c_code) > 0:
		return render(request,'schedules/addstudent.html',context)
	else:
		return render(request, 'schedules/Dashboard.html')

def leave(request):
	if "emailid" in request.session:
		return render(request, 'schedules/leave.html')
	else:
		return redirect('index-page')


def viewleave(request):
	if "emailid" in request.session:
		return render(request, 'schedules/viewleave.html')
	else:
		return redirect('index-page')


def calender(request):
	if "emailid" in request.session:
		return render(request, 'schedules/calender.html')
	else:
		return redirect('index-page')
