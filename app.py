from flask import Flask 
from flask import render_template
from flask import request, redirect

from twilio.rest import TwilioRestClient 

app = Flask(__name__) # Creating the Flask app
client = TwilioRestClient ('AC4f664d9c5755a9d50c0faab37cf119f4', '28972db267c44d9bbd6a0171e67aad5d') # Paste in your AccountSID and AuthToken here
twilio_number = "+14152148623" # Replace with your Twilio number

@app.route("/") # When you go to top page of app, this is what it will execute
def main():
    return render_template('form.html')
  
@app.route("/submit-form/", methods = ['POST']) 
def submit_number():
    number = request.form['number']
    formatted_number = "+1" + number # Switch to your country code of choice
    client.messages.create(to=formatted_number, from_ = twilio_number, 
    	body = "A C error walks into a bar. The bartender says, \"We don't serve bugs here.\" The C error, \"Segfault.\"") # Replace body with your message of choice
    return redirect('/messages/')
  
@app.route("/messages/")
def list_messages():
    messages = client.messages.list(to=twilio_number)
    return render_template('messages.html', messages = messages)
    
    
if __name__ == '__main__': # If we're executing this app from the command line
    app.run("0.0.0.0", port = 3000, debug = True)
