




from flask import Flask, render_template, redirect
from pymongo import MongoClient
import scrape_mars





#connect to the database
conn = 'mongodb://localhost:27017'
client = MongoClient(conn)
db = client.mars_db
collection = db.mars





app = Flask(__name__)





@app.route('/')
def  home():
    mars = collection.find_one()
    return render_template('index.html', mars=mars)

@app.route('/scrape')
def scrape():
    scrape_mars.scrape()
    return redirect('/', code = 302)

if __name__ == "__main__":
      app.run(debug=True)

