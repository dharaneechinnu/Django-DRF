import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/"

get_res=requests.get(endpoint)
print(get_res.text)
print(get_res.history)
print("response from API call : ",get_res.json())
print(get_res.status_code)