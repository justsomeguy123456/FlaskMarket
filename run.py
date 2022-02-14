
from market import app

if __name__ =='__main__':

    app.run(debug=True)

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



#how to run
#export FLASK_APP = market.py
#export FLASK_DEBUG=1
