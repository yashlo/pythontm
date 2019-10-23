import pymysql.cursors
print("====>>>>Stock Management<<<<====");
def menu1():
    print("Enter your choice");
    print(" 1-show all stoke");
    print(" 2-Insert stoke");
    print(" 3- Selling stoke");
def display():
    connection = pymysql.connect(host="localhost",database='stock',user="root",password="yash");
    cursor=connection.cursor();
    cursor.execute("select * from stock");
    row=cursor.fetchall();
    for x in row:
        print(x);
def insert():
    connection = pymysql.connect(host="localhost",database='stock',user="root",password="yash");
    s1="LED125";
    s2="LED";
    s3=80;
    s4=25000;
    cur = connection.cursor()
    print ("writing to db");
    cur.execute("INSERT INTO stock VALUES ('LED125','LED',80,20000)")
    print ("wrote to db");
    connection.commit();
menu1();
cho=int(input("Enter your choice"));
if(cho==1):
    display();
if(cho==2):
    insert();
    display();



    
