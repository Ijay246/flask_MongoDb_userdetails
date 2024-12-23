from pymongo import MongoClient
import pandas
from flask import Flask, render_template, request, Response, send_file
import csv
 
app = Flask(__name__)

# Establish a connection to MongoDB
client = MongoClient()

# Access a specific database
db = client.flask_userdetail_db

# Access a collection within the database
collection = db.userdetails

# Retrieve all documents from events collection
documents = collection.find()

#print all documents
for document in documents:
    print(document)

@app.route("/generate_csv")
def generate_csv():
    if len(document) == 0:
        return "No data to generate CSV."
 
    # Create a CSV string from the user data
    csv_data = "Name,Email\n"
    for document in documents:
        csv_data += f"{document['username']},{document['useremail']}\n"
 
    return render_template("index.html", csv_data=csv_data)
 
@app.route("/download_csv")
def download_csv():
    if len(document) == 0:
        return "No data to download."
 
    # Create a CSV string from the user data
    csv_data = "Name,Email\n"
    for document in documents:
        csv_data += f"{document['username']},{document['useremail']}\n"
 
    # Create a temporary CSV file and serve it for download
    with open("document.csv", "w") as csv_file:
        csv_file.write(csv_data)
 
    return send_file("document.csv", as_attachment=True, download_name="users.csv")
 
@app.route("/download_csv_direct")
def download_csv_direct():
    if len(document) == 0:
        return "No data to download."
 
    # Create a CSV string from the user data
    csv_data = "Name,Email\n"
    for document in documents:
        csv_data += f"{document['username']},{document['useremail']}\n"
 
    # Create a direct download response with the CSV data and appropriate headers
    response = Response(csv_data, content_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=users.csv"
 
    return response
 
if __name__ == "__main__":
    app.run(debug=True)


# print the total number of documents returned in a MongoDB collection
print ("total docs returned by find():", len( list(documents) ))



# create an empty DataFrame obj for storing Series objects
docs = pandas.DataFrame(columns=[])

# iterate over the list of MongoDB dict documents
for num, doc in enumerate( documents ):
    # convert ObjectId() to str
    doc["_id"] = str(doc["_id"])

    # get document _id from dict
    doc_id = doc["_id"]


    # create a Series obj from the MongoDB dict
    series_obj = pandas.Series( doc, name=doc_id )

# The inherent methods of Pandas Series and DataFrame objects allow streamlined exporting of different file 
# formats including to_html() to_json(), and to_csv().
    # append the MongoDB Series obj to the DataFrame obj
    docs = docs.append( series_obj )


# export MongoDB documents to CSV
csv_export = docs.to_csv(sep=",") # CSV delimited by commas
print ("\nCSV data:", csv_export)