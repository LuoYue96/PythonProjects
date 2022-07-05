#import pytest
import requests
url = "https://api.weixin.qq.com/cgi-bin/token"
data = {
    "grant_type":"client_credential",
    "appid":"wx6b11b3efd1cdc290",
    "secret":"106a9c6157c4db5f6029918738f9529d"
}
rep = requests.get(url=url,params=data)
print(rep.json())