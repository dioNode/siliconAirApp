import requests
import json
import csv
import tensorflow as tf
from sklearn.model_selection import train_test_split

class PriorityANN:
    """ANN to use for determining priority listing"""
    def __init__(self):
        print("Initialising...")
        self.desiredParameters = ['firstName', 'lastName', 'bookingClass', 'checkInStatus', 'willingEvictor']

    def train(self, api_url):
        azure_cv_endpoint = 'INSERT YOUR ENDPOINT URL HERE'
        azure_cv_key = 'INSERT YOUR KEY HERE'

        self.passengerList = self._getPassengerDetails("SQ890")

        #self.writeCSV("passengerDetails.csv")
        
#        mnist = tf.keras.datasets.mnist
#        print(mnist.load_data()[0][0].shape)
		
#        (x_train, y_train),(x_test, y_test) = mnist.load_data()
#        x_train, x_test = x_train / 255.0, x_test / 255.0
#		
#        model = tf.keras.models.Sequential([
#			  tf.keras.layers.Flatten(),
#			  tf.keras.layers.Dense(512, activation=tf.nn.relu),
#			  tf.keras.layers.Dropout(0.2),
#			  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
#			  ])
#        model.compile(optimizer='adam',
#		              loss='sparse_categorical_crossentropy',
#		              metrics=['accuracy'])
#		
#        model.fit(x_train, y_train, epochs=5)
#        model.evaluate(x_test, y_test)



    def requestData(self, url, payload):
        headers = {
            'content-type': "application/json",
            'apikey': "aghk73f4x5haxeby7z24d2rc",
            'cache-control': "no-cache",
            'postman-token': "53cd8502-4b4b-54d8-c2de-8636e549ba75"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        data = json.loads(response.text)
        return data

    def writeCSV(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = self.passengerList[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for passenger in self.passengerList:
                writer.writerow(passenger)

    def _getPassengerDetails(self, flightNo):
        flightschedule = self.requestData(
            "https://apigw.singaporeair.com/appchallenge/api/flight/passenger",
            "{ \"flightNo\": \""+flightNo+"\", \"flightDate\": \"2018-07-20\" }"
        )
        passengerList = flightschedule.get("response").get("passengerList")
        flightSummary = flightschedule.get("response").get("loadSummary")
        for passenger in passengerList:
            passenger["willingEvictor"] = True if passenger.get("bookingClass") == "Business" else False

        # Process data to get rid of unnecessary data
        passengerList = self._removeUnnecessaryFields(passengerList)

        return passengerList

    def _removeUnnecessaryFields(self, passengerList):
        for idx, passenger in enumerate(passengerList):
            tempPassenger = {}
            for param in self.desiredParameters:
                tempPassenger[param] = passenger.get(param)
            passengerList[idx] = tempPassenger
        return passengerList
    
        
        
        
        
        
        