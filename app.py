from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsdb"
mongo = PyMongo(app)


# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define the 'marsdb' database in Mongo
db = client.marsdb
# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    mars_info = mongo.db.info.find_one()
    return render_template("index.html", mars_info=mars_info)


#@app.route("/scrape")
#def scraper():
 #   listings = mongo.db.listings
  #  listings_data = scrape_craigslist.scrape()
   # listings.update({}, listings_data, upsert=True)
    #return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
