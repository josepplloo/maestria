import requests
import time

file =open ("//Applications/Splunk/etc/apps/library/info/sms.ris","r")

for line in file:
    if line.find('DO  -') != -1:
        r=requests.get("https://api.elsevier.com/content/abstract/
                       citations?doi="+line[6:]+
                       "&apiKey=7f59af901d2d86f78a1fd60c1bf9426a
                       &httpAccept=application%2Fjson")
        data=r.json()
        print data
        time.sleep(1)
        


