# a new project
from flask import Flask, jsonify, render_template_string, redirect, url_for
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/new")
def new_change():
    return "<p>New change to Docker!</p>"

@app.route("/greet/<name>")
def greet_fun(name):
    return f"<p>Hello, {name}!</p>"

@app.route("/about")
def about():
    return "<p>This is my first project in flask!</p>"

@app.route('/get_data')
def get_data():
    # פנייה ל-API לקבלת נתוני שערי חליפין
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
    except Exception as e:
        return f"<p>קרתה שגיאה בקבלת נתונים: {e}</p>"

    # תבנית HTML להצגת הנתונים
    html = """
    <!DOCTYPE html>
    <html lang="he" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>שווי המטבעות</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(to bottom, #e0f7fa, #ffffff);
                margin: 0;
                padding: 0;
                text-align: center;
                color: #333;
            }
            h1 {
                color: #4CAF50;
                margin-top: 20px;
            }
            p {
                font-size: 18px;
                margin: 10px 0;
            }
            table {
                width: 80%;
                margin: 20px auto;
                border-collapse: collapse;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }
            table th, table td {
                padding: 10px;
                border: 1px solid #ddd;
                text-align: center;
            }
            table th {
                background-color: #4CAF50;
                color: white;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            tr:hover {
                background-color: #f1f1f1;
            }
        </style>
    </head>
    <body>
        <h1>שווי המטבעות ביחס לדולר</h1>
        <p><strong>תאריך:</strong> {{ date }}</p>
        <table>
            <tr>
                <th>מטבע</th>
                <th>שער חליפין</th>
            </tr>
            {% for currency, rate in rates.items() %}
            <tr>
                <td>{{ currency }}</td>
                <td>{{ rate }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """

    # החזרת התבנית עם הנתונים מה-API
    return render_template_string(html, date=data['date'], rates=data['rates'])

#if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
