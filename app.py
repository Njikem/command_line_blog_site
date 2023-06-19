from flask import Flask,request
import dbhelpers
import json

app = Flask(__name__)

#function for client username and password
def get_client(username, password):
    conn = mariadb.connect(**dbcreds.conn_params)
    cursor = conn.cursor()

    cursor.execute('call get_client(?,?)', [username, password])
    results = cursor.fetchall()

    cursor.close()
    conn.close()


def client_id(client_id):

#Promp user to type it title and content
    user_title = input("Enter title")
    user_content = input("Enter content")

#insert the title and content into post
    cursor.execute('call insert_post(?,?,?)', [client_id, title, content])


#function to retrieve all post
def get_post(client_id, content, title):
    onn = mariadb.connect(**dbcreds.conn_params)
    cursor = conn.cursor()
    cursor.execute('call post(?,?,?)', [client_id, content, title])
    results = cursor.fetchall()

    cursor.close()
    conn.close()



    print("title")
    print("content")


#function to attempt user login
def log_user():

    username = input("enter username:")
    password = input("enter password:")


    





    











