# Write a program that prints the data for all trains in Ireland to the console.
# (You can modify this to store all the data in a CSV file
# Use the Irish rail API
# http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML
# to retrieve the data.
# Then as an exercise only store trains that have a train code that starts with D:
# For data sets of this size I would normally get all the data, and perform analysis
# (deletions) later.

import requests
import csv
from xml.dom.minidom import parseString

# Step 1: Get the data from the URL and check if it works
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

# Uncomment the following line to check if the XML is retrieved correctly 
print(doc.toprettyxml())
# Uncomment the following lines to store the XML in a file
with open("trainxml.xml", "w") as xmlfp:
     doc.writexml(xmlfp)

# Step 4: Print out each of the train codes
train_codes = doc.getElementsByTagName("TrainCode")
for train_code in train_codes:
    print(train_code.firstChild.data)

# Uncomment the following line to print out the latitudes
for listing in doc.getElementsByTagName("listing"):
     print(listing.getElementsByTagName("TrainLatitude")[0].firstChild.data)

# Step 6: Store train codes in a CSV file
dataList = []
with open("traincodes.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["TrainCode"])
    for train_code in train_codes:
        code = train_code.firstChild.data
        if code.startswith("D"):
            dataList.append(code)
            writer.writerow([code])

# Uncomment the following lines to store other properties in the CSV file
retrieveTags = ['TrainStatus', 'TrainLatitude', 'TrainLongitude', 'TrainDate', 'PublicMessage', 'Direction']
with open("traindata.csv", "w") as csvfile:
     writer = csv.writer(csvfile)
     writer.writerow(retrieveTags)
     for listing in doc.getElementsByTagName("listing"):
         dataList = []
         for retrieveTag in retrieveTags:
             dataNode = listing.getElementsByTagName(retrieveTag)[0].firstChild
             dataList.append(dataNode.data.strip())
         writer.writerow(dataList)
