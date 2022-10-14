 http designed enable to communicate between client and server. Http work as request and response bewtwwn client and 
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

# What ever project do eacha dn every project in virtual environmentc

- to delete the env - conda env remove -n <env name> fist to do deactivate conda

Vertical and horizontal scaling

# Things required in to run project
            -coding file
            -req file

Cloud server- server is just laptop  but physcially it is virtually
deployemnt means anyone that you allow. We will try to put the file on that laptop which is not pysical present.
Heroku-paas server - plateform as service App and data
We gave app and data
We dont have control of os .    

How server will library to use 
For the we made confirguration file - to make heroku know the secific file we create We need to create procfile 
that is standard file of heroku  
We have to tell heroku which type of application it is either gaming or web application web:gunicorn 
Then write the file name and app like main:app

Few things to know
    ----procfile
    ----requirments.txt 



1.  Try to run main.py and execute it 
2. We have tarin and save the model. if you have save the model for eg scikitlearn 0.4 whatever scikitlearn pip list
and you should change in requirements.txt


