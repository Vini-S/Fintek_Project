from django.db import models
from django.utils.timezone import timezone	


# Create your models here.
class Users(models.Model):	
	Usertype = models.IntegerField(max_length=100)
	Email_id = models.EmailField(max_length=100, primary_key=True)
	Password = models.CharField(max_length=100)

class Course(models.Model):
	c_code = models.AutoField(primary_key=True,max_length=100)
	c_name = models.CharField(max_length=100) 
	

class Chapters(models.Model):
	m_id = models.AutoField(primary_key = True)
	m_name = models.CharField(max_length=100)
	c_code = models.ForeignKey('Course',default="", on_delete=models.CASCADE)
	
class CourseModule(models.Model):
	cm_id = models.AutoField(primary_key = True)
	c_code = models.ForeignKey('Course',default="", on_delete=models.CASCADE)
	m_id = models.ForeignKey('Chapters', default="", on_delete=models.CASCADE)


class Student_view(models.Model):
	s_id = models.AutoField(primary_key=True)
	s_f_name = models.CharField(max_length=100, default="")
	s_l_name = models.CharField(max_length=100, default="")
	s_Email_id = models.EmailField(max_length=100)
	Password = models.CharField(max_length=100, default="")
	c_code = models.ForeignKey('Course',default="", on_delete=models.CASCADE)
	

class Faculty_view(models.Model):
	f_id = models.AutoField(primary_key=True)
	f_f_name = models.CharField(max_length=100,  default="")
	f_l_name = models.CharField(max_length=100,  default="")
	f_Email_id = models.EmailField(max_length=100)
	Password = models.CharField(max_length=100, default="")
	f_phno = models.BigIntegerField()
	

class Student_leave(models.Model):
	l_id = models.AutoField(primary_key=True)
	s_email = models.CharField(max_length=100, default="")
	s_date = models.DateField(max_length=100)
	e_date = models.DateField(max_length=100)
	l_reason = models.CharField(max_length=500, default="")
	s_status = models.CharField('1' or '0', max_length=10, default="")


class Faculty_leave(models.Model):
	l_id = models.AutoField(primary_key=True)
	f_email = models.CharField(max_length=100,default="")
	s_date = models.DateField(max_length=100)
	e_date = models.DateField(max_length=100)
	l_reason = models.CharField(max_length=500)
	f_status = models.CharField('1' or '0', max_length=10, default="")

class Session(models.Model):
	se_id = models.AutoField(primary_key=True)
	se_date = models.DateField(max_length=100)
	se_detail = models.CharField(max_length=100)
	se_owner = models.CharField(max_length=100)
	c_code = models.ForeignKey('Course',default="", on_delete=models.CASCADE)
	m_id = models.ForeignKey('Chapters',default="", on_delete=models.CASCADE)
	f_id = models.ForeignKey('Faculty_view',default="", on_delete=models.CASCADE)

class Accepted_Faculty_leave(models.Model):
	a_id = models.AutoField(primary_key=True)
	a_email = models.CharField(max_length=100)
	a_s_date = models.DateField(max_length=100)
	a_e_date = models.DateField(max_length=100)
	a_l_reason = models.CharField(max_length = 500)

class Accepted_Student_leave(models.Model):
	a_sid = models.AutoField(primary_key=True)
	a_semail = models.CharField(max_length=100)
	a_ss_date = models.DateField(max_length=100)
	a_se_date = models.DateField(max_length=100)
	a_sl_reason = models.CharField(max_length = 500)

class ModulePM(models.Model):
	PM_id = models.AutoField(primary_key=True)
	Session_key = models.CharField(max_length=100)
	Session_value = models.CharField(max_length=100)
	m_id = models.ForeignKey('Chapters',default="", on_delete=models.CASCADE)


class Admin_view(models.Model):
	A_id = models.AutoField(primary_key=True)
	A_name = models.CharField(max_length=100)
	A_phno = models.BigIntegerField()
	A_Email_id = models.EmailField(max_length=100)
	

	