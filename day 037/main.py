import requests
from datetime import datetime

USERNAME = "vandit"
TOKEN =  "abcdefghijklmnopqrstuvwxyz123456789"

pixel_endpoint = "https://pixe.la/v1/users"

post_params = {
    "token": "abcdefghijklmnopqrstuvwxyz123456789",
    "username": "vandit",
    "agreeTermsOfService":"yes",
    'notMinor':"yes"
}

response = requests.post(url=pixel_endpoint, json=post_params)
print(response.text)

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

graph_headers={
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
print(response.text)
today = datetime.now()
graph_write_endpoint = f"{graph_endpoint}/{graph_params['id']}"
graph_write_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.24"
}

response = requests.post(url=graph_write_endpoint, json=graph_write_params, headers=graph_headers)
print(response.text)

pixel_update_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/graph1/20220314"
print(pixel_update_endpoint)
pixel_update_params = {
    "quantity": "15.14"
}

response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=graph_headers)
print("done")
print(response.status_code)

delete_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/graph1/20220314"
response = requests.delete(url=delete_endpoint, headers=graph_headers)
print(response.text)
