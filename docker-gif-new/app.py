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

        # עדכון מונה המבקרים 
        print("Updating visitor count...")
        cursor.execute("UPDATE visitors SET visit_count = visit_count + 1 WHERE id = 1")
        cnx.commit()

        # שאילתת ה-SQL לשליפת המונה והתמונות 
        
        cursor.execute("SELECT visit_count FROM visitors WHERE id = 1")
        visit_count = cursor.fetchone()[0]
        print(f"Visitor count updated to: {visit_count}")
        
        query = "SELECT image_url FROM images"
        cursor.execute(query)
        result = cursor.fetchall()
        images = [row[0] for row in result]
        
        # סגירת ההתחברות למסד הנתונים 
        cursor.close()
        cnx.close()

        # בדיקה אם יש תמונות
        if not images:
            return jsonify({"message": "No images found in the database."}), 404

        # העברת ה-URLs לתבנית להציג אותם
        return render_template('index.html', images=images, visit_count=visit_count)

    except mysql.connector.Error as err:
        # טיפול בשגיאות של MySQL
        return jsonify({"error": f"Database error: {err}"}), 500

    except Exception as e:
        # טיפול בשגיאות כלליות
        return jsonify({"error": f"Unexpected error: {e}"}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
