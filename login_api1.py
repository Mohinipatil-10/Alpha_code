import os
import hashlib
import requests
import json
from datetime import timezone, datetime

api_account = "you"
username = "you"
api_secretkey = "77563"
password = "1Po=="

timeStamp = int(datetime.now(tz=timezone.utc).timestamp())

# ************ LOGIN DATA **********************
login_url = "https://api.alphaess.com/ras/v2/Login"

data_dict = {
    "Api_Account": api_account,
    "Password": password,
    "api_secretkey": api_secretkey,
    "TimeStamp": timeStamp,
    "Username": "yomauser"
}

headers = {'Content-Type': 'application/json'}

sign_str = f"api_account={api_account}password={password}secretkey={api_secretkey}timestamp={timeStamp}username={username}"
convert_sign = hashlib.md5(sign_str.encode()).hexdigest()
data_dict.update({"Sign": convert_sign})

login_json = requests.post(url=login_url, headers=headers, data=json.dumps(data_dict)).json()

# ********************* GET RUNNING DATA **********888**************
data_url = "https://api.alphaess.com/ras/v2/GetRunningData"

data_url_dic = {
    'api_account': api_account,
    'timestamp': timeStamp,
    'Sn': 'AE6010521060008',
    'Token': login_json.get('Token'),
}

sign_str = f"api_account={api_account}secretkey={api_secretkey}Sn=AE6010521060008timestamp={timeStamp}Token={login_json.get('Token')}"
convert_sign = hashlib.md5(sign_str.encode()).hexdigest()
data_url_dic.update({"sign": convert_sign})

data_req = requests.post(url=data_url, headers=headers, data=json.dumps(data_url_dic))

print("\t\t \n\n*****************GetRunningData*****************")
print("GetRunningData Response: ", data_req.json())
