import os, os.path as op
import requests as rq
import json
import time, datetime as dt

class JsonFilter:
    # calls the api and puts the response in a local json file
    key = ""
    # url_address = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=GBP&api_key="
    url_address = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=10&api_key="
    key_file = "/Users/tillie/Documents/CryptoDev/APIKey.txt"
    file_output_dir = "/Users/tillie/Documents/CryptoDev/"

    # Any class will have an api key file, json file and a url
    def __init__(self,api_key_file,url,json_file,api_key):
        self.api_key_file = api_key_file
        self.url = url
        self.json_file = json_file
        self.api_key = api_key

    def extract_api_key(self):
        # Check if files exist
        if op.exists(self.api_key_file):
            # Opens files for read purpose and use read lines
            with open(self.api_key_file, 'r') as F:
                    txtfilecontent = F.readlines()
                    # Loops though the contents and returns the APIKEY
                    for Lines in txtfilecontent:
                        if "KEY:" in Lines:
                            stakey = Lines.index("{")
                            endkey = Lines.index("}") + 1
                            key = Lines[stakey:endkey]
                            self.key = key

        # prints can't find file
        else:
            print("This file doesn't exist")

    def call_api_get_json(self,name):
        # Api strings needed to get the JSON
        file_output_location = self.file_output_dir + name + ".json"

        if op.exists(file_output_location):
            os.remove(file_output_location)

        # Forms the URL with API key, gets response formated as JSON then saves file
        url = self.url_address + self.key
        rget = rq.get(url)
        rget_json = rget.json()

        with open(file_output_location, 'w') as outfile:
            json.dump(rget_json, outfile)

class JSONDataFillter:
    # Starts to do caluclations and formate the data
    json_file_read = "/Users/tillie/Documents/CryptoDev/HistoricalDump.json"

    def __init__(self, time, open_price, close_price, low, high):
        self.time = time
        self.open_price = open_price
        self.close_price = close_price
        self.low = low
        self.high = high

    def extract_time(self,file):
        with open(file, 'r') as jf:
            jsoncontent = json.load(jf)

            # Time is a int and in unix based time stamp, then formated as dd/mm/yyyy
            time = jsoncontent['Data'][0]['time']
            self.time = dt.datetime.utcfromtimestamp(time).strftime("%d/%m/%Y")

datam = JSONDataFillter("","","","","")

datam.extract_time(datam.json_file_read)

print(datam.time)