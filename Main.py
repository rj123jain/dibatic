from flask import Flask,render_template,request
import joblib 

# Intialize the app
app=Flask(__name__)
# load the model
model=joblib.load('Flask_Afsaan\model\dibatic_80.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/image')
def image():
    return render_template('image.html')

@app.route('/contect')
def contect():
    return'i found the contect'

@app.route('/about_us')
def about_us():
    return'about_us'

@app.route('/data',methods=['post'])
def data():
    firstname=request.form.get('first_name')
    lastname=request.form.get('last_name')
    phone_no=request.form.get('phone_no')
    email_no=request.form.get('email_no.')
    data={
        firstname:firstname,
        lastname:lastname,
        phone_no:phone_no,
        email_no:email_no,
    }
    print(firstname,lastname,phone_no,email_no)
    return render_template('test.html',data=data)

@app.route('/flight')
def flight():
    return render_template('flight.html')
    

@app.route('/flight',methods=['post'])
def flight_details():
    first_name=request.form.get('first_name')
    last_name=request.form.get('last_name')
    flight_no=request.form.get('flight_no')
    email_id=request.form.get('email_id')
    print(first_name,last_name,flight_no,email_id)
    return 'data_fetched'

@app.route('/predict')
def predict():
    return render_template('predict.html')



@app.route('/predict',methods=['post'])
def dibatic_details():
    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')
    
    result=model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if result[0]==1:
        data='person is diabatic'
    else:
        data='person is not diabatic'
    print(data)
    
    return render_template('body.html',data=data)



# When a user give the value we show proper result.
# jinja
# what ever project you are doing we need to creat requrent .txt
    
    

    
    
    
    


    
    

    



# Write on html pages
#1 all the html page on html folder
    
app.run(debug=True)

# http designed enable to communicate between client and server. Http work as request and response bewtwwn client and 
# server. A client (browser) send an http request to server then server return and response to client.
# the response contains status information about request and may also contain requested contain.
# methods get,put,push,delete # crud create read update delete basic opertaion on database.
# whten you create new row in database, read,update and delete
# Get -reteive put -update push  client to server side that is call post method
# client side to server that is called post
# click on profile fetech and display get
# the data alreay prensent and you update it put
# delete means to deactivate

# Flask_Afsaan - parent folder
# -model/(stores the save model)
#        - pkl(model file)
#- templet(stores the templet)
#        -home.html(to render the form)
# main.py (logic file)  # 

# - pip freeze > requirments.txt
# - pip install -r reqirments.txt

# Virtual envirnment

# you are doing prject 2020                      2022
# project#1
# numpy==0.4                                             # numpy==0.5

# pandas =0.8
# scikitlearn =2.4.2

# if version change as project not work . Different project have different version.
# We try to create conatiner type of stuff .Whatever project you do you should create virtual env
# 1 . to maintain the compatibility
#2 .unessary kind of library not there

# the method to create virtual envirnment

# -conda should be working 
# -conda env commands
# create a venv -----   conda create -n < env_name> python==<version>

# To check all the libraries present in particular env ---- pip list
#  to check what env is active - conda env list 

# What ever project do eacha dn every project in virtuacol environment