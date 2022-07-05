import requests
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.html"
data = {
    "tel":"13375849313",
}
rep = requests.get(url=url,params=data)
print(rep.text)
