1. import required libraries
   * flask
   * flask-cors

```pip3 install Flask-Cors```

2. create **__init__.py** constructor which contains application factory. 
    * it tells python to treats **Meal-App** as a package
    

3.  * ``` export FLASK_APP=MealApp```
    * ``` export FLASK_ENV=development```
    *  ``` flask run```
    
4. Connect to database
    * touch db.py