from schedule.models import Users
from django.db import connection


class Dao:  
	def login(self, emailid, password):
		cursor = connection.cursor()
		query = ("select * from schedule_users where Email_id=%s and Password=%s")
		values = (emailid, password)
		cursor.execute(query,values) 
		a = cursor.fetchall()
		b = list(a) 
		return b

class p_reset:
	def reset(self,email):
		cursor = connection.cursor() 
		query = ("select Email_id from schedule_users where Email_id=%s")
		values = (email)
		cursor.execute(query,values)
		a = cursor.rowcount
		return a 

class p_update:
	def update(self, usertype, emailid, password):
		cursor = connection.cursor()
		query = "update schedule_users set password=%s where usertype=%s and Email_id=%s"
		values = (password, usertype, emailid)
		cursor.execute(query,values)
		connection.commit()
		return 1

class Student:
	def add(self, f_name, l_name, emailid, password, c_code):
		cursor = connection.cursor()
		query1 = "insert into schedule_student_view(s_f_name, s_l_name, s_Email_id, Password, c_code_id) values (%s,%s,%s,%s,%s)"
		query2 = "insert into schedule_users(Usertype, Email_id, Password) values ('3', %s,%s)"
		values1 = (f_name, l_name, emailid, password, c_code)
		values2 = (emailid, password)
		cursor.execute(query1,values1)
		cursor.execute(query2,values2)
		connection.commit()
		return 1

	def viewstudent(self):
		cursor = connection.cursor()
		query = "select schedule_student_view.s_id, schedule_student_view.s_f_name, schedule_student_view.s_l_name, schedule_student_view.s_Email_id, schedule_student_view.c_code_id,schedule_course.c_name from schedule_course INNER JOIN schedule_student_view ON schedule_student_view.c_code_id=schedule_course.c_code"
		cursor.execute(query)
		row = cursor.fetchall()
		return row

	def viewstudentbyid(self, sid):       #(Auto fill form) 
		cursor = connection.cursor()
		query = "select s_id, s_f_name, s_l_name, s_Email_id, c_code_id from schedule_student_view where s_id=%s"
		values = (sid)
		cursor.execute(query,values)
		row = cursor.fetchall()
		return row

	def selectcourse(self):     		 #(Drop Down list)
		cursor = connection.cursor()
		query = "select c_code, c_name from schedule_course"
		cursor.execute(query)
		lst1 = cursor.fetchall()
		return lst1

	def editstudent(self, f_name, l_name, emailid, c_code, sid):
		cursor = connection.cursor()
		query = "update schedule_student_view set s_f_name=%s, s_l_name=%s, s_Email_id=%s, c_code_id=%s where s_id=%s"
		values = (f_name, l_name, emailid, c_code, sid)
		cursor.execute(query,values)
		connection.commit()
		return 1
	
	def deletestudent(self, email):
		cursor = connection.cursor()
		query1 = "delete from schedule_student_view where s_Email_id=%s"
		query2 = "delete from schedule_users where Email_id=%s"
		values1 =(email)
		values2 = (email)
		cursor.execute(query1,values1)
		cursor.execute(query2,values2)
		connection.commit()
		return 1

	def viewleave(self):
		cursor = connection.cursor()
		query = "select l_id, s_email, s_date, e_date, l_reason, s_status from schedule_student_leave"
		cursor.execute(query)
		row = cursor.fetchall()
		return row

	def acceptstudent(self, l_id):
		cursor = connection.cursor()
		query = "update schedule_student_leave set s_status='1' where l_id=%s"
		values = (l_id)
		cursor.execute(query,values)
		connection.commit()
		return 1

	def rejectstudent(self, l_id):
		cursor = connection.cursor()
		query = "update schedule_student_leave set s_status='0' where l_id=%s"
		values = (l_id) 
		cursor.execute(query,values)
		connection.commit()
		return 1

	def searchstudent(self, name):
		cursor = connection.cursor()
		query = "select s_id, s_f_name, s_l_name, s_Email_id, c_code_id from schedule_student_view where s_f_name=%s"
		values = (name)
		cursor.execute(query, values)
		row = cursor.fetchall()
		return row


class Faculty:
	def addf(self, f_name, l_name, emailid, password, phno):
		cursor = connection.cursor()
		query1 = "insert into schedule_faculty_view(f_f_name, f_l_name, f_Email_id, Password, f_phno) values (%s,%s,%s,%s,%s)"
		query2 = "insert into schedule_users(Usertype, Email_id, Password) values ('2', %s, %s)"
		values1 = (f_name, l_name, emailid, password, phno)
		values2 = (emailid, password)
		cursor.execute(query1,values1)
		cursor.execute(query2,values2)
		connection.commit()
		return 1


	def viewfaculty(self):
		cursor = connection.cursor()
		query = "select f_id, f_f_name, f_l_name, f_Email_id, f_phno from schedule_faculty_view "
		cursor.execute(query)
		row1 = cursor.fetchall()
		return row1


	def viewfacultybyid(self, fid):       #(Auto fill form)
		cursor = connection.cursor()
		query = "select f_id, f_f_name, f_l_name, f_Email_id, f_phno from schedule_faculty_view where f_id=%s"
		values = (fid)
		cursor.execute(query,values)
		row = cursor.fetchall()
		return row


	def editfaculty(self, f_name, l_name, emailid, phno, fid):
		cursor = connection.cursor()
		query = "update schedule_faculty_view set f_f_name=%s, f_l_name=%s, f_Email_id=%s, f_phno=%s where f_id=%s"
		values = (f_name, l_name, emailid, phno, fid)
		cursor.execute(query,values)
		connection.commit()
		return 1

	def deletefaculty(self, email):
		cursor = connection.cursor()
		query1 = "delete from schedule_faculty_view where f_Email_id=%s"
		query2 = "delete from schedule_users where Email_id=%s"
		values1 = (email)
		values2 = (email)
		cursor.execute(query1,values1)
		cursor.execute(query2,values2)
		connection.commit()
		return 1

	def fviewleave(self):
		cursor = connection.cursor()
		query = "select l_id, f_email, s_date, e_date, l_reason, f_status from schedule_faculty_leave"
		cursor.execute(query)
		row = cursor.fetchall()
		return row

	def selectfaculty(self):     		 #(Drop Down list)
		cursor = connection.cursor()
		query = "select f_Email_id, f_f_name from schedule_faculty_view"
		cursor.execute(query)
		lst3 = cursor.fetchall()
		return lst3

	def acceptfaculty(self, l_id):
		cursor = connection.cursor()
		query = "update schedule_faculty_leave set f_status='1' where l_id=%s"
		values = (l_id)
		cursor.execute(query,values)
		connection.commit()
		return 1

	def rejectfaculty(self, l_id):
		cursor = connection.cursor()
		query = "update schedule_faculty_leave set f_status='0' where l_id=%s"
		values = (l_id)
		cursor.execute(query,values)
		connection.commit()
		return 1

	def searchfaculty(self, name):
		cursor = connection.cursor()
		query = "select f_id, f_f_name, f_l_name, f_Email_id, f_phno from schedule_faculty_view where f_f_name=%s"
		values = (name)
		cursor.execute(query, values)
		row = cursor.fetchall()
		return row


class Course:
	def addc(self, c_code, name):
		cursor = connection.cursor()
		query = "insert into schedule_course(c_code, c_name) values (%s, %s)"
		values = (c_code, name)
		cursor.execute(query,values)
		connection.commit()
		return 1

	def viewcourse(self):
		cursor = connection.cursor()
		query = "select c_code, c_name from schedule_course"
		cursor.execute(query)
		row = cursor.fetchall()
		# print(row)
		return row

	def viewcoursebyid(self, c_code):
		cursor = connection.cursor()
		query = "select * from schedule_course where c_code=%s"
		values = (c_code)
		cursor.execute(query,values)
		row = cursor.fetchall()
		return row

	def selectmodule(self,c_code_id=None):
		cursor = connection.cursor()
		if c_code_id:
			query = "select m_id, m_name from schedule_chapters where  c_code_id=%s"
			values = (c_code_id)
			cursor.execute(query,values)
		else:
			query = "select m_id, m_name from schedule_chapters"
			cursor.execute(query)
		
		lst1 = cursor.fetchall()
		return lst1

	def editcourse(self, name, c_code):
		cursor = connection.cursor()
		query = "update schedule_course set c_name=%s where c_code=%s"
		values = (name, c_code)
		cursor.execute(query,values)
		connection.commit()
		return 1

	def deletecourse(self, c_code):
		cursor = connection.cursor()
		query = "delete from schedule_course where c_code=%s"
		values = (c_code)
		cursor.execute(query,values)
		connection.commit()
		return 1

	def searchcourse(self, name):
		cursor = connection.cursor()
		query = "select c_code,c_name from schedule_course where c_name=%s"
		values = (name)
		cursor.execute(query, values)
		row = cursor.fetchall()
		return row

class Module:
	def addm(self, data):
		cursor = connection.cursor()
		query = "insert into schedule_modulepm (m_id_id, Session_key, Session_value) values (%s, %s, %s)"
		values = (data)
		cursor.executemany(query,values)
		connection.commit()
		return 1

	def viewmodule(self):
		cursor = connection.cursor()
		query = "select * from schedule_chapters"
		cursor.execute(query)
		row = cursor.fetchall()
		return row

	def viewmodulebyid(self, mid):
		cursor = connection.cursor()
		query = "select * from schedule_chapters where m_id=%s"
		values = (mid) 
		cursor.execute(query,values)
		row = cursor.fetchall()
		return row

	def editmodule(self, name, mid):
		cursor = connection.cursor()
		query = "update schedule_chapters set m_name=%s where m_id=%s"
		values = (name,mid)
		cursor.execute(query,values)
		connection.commit()
		return 1

	def deletemodule(self, mid):
		cursor = connection.cursor()
		query = "delete from schedule_chapters where m_id=%s"
		values = (mid)
		cursor.execute(query,values)
		connection.commit()
		return 1

class Assign:
	def assignm(self, c_code, mid):
		cursor = connection.cursor()
		query = "insert into schedule_coursemodule(c_code_id,m_id_id) values(%s,%s)"
		values = (c_code,mid)
		cursor.execute(query,values)
		connection.commit()
		return 1

	def selectcourse(self):     		 #( course Drop Down list)
		cursor = connection.cursor()
		query = "select c_code, c_name from schedule_course"
		cursor.execute(query)
		lst1 = cursor.fetchall()
		return lst1

	def selectmodule(self):     		 #(Module Drop Down list)
		cursor = connection.cursor()
		query = "select m_id, m_name from schedule_chapters"
		cursor.execute(query)
		lst2 = cursor.fetchall()
		return lst2

	def viewassign(self):
		cursor = connection.cursor()
		query = "select schedule_coursemodule.cm_id, schedule_coursemodule.c_code_id, schedule_course.c_name,schedule_coursemodule.m_id_id,schedule_chapters.m_name from schedule_coursemodule inner join schedule_course on schedule_course.c_code = schedule_coursemodule.c_code_id inner join schedule_chapters on schedule_chapters.m_id = schedule_coursemodule.m_id_id"
		cursor.execute(query)
		row = cursor.fetchall()
		return row

	def viewassignbyid(self, cmid):
		cursor = connection.cursor()
		query = "select * from schedule_coursemodule where cm_id=%s"
		values = (cmid) 
		cursor.execute(query,values)
		row = cursor.fetchall()
		return row

	def editassign(self, c_code, mid, cmid):
		cursor = connection.cursor()
		query = "update schedule_coursemodule set c_code_id=%s, m_id_id=%s  where cm_id=%s"
		values = (c_code,mid,cmid)
		cursor.execute(query,values)
		connection.commit()
		return 1

	def deleteassign(self, cmid):
		cursor = connection.cursor()
		query = "delete from schedule_coursemodule where cm_id=%s"
		values = (cmid)
		cursor.execute(query,values)
		connection.commit()
		return 1

class Session:

	def selectcourse(self,keyword):
		cursor = connection.cursor()
		query = "select c_code,c_name from schedule_course where c_name=%s"
		values = (keyword)
		cursor.execute(query,values)
		row = cursor.fetchall()
		return row

	def viewmodulebycode(self, c_code):
		cursor = connection.cursor()
		query = "select m_id,m_name from schedule_chapters where c_code_id=%s"
		values = (c_code)
		cursor.execute(query,values)
		row = cursor.fetchall()
		return row

	def modulesession(self, module):    # for fetching count of sessions in a module 
		cursor = connection.cursor() 
		query = "select count(*) from schedule_modulepm where m_id_id=%s"
		values = (module)
		cursor.execute(query, values)
		result = cursor.fetchall()
		return result

	def sessiondisplay(self, mid):    # for fetching all sessions name amd values in a module   
		cursor = connection.cursor()
		query = "select Session_key,Session_value,m_id_id from schedule_modulepm where m_id_id=%s"
		values = (mid)
		cursor.execute(query, values)
		row = cursor.fetchall()
		return row

	def session_display(self):              #
		cursor = connection.cursor()
		query = "select Session_key,Session_value,m_id_id from schedule_modulepm"
		cursor.execute(query)
		row = cursor.fetchall()
		return row
