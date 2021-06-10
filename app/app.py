from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Events.db'
db = SQLAlchemy(app)

class Events(db.Model):
    id = db.Column(db.Integer,db.Sequence('seq_reg_id', start=1, increment=1),primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    event_details = db.Column(db.String(500),nullable=False)
    organiser = db.Column(db.String(32), nullable=False)
    start_date = db.Column(db.String(12), nullable=False, default= str(datetime.utcnow()))
    date_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow())
    end_date = db.Column(db.String(12), nullable=False)
    Link = db.Column(db.String(100))
    contact1 = db.Column(db.String(10))
    contact2 = db.Column(db.String(10))

    def __repr__(self):
        data = self.organiser +" "+ str(self.id)
        return data

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
        # evtPstr = request.form['eventPoster']
        evtDtls = request.form['eventDetails']
        evntStrDt = request.form['startDate']
        evntEndDt = request.form['endDate']
        evtLnk = request.form['regLink']
        evtCtc =[request.form['contactOne'],request.form['contactTwo']] 
        
        new_event = Events(event_name=evtTitle,event_details=evtDtls,organiser=evtOrg,start_date=evntStrDt,end_date=evntEndDt,Link=evtLnk,contact1=evtCtc[0],contact2=evtCtc[1])

        db.session.add(new_event)
        db.session.commit()

        return redirect('/home')
    else:
        pass
        
    return render_template('form.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)