import requests
import json
import csv
import urllib
import pandas as pd

class PriorityANN:
    """ANN to use for determining priority listing"""
    def __init__(self):
        print("Initialising...")
        self.desiredParameters = ['firstName', 'lastName', 'bookingClass', 'email', 'checkInStatus', 'willingEvictor']
        self.passengerList = []
        self.flightList = ["SQ494", "SQ890"]

    def setFlight(self, flightNo):
        self.passengerList = self._getPassengerDetails(flightNo)
        #self.writeCSV("passengerDetails.csv")

    def buildCSV(self):
        # do nothing
        print("nothing")


    def evaluate(self, flightNo):
        passengerList = self._getPassengerDetails(flightNo)
        values = []
        columnNames = ["firstName", "lastName", "bookingClass", "KFTier", "email", "checkInStatus",
                                        "willingEvictor"]
        for passenger in passengerList:
            passengerInfo = []
            for columnName in columnNames:
                passengerInfo.append(passenger.get(columnName))
            values.append(passengerInfo)


        data = {

            "Inputs": {
                "input1":
                    {
                        "ColumnNames": columnNames,
                        "Values": values
                    }, },
            "GlobalParameters": {
            }
        }

        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/8334317b4f7a4e8ba1058977846f6f84/services/1594f6de0f8c42abbd0ce53bcf9a712f/execute?api-version=2.0&details=true'
        api_key = '42zafbAj/h0j6xwLp6hiEgllwnm4S4LtNKwI9FmyQoHTN0pUEKQQOYeAkb+1N2c+i65bLR6con1LjtYUdDNzBQ=='
        headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

        req = urllib.request.Request(url, body, headers)

        try:
            response = urllib.request.urlopen(req)

            result = json.loads(response.read().decode('utf-8'))
            scoreList = result["Results"]["output1"]["value"]["Values"]
            passengerNames = []
            scoreListParsed = []
            for passengerIdx, score in enumerate(scoreList):
                firstName = passengerList[passengerIdx].get('firstName')
                lastName = passengerList[passengerIdx].get('lastName')
                passengerNames.append(firstName + " " + lastName)
                scoreListParsed.append(float(score[0]))

            score_df = pd.DataFrame({
                'score' : scoreListParsed,
                'passengerName' : passengerNames
            })
            sorted_score_df = score_df.sort_values(by=['score'], ascending=False)
            print(sorted_score_df)


        except urllib.error.HTTPError:
            print("The request failed with status code: ")


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
            passenger["willingEvictor"] = False if passenger.get("bookingClass") == "Business" else True

        return passengerList

