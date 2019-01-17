import requests
import json

# 有道API: https://lbs.amap.com/api/webservice/guide/api/georegeo/
# API example: https://restapi.amap.com/v3/geocode/geo?address=天安门&key=68a6e2e4232937916b4a414079a22239


#qq音乐API: https://y.qq.com/m/api/api.html#js-qm-media-playSonglist

def main():

    url = 'https://restapi.amap.com/v3/geocode/geo'
    address = '文慧园'
    key = '68a6e2e4232937916b4a414079a22239'
    payload = {'address':address,
               'key':key}

    r=requests.get(url, params = payload)
    json = r.json()

    print("Hello API")
