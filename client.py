from pymongo import MongoClient

def get_database():
 
   CONNECTION_STRING = "mongodb://localhost:27017"
   client = MongoClient(CONNECTION_STRING)
   return client['annoythestreamer']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()

dbname = get_database()
col_facememe = dbname["facememe"]
col_normalmeme = dbname["normalmeme"]


def add_facememe(collection):
   col_facememe.insert_many([collection])

def top_facememe_id():
   max_id_dict = col_facememe.find_one(sort=[("_id", -1)])
   if max_id_dict is None:
      return 0
   else:
      return int(max_id_dict.get("_id"))
   
def first_facememe():
   first_meme = col_facememe.find_one({"done":"no"}, sort=[("_id", 1)])
   myquery = { "done" : "no" }
   newvalues = { "$set": { "done" : "yes" } }
   col_facememe.update_one(myquery, newvalues)
   return first_meme

def add_normalmeme(collection):
   col_normalmeme.insert_many([collection])

def top_normalmeme_id():
   max_id_dict = col_normalmeme.find_one(sort=[("_id", -1)])
   if max_id_dict is None:
      return 0
   else:
      return int(max_id_dict.get("_id"))
   
def first_normalmeme():
   first_meme = col_normalmeme.find_one({"done":"no"}, sort=[("_id", 1)])
   myquery = { "done" : "no" }
   newvalues = { "$set": { "done" : "yes" } }
   col_normalmeme.update_one(myquery, newvalues)
   return first_meme