from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False,primary_key=True)
    event_details = db.Column(db.String(500), nullable=False,nullable=False)
    organiser = db.Column(db.String(32), nullable=False)
    Start_date = db.Column(db.DateTime, nullable=False, default= datetime.utcnow)
    End_date = db.Column(db.DateTime, nullable=False)
    Link = db.Column(db.String(100))
    contact1 = db.Column(db.String(10))
    contact2 = db.Column(db.String(10))

    def __repr__():
        return self.organiser +" "+ str(self.id)

images = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html',images=images)

@app.route('/forms', methods=['GET','POST'])
def form():
    if request.method=='POST':
        evtTitle= request.form['eventName']
        evtOrg = request.form['organizer']
        evtPstr = request.form['eventPoster']
        evtDtls = request.form['eventDetails']
        evntStrDt = request.form['startDate']
        evntEndDt = request.form['endDate']
        evtLnk = request.form['regLink']
        evtCtc =[request.form['contactOne'],request.form['contactTwo']] 
        
    return render_template('form.html')
 
if __name__ == "__main__":
    app.run(debug=True)