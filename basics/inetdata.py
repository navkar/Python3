
import urllib.request

def smain():
    webUrl = urllib.request.urlopen("https://www.google.com")
    print("Response code: " + str(webUrl.getcode()))
    data = webUrl.read()
    print(data)


if __name__ == "__main__":
    smain()
