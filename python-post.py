import requests

url = "http://localhost:5000/miPost"
locationNames = "Test-py"
myobj = {"locationName": locationNames}

x = requests.post(url, data = myobj)

print(x.text)
