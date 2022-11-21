import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vikram@2023",
  database="RainFall_Data_Analysis"
)

mycursor = mydb.cursor()

def feedback(username1, email1,phone_no1,Feedback1):
    sql = "INSERT INTO Feedback_Data (username,email,phone_no,Feedback) VALUES ('"+username1+"','"+email1+"','"+phone_no1+"','"+Feedback1+"');"
    mycursor.execute(sql)
    mydb.commit()
    return True

def registration(username,email,pwd):
    sql = "INSERT INTO User_Data(username,email,pwd) VALUES (%s, %s,%s)"
    val = (username,email,pwd)
    mycursor.execute(sql, val)
    mydb.commit()
    return True

def login(email1,pwd1):
    mycursor = mydb.cursor()
    print("SELECT email,pwd FROM User_Data WHERE email='"+email1+"' AND pwd='"+pwd1+"';")
    sql="SELECT email,pwd FROM User_Data WHERE email='"+email1+"' AND pwd='"+pwd1+"';"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if myresult!=[]:
        ls1=list(myresult[0])
        ls2=[email1,pwd1]
        return ls1==ls2
    else:
        return False

#registration("Vikram","vinothmass04072002@gmail.com","vikram@2023")
#print(login("vinothmass04072002@gmail.com","vikram@2023"))
#feedback("vinoth","vinothmass04072002@gmail.com","7339164558","Feedback")