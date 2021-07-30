from flask import Flask,request,render_template
from tensorflow.keras.models import load_model
import numpy as np
import joblib


model = load_model('airline4-copy1.h5')
sc = joblib.load("scalar")

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ind')
def index2():
    return render_template('index2.html')


@app.route('/login', methods =['POST']) 
def login():
    year = request.form['year']
    month = request.form['month']
    passengers = request.form['passengers']
   
    test = [year,month,passengers]
    print(test)
    test = np.array(test)
    test = test.reshape(-1,1)
    test = sc.transform(test)
    test = np.reshape(test, (1,1,3))
    print(test.shape)
    
    f = model.predict((test))
    print(f)
    f = sc.inverse_transform(f)
    print(f)
  
        
    return render_template('output.html' ,year = year,month=month, passengers= passengers,showcase = str(round(f[0][0])))

if __name__ == '__main__':
    app.run(debug=True)





