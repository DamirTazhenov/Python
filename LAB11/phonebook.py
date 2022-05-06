from tkinter import EXCEPTION
import psycopg2, platform, os, csv
from config import host, user, password, db_name
def banner():
    if platform.system().lower()=="windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""
  
██████╗░██╗░░██╗░█████╗░███╗░░██╗███████╗██████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██████╔╝███████║██║░░██║██╔██╗██║█████╗░░██████╦╝██║░░██║██║░░██║█████═╝░
██╔═══╝░██╔══██║██║░░██║██║╚████║██╔══╝░░██╔══██╗██║░░██║██║░░██║██╔═██╗░
██║░░░░░██║░░██║╚█████╔╝██║░╚███║███████╗██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝
                                                                                                                                                                                                    
                        By : Tazhenov Damir 
""")   

def delete(PNumber):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
            f"delete from PhoneBook where PhoneNumber = '{PNumber}'"
            )
            print("[INFO] Deleting was complete siccesfully!")
        except Exception as ex:
            print(f"[INFO] Error, deleting is failed - {ex}")

def insert(FName, LName, PNumber):
    FName = FName.strip()
    LName = LName.strip()
    PNumber = PNumber.strip()
    #print(PNumber)
    with conn.cursor() as cursor:
        try:
            cursor.execute(
            f"insert into PhoneBook (FirstName, LastName, PhoneNumber) values ('{FName}','{LName}','{PNumber}')"
            )
            print ("[INFO] Insert was complete succesfully!")
        except Exception as ex:
            print(f"[INFO] Error, iserting is failed - {ex}")

try:
    banner()
    conn = psycopg2.connect(
        database=db_name, 
        user=user, 
        password=password, 
        host=host)    
    #cursor = conn.cursor()
    conn.autocommit = True #autocommit

    """with conn.cursor() as cursor:
        cursor.execute(
            "select version();"
        )
        print (f"Server version: {cursor.fetchone()}")
    """
    #create a table
    '''
    with conn.cursor() as cursor:
        cursor.execute(
            """ccreate table PhoneBook(
                FirstName varchar(50) not null,
                LastName varchar(50),
                PhoneNumber varchar(11) not null check(PhoneNumber!=''),
                PRIMARY KEY(PhoneNumber),
                unique(PhoneNumber)
                )            
                """
        )'''
    #insert into a table
    '''with conn.cursor() as cursor:
        cursor.execute(
            """
            insert into PhoneBook (FirstName, LastName, PhoneNumber) values ('Damir','Tazhenov','77056607999')
            """
        )
        print ("[INFO] Data was succesfully inserted")'''
    
    #import from CSV file
    """with open('LAB11\data.csv', "r", encoding="utf-8") as data:
        printed_data = csv.reader(data)
        for row in printed_data:
            #for item in row:
                #print (item, end=(' '))
            FName, LName, PNumber = row
            insert(FName,LName,PNumber)"""

    #print all data from table        
    with conn.cursor() as cursor:
        cursor.execute(
            """select * from PhoneBook"""
        )
        print(f"[INFO] {cursor.fetchall()}")

    #insert data from console
    '''inp = list(map(str,input("Введите данные через пробел!!").split()))
    try:
        insert(inp[0],inp[1],inp[2])
    except Exception as _ex:
        print(f"Deleting was failed, because {_ex}")'''
    
    #deleting data by phone number
    """inp = input("Input number which you want to delete!")
    delete(inp.strip())"""
    #Show by ordering
    with conn.cursor() as cursor:
        inp = input("Choose by what coloumn you want to order data: FirstName, LastName or PhineNumber?")
        inp2 = input("Chose ASC or DESC:")
        try:
            cursor.execute(
            f"""
            select * from PhoneBook
            order by {inp} {inp2} 
            """
            )
            print(f"[INFO] {cursor.fetchall()}")
        except Exception as ex:
            print(f"[INFO] Error, ordering is failed - {ex}")
    #update data by phone number
    with conn.cursor() as cursor:
        PhoneNum = input("Input phone number to change the owner!")
        Name = input("Input new First name and Last name").split(" ")
        try:
            cursor.execute(f"""
            update phonebook
            set firstname='{Name[0]}', lastname='{Name[1]}'
            where phonenumber = '{PhoneNum}'
        """)
            print("[INFO] Data was succefully updated")
        except Exception as ex:
            print(f"[INFO] Error, updating is failed - {ex}")
        
except Exception as _ex:
    print ("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if conn:
        #cursor.close()
        conn.close()
        print ("[INFO] Postgre connection closed")
