#importing the necessary libraries
from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle

#initiating the flask app
app = Flask(__name__)

#Route to display the home page
@app.route('/', methods = ['GET'])
@cross_origin()
def home_page():
    return render_template('index.html')

#Route to show the prediction in UI
@app.route('/predict', methods = ['GET','POST'])
@cross_origin()
def prediction():
    if request.method == 'POST':
        try:
            #Reading the inputs given by the user
            wocc2, wocc3, wocc4, wocc5, wocc6 = 0, 0, 0, 0, 0
            print("Started reading the input features")
            wife_Occ = request.form['Wife_Occupation']
            print("Reading the wife occupation")
            if wife_Occ == 'occ2':
                wocc2 = 1
            elif wife_Occ == 'occ3':
                wocc3 = 1
            elif wife_Occ == 'occ4':
                wocc4 = 1
            elif wife_Occ == 'occ5':
                wocc5 = 1
            elif wife_Occ == 'occ6':
                wocc6 = 1
            print("Completed reading the wife occupation",wocc2, wocc3, wocc4, wocc5, wocc6)
            hoc2, hoc3, hoc4, hoc5, hoc6 = 0, 0, 0, 0, 0
            hus_Occ = request.form['Hus_Occupation']
            if hus_Occ == 'hocc2':
                hoc2 = 1
            elif hus_Occ == 'hocc3':
                hoc3 = 1
            elif hus_Occ == 'hocc4':
                hoc4 = 1
            elif hus_Occ == 'hocc5':
                hoc5 = 1
            elif hus_Occ == 'hocc6':
                hoc6 = 1
            print("Completed reading the husband occupation",hoc2, hoc3, hoc4, hoc5, hoc6)
            rate_marriage = int(request.form['rate_marriage'])
            age = int(request.form['age'])
            yrs_married = int(request.form['yrs_married'])
            children = int(request.form['children'])
            religious = int(request.form['religious'])

            wife_edu = request.form['Wife_Education']
            if wife_edu == 'g_school':
                edu = 9
            elif wife_edu == 'h_school':
                edu = 12
            elif wife_edu == 's_college':
                edu = 14
            elif wife_edu == 'col_graduate':
                edu = 16
            elif wife_edu == 'some_col_graduate':
                edu = 17
            elif wife_edu == 'adv_degree':
                edu = 20
            #Loading the saved model
            filename = 'Log_model.pickle'
            print("filename:", filename)
            load_model = pickle.load(open(filename, 'rb'))
            print("Loaded the file")
            #prediction using the loaded model file
            predict = load_model.predict([[wocc2,wocc3,wocc4,wocc5,wocc6,hoc2,hoc3,hoc4,hoc5,hoc6,rate_marriage,age,yrs_married,children,religious,edu]])
            print("Prediction is ",predict)
            if predict == 1:
                msg = "Women has a affair"
            else:
                msg = "Women is not having an affair"
            print(msg)
            return render_template('results.html', message=msg)
        except Exception as e:
            print("Exception is ", e)
            return "Something is Wrong"
    else:
        return render_template('index.html')

if __name__ =="__main__":
    app.run(debug = True)



