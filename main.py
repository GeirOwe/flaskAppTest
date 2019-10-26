#source tutorial found here
#https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/

#Here we are importing the Flask module and creating a Flask web server from the Flask module.
#render_template lets us use html to format our output
from flask import Flask, render_template


# __name__ means this current file. In this case, it will be main.py.
# This current file will represent my web application.
app = Flask(__name__)

#the starting page: ./
@app.route("/")
def home():
    return render_template("home.html")

#The Flask Framework looks for HTML files in a folder called templates.
#You need to create a templates folder in the same directory where you have your main.py file
#and put all your HTML files in there.

#another page page: ./about
@app.route("/about")
def about():
    return render_template("about.html")

#Having debug=True allows possible Python errors to appear on the web page. This will help us trace the errors.   
if __name__ == "__main__":
    app.run(debug=True)




#to run it:
# In your Terminal or Command Prompt go to the folder that contains your main.py.
# Then do py main.py or python main.py. In your terminal or command prompt you should see this output.
#
# Running on http://127.0.0.1:5000/

#To deploy our web application to azure:
#https://medium.com/@nikovrdoljak/deploy-your-flask-app-on-azure-in-3-easy-steps-b2fe388a589e


