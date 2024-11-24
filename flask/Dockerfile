# בחר את התמונה הבסיסית של Python
FROM python:3.8-slim

# הגדר משתנה סביבה שיבטיח שפלט יועבר ישר (מונע caching)
ENV PYTHONUNBUFFERED=1

# צור ספריית עבודה לאפליקציה
WORKDIR /app

# התקן את כל התלויות
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# העתק את כל הקבצים מפרויקט Flask לתוך ספריית העבודה
COPY . /app/

# הגדר את הפורט שבו האפליקציה תאזין
EXPOSE 5000

# הגדר את פקודת ההרצה של האפליקציה
CMD ["flask", "run", "--host=0.0.0.0"]
