import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    for record in theJSON["features"]:
        if record["properties"]["mag"] >= 4.0:
            print("%2.1f" % record["properties"]["mag"], record["properties"]["place"])
    print("--------------------------------------\r\n")

def smain():
    webUrl = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
    print("Response code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Unable to parse data")


if __name__ == "__main__":
    smain()