from flask import *

import requests, re
import pandas as pd
from MealApp.db import connect_db

meal_app = Blueprint('meal_app', __name__, url_prefix='/app')

client = connect_db()
OBJ = client.db.meal_table

@meal_app.post('/search_name')
def search():
    recipe_list = request.json['recipe']
    for i in recipe_list:
        URL ='https://www.themealdb.com/api/json/v1/1/search.php?s={}'.format(i)
        data = requests.get(URL).json()
        index_data = {'_id':OBJ.count_documents({}) + 1}
        index_data.update(data['meals'][0])
        insert_data = {}
        sub_list = []
        for k, v in index_data.items():
            if k.startswith('strIngredient'):
                sub_list.append(v)
            else:
                insert_data[k] =v
        insert_data["strIngredient"] = sub_list
        _id = OBJ.insert_one(insert_data)
    return {"status": "success", "message": "sucessfully updated", "result":list(OBJ.find())}


@meal_app.post('/ingredient_search')
def getmeal_ingredient():
    data = request.json['ingredient']
    output =[]
    for i in  list(OBJ.find()):
        for j in data:
            if j in i['strIngredient']:
                output.append(i)
    return {"status": "success", "message": "sucessfully updated", "result":output}


@meal_app.get('/test',)
def getMeal():
    df = pd.DataFrame(list(OBJ.find()))
    return render_template('index.html', tables=[re.sub(' mytable', '" id="example', df.to_html(classes='mytable'))],titles = ['Meal Recipe'])
