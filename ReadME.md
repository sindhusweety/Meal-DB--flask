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
    * 
5. run MealApp as a package using flask
    
   * ``` export FLASK_APP=MealApp```
    * ``` export FLASK_ENV=development```
    *  ``` flask run```

6.  http://127.0.0.1:5000/app/search_name
   {"recipe": ["Arrabiata"]}
    
7. http://127.0.0.1:5000/app/ingredient_search
    {
   
    "ingredient":"olive oil, penne rigate"
}
