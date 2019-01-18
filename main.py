import requests
import json

def youdao_api():
    # 有道API: https://lbs.amap.com/api/webservice/guide/api/georegeo/
    # API example: https://restapi.amap.com/v3/geocode/geo?address=天安门&key=68a6e2e4232937916b4a414079a22239

    url = 'https://restapi.amap.com/v3/geocode/geo'
    address = '文慧园'
    key = '68a6e2e4232937916b4a414079a22239'
    payload = {'address': address,
               'key': key}
    r = requests.get(url, params=payload)
    r_json = r.json()


def qq_music() :
    # qq音乐API: https://y.qq.com/m/api/api.html#js-qm-media-playSonglist

    cmd = {'我喜欢': 'qqmusic://qq.com/ui/myTab?p=%7B%22tab%22%3A%22fav%22%7D', # p={"tab":"fav"} (url解码）
           '个性电台': 'qqmusic://qq.com/media/playRadio?p=%7B%22radioId%22%3A%2299%22%7D', # p={"radioId":"99"}
           '识别歌曲': 'qqmusic://qq.com/ui/recognize',
           'play':'qqmusic://qq.com/media/playSonglist?p=%7B%22song%22%3A%5B%7B%22songid%22%3A%22来自列表的项目%22%7D%5D%7D'} # p={"song":[{"songid":"来自列表的项目"}]}

def ts():

    api = 'http://music.163.com/api/playlist/detail?id=歌单ID&updateTime=-1'
    a = 'https://api.douban.com/v2/movie/search'
    a_param = {'q': '肖申克的救赎'}
    r = requests.get(a, a_param)
    r_json = r.json()
    return  r_json

def main():
    # youdao_api()
    de = ts()
    pr = json.dumps(de, sort_keys=True, indent=4, separators=(',', ':'))
    #print(pr)
    print('Hello API')

if __name__ == "__main__":
    main()
