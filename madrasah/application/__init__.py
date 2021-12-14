from flask import Flask
import pymongo


app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://test:password1234@cluster0.hx8ib.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# Connecting to local mongodb database
# client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
# Creating a database



client = pymongo.MongoClient("mongodb+srv://test:password1234@cluster0.hx8ib.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.db

# madrasah = client['madrasah']
# Creating a collection in the database already created
# studentCollection = madrasah['students']
# set up mongodb


from application import routes