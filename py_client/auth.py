import requests
from getpass import getpass

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/auth/"
pad= getpass("Enter your password: ")


get_res=requests.post(endpoint,json={"username":"dharanee","password":pad})

if get_res.status_code==200:
    token= get_res.json()['token']
    headers={'Authorization':f'Token {token}'}
    endpoint="http://localhost:8000/api/products/"
    get_res=requests.get(endpoint, headers=headers)


    print(get_res.text)
    print(get_res.history)
    print("response from API call : ",get_res.json())
    print(get_res.status_code)