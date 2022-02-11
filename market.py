from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

#create db:
#open term and start python
#from market import db
#db.create_all()
#sqllite now created
#adding items
#from market import Item
#item1 = Item(name = "Iphone 10", price=500, barcode="1234567876923", description="desc")
#db.session.add(item1)
#db.session.commit()
#Item.query.all()


class Item(db.Model):
    id = db.Column(db.Integer(),primary_key=True, nullable=False,unique=True)
    name = db.Column(db.String(length=50),nullable=False,unique=True)
    price = db.Column(db.Integer(),nullable=False,unique=False)
    barcode = db.Column(db.String(length=15),nullable=False,unique=True)
    description = db.Column(db.String(length=1024),nullable=False,unique=False)

    def __repr__(self):
        return f'Item {self.name}'
#how to run
#export FLASK_APP = market.py
#export FLASK_DEBUG=1


@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html',items=items)
