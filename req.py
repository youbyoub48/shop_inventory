import requests

r = requests.post("http://127.0.0.1:8000/api/", data={"nb": 15}, verify=False)
print(r.status_code)
print(r.content)