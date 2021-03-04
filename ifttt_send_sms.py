import requests
def sendtogo(msg):
    url = "https://maker.ifttt.com/trigger/deepsend/with/key/eYIgoy3oEmgNxEjKffu6DSBUZxVRdlhb0pHxje1wM3B"
    data = {'value1':msg}
    re = requests.post(url,data=data)