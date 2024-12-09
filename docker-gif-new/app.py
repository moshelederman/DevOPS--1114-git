from flask import Flask, render_template, jsonify
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# הגדרות מסד הנתונים
db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DB')
}

@app.route('/')
def display_images():
    try:
        # התחברות למסד הנתונים
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        # שאילתת ה-SQL לשליפת התמונות
        query = "SELECT image_url FROM images"  # ודא שהעמודה נקראת image_url ולא url
        cursor.execute(query)

        # קבלת רשימת ה-URLs של התמונות
        result = cursor.fetchall()
        images = [row[0] for row in result]  # עיבוד התוצאות לרשימה פשוטה

        # סגירת ההתחברות למסד הנתונים
        cursor.close()
        cnx.close()

        # בדיקה אם יש תמונות
        if not images:
            return jsonify({"message": "No images found in the database."}), 404

        # העברת ה-URLs לתבנית להציג אותם
        return render_template('index.html', images=images)

    except mysql.connector.Error as err:
        # טיפול בשגיאות של MySQL
        return jsonify({"error": f"Database error: {err}"}), 500

    except Exception as e:
        # טיפול בשגיאות כלליות
        return jsonify({"error": f"Unexpected error: {e}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
