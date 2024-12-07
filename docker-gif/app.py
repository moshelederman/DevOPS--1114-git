from flask import Flask, render_template
import os
import mysql.connector
import random

app = Flask(__name__)

# הגדרות מסד הנתונים 
db_config = { 
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', 'example'),
    'database': os.getenv('MYSQL_DB', 'testdb')
}


@app.route('/')
def display_images(): # התחברות למסד הנתונים 
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # שאילתת ה-SQL לשליפת התמונות 
    query = "SELECT url FROM images"
    cursor.execute(query)

    # קבלת רשימת ה-URLs של התמונות 
    images = cursor.fetchall() 
    # סגירת ההתחברות למסד הנתונים 
    cursor.close() 
    cnx.close() 
    # העברת ה-URLs לתבנית להציג אותם 
    return render_template('index.html', images=images)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
