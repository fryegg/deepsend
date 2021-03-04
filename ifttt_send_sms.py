import requests
def sendtogo(msg, url):
    data = {'value1':msg}
    re = requests.post(url,data=data)
