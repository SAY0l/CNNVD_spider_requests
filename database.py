import pymysql
import datetime
from base import Task

Host = "127.0.0.1"
Port = 3306
Username = "root"
Password = "root"
Database = "sayo_test"
Tablename = "cnnvd_data"

'''
create table `cnnvd_data`(
    cnnvd_id varchar(255) primary KEY,
    vulName varchar(255) not null,
    cve_id varchar(255) default null,
    vulType varchar(255) default null,
    hazardLevel int default 3,
    vulDesc text default null,
    referUrl text default null,
    patch text default null,
    updateTime datetime
    
)DEFAULT CHARSET=utf8;
'''

def connect_database():
    conn = pymysql.connect(host=Host, port=Port,user=Username, password=Password, database=Database)
    cursor = conn.cursor()
    return conn,cursor

def insert_data(conn,cursor,values):
    sql = "INSERT INTO {} (cnnvd_id, vulName,cve_id,vulType,hazardLevel,vulDesc,referUrl,patch,updateTime)\
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(Tablename)
    cursor.execute(sql,values)

    conn.commit()

def close_database(conn,cursor):
    cursor.close()
    conn.close()

def edit_data(source_data):
    cnnvd_id = source_data['cnnvdCode']
    vulName = source_data['vulName']
    cve_id = source_data['cveCode']
    vulType = source_data['vulType']
    hazardLevel = source_data['hazardLevel']
    vulDesc = source_data['vulDesc']
    referUrl = source_data['referUrl']
    patch = source_data['patch']
    updateTime = datetime.datetime.strptime(source_data['updateTime'], "%Y-%m-%d %H:%M:%S")
    
    res=(cnnvd_id, vulName, cve_id, vulType,hazardLevel,vulDesc,referUrl,patch,updateTime)

    return res

def mysql_insert_data(source_data):
    conn = None
    try:
        conn,cursor = connect_database()
        values= edit_data(source_data)
        insert_data(conn,cursor,values)
        print(">>> save to database successfully!")
        #Task.count+=1
    except pymysql.IntegrityError as ie:
        Task.failure_flag = True
        print(">>> same primary key, exit...",ie) #简易去重处理
    except pymysql.Error as e:
        print(">>> database wrong! skip!",e)  
    finally:
        if conn:
            close_database(conn,cursor)