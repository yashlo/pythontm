import mysql.conector
print("====>>>>Stock Management System<<<<====");
def connect():
      connection = pymysql.connect(host="localhost",database='stock',user="root",password="");
      return connection;
def menu1():
    print("Enter your choice");
    print(" 1-show all stoke");
    print(" 2-Insert stoke");
    print(" 3- Selling stoke");
    print(" 4- search record");
def display(connection):
    cursor=connection.cursor();
    cursor.execute("select * from stock");
    row=cursor.fetchall();
    for x in row:
        print(x);
def insert(connection):
    cur = connection.cursor();
    prod=input("Enter the item model");
    cate=input("Enter the item categouri");
    qty=int(input("Enter the quantity"));
    price=int(input("Enter the price"));
    print ("writing to db");
    sql="INSERT INTO stock VALUES ('%s','%s','%d','%d')";
    args=(prod,cate,qty,price);
    res=cur.execute(sql%args);
    connection.commit();
def sell(connection):
    cur = connection.cursor();
    prod=input("Enter the model item number that user want to buy");
    qty1=int(input("Enter the quantity that user want to buy"));
    sql="update  stock set qty = qty - '%d'  where modelid='%s' and qty >= '%d'";
    args=(qty1,prod,qty1);
    cur.execute(sql%args);
    connection.commit();
def search(connection):
    prod=input("Enter the item model that you want to seaech");
    cursor=connection.cursor();
    sql="select * from stock where modelid='%s'";
    args=(prod);
    res=cursor.execute(sql%args);
    row=cursor.fetchall();
    for x in row:
        print(x);
    #display();
menu1();
connection = connect();
ch=int(input("Enter your choice"));
if(ch==1):
    display(connection);
elif(ch==2):
    insert(connection);
    display(connection);
elif(ch==3):
    sell(connection);
    display(connection);
elif(ch==4):
    search(connection);
