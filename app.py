from flask import Flask,render_template,url_for,request,redirect
from pymongo import MongoClient

app= Flask(__name__)
client = MongoClient('localhost',27017)
#create db
db = client.flask_userdetail_db
#creates table
user_detail = db.user_detail
@app.route('/index',methods=['GET','POST'])

def index():
    data = request.form 
    data1 = request.form.get('checkbox') 
    if request.method == 'POST':
        username = data['username']
        useremail = data['useremail']
        age = data['age']
        gender = 'Male' if data['genderMale'] else 'Female'
        totalincome = data['totalincome']
        checkU= data1
        utilities=data['utilities']
        checkE= data1
        entertainment= data['entertainment']
        checkS= data1
        schoolfees=data['schoolfees']
        checkSh= data1
        shopping = data['shopping']
        checkH= data1
        healthcare = data['healthcare']
        user_detail.insert_one({'username':username,
        'useremail': useremail,
        'age': age,
        'gender' :gender,
        'totalincome' : totalincome,
        'checkU':data1,
        'utitlities':utilities,
        'checkE':data1,
        'entertainment':entertainment,
        'checkS':data1, 
        'schoolfees':schoolfees,
        'checkSh':data1,
        'shopping' :shopping,
        'checkH':data1,
        'healthcare':healthcare})
  
        return redirect(url_for('index'))
    all_details =user_detail.find()
    return render_template('index.html',user_detail=all_details)





if __name__ =="__main__":
    app.run(debug=True)
