   # this python file is to test all functionality isnised student class 
   # In future that calss will be used in real scenario like login / registeration/update details etc

from modules.student.Student import StudentClass


   # step  :  Student registration test

email = input("enter your email")
password = input("enter your password")

s1 =StudentClass()
s1.setUserNameAndPassword(email, password)

