from schedule.models import Users
from django.db import connection

  

class Student:
	def studentview(self):
		cursor = connection.cursor()
		query = "select schedule_student_view.s_id, schedule_student_view.s_f_name, schedule_student_view.s_l_name, schedule_student_view.s_Email_id, schedule_student_view.c_code_id,schedule_course.c_name from schedule_course INNER JOIN schedule_student_view ON schedule_student_view.c_code_id=schedule_course.c_code"
		cursor.execute(query)
		row = cursor.fetchall()
		return row

	def studentsearch(self, name):
		cursor = connection.cursor()
		query = "select s_id, s_f_name, s_l_name, s_Email_id, c_code_id from schedule_student_view where s_f_name=%s"
		values = (name)
		cursor.execute(query, values)
		row = cursor.fetchall()
		return row

	def sviewleave(self):
		cursor = connection.cursor()
		query = "select s_email, s_date, e_date, l_reason, s_status from schedule_student_leave"
		cursor.execute(query)
		row = cursor.fetchall()
		print(row)
		return row

class Faculty:
	def facultyview(self):   
		cursor = connection.cursor()
		query = "select f_id, f_f_name, f_l_name, f_Email_id, f_phno from schedule_faculty_view "
		cursor.execute(query)
		row1 = cursor.fetchall()
		return row1

	def facultysearch(self, name):
		cursor = connection.cursor()
		query = "select f_id, f_f_name, f_l_name, f_Email_id, f_phno from schedule_faculty_view where f_f_name=%s"
		values = (name)
		cursor.execute(query, values)
		row = cursor.fetchall()
		return row

	def addleave(self, emailid, s_date, e_date, reason):     
		cursor = connection.cursor()
		query = "insert into schedule_faculty_leave(f_email, s_date, e_date, l_reason) values (%s,%s,%s,%s)"
		values = (emailid, s_date, e_date, reason) 
		cursor.execute(query,values)
		connection.commit()
		return 1

	def viewfleavebysession(self, emailid):       #(Auto fill form)
		cursor = connection.cursor()
		query = "select f_Email_id from schedule_faculty_view where f_Email_id=%s"
		values = (emailid)
		cursor.execute(query,values)
		row = cursor.fetchall()
		return row

	def viewleave(self):
		cursor = connection.cursor()
		query = "select f_email, s_date, e_date, l_reason, f_status from schedule_faculty_leave"
		cursor.execute(query)
		row = cursor.fetchall()
		return row

class Course:
	def courseview(self):
		cursor = connection.cursor()
		query = "select c_code,c_name from schedule_course"
		cursor.execute(query)
		row = cursor.fetchall()
		return row

	def coursesearch(self, name):
		cursor = connection.cursor()
		query = "select c_code,c_name from schedule_course where c_name=%s"
		values = (name)
		cursor.execute(query, values)
		row = cursor.fetchall()
		return row

class Module:
	def moduleview(self):
		cursor = connection.cursor()
		query = "select m_id,m_name from schedule_chapters"
		cursor.execute(query)
		row = cursor.fetchall()
		return row
	
