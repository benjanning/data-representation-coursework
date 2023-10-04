import requests
url = "http://www.githup.com"
response = requests.get(url)
print("The status code for", url, "is", response.status_code)

import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)
print("The status code for", url, "is", response.status_code)

import requests
url = "https://api.twitter.com/oauth/request_token"
response = requests.post(url)
print("The status code for", url, "is", response.status_code)