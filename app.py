from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender = int(request.form['Gender'])
        Age=int(request.form['Age'])
        Weight=float(request.form['Weight'])
        Duration=float(request.form['Duration'])
        Body_Temp=request.form['Body_Temp']
        if(Body_Temp=='1'):
                Body_Temp = 41
        elif(Body_Temp=='2'):
                Body_Temp = 40.4      
        else:
            Body_Temp = 39.5
        prediction=model.predict([[Gender,Age,Weight,Duration,Body_Temp]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you have not burn't calories")
        else:
            return render_template('index.html',prediction_text="Calories Burnt : {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
    
