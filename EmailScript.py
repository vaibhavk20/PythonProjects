# please enable less secure app access for sending mail
import smtplib as s
ob = s.SMTP("smtp.gmail.com",587)
ob.starttls()
user_name = input("Enter the user name :")
user_pass = input("Enter the password :")
ob.login(user_name, user_pass)
subject = "Sending message using python"
body = "This message is sending through the python script \n" \
       "reply me \n" \
       "thank you..."
message = "Subject:{}\n\n{}".format(subject, body)
listOfAddress = ["vaibhav.2071998@gmail.com"]
ob.sendmail(user_name, listOfAddress , message )
ob.quit()
print("Send successfully...")