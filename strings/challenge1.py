import requests
url = "https://opentdb.com/api_config.php"
response = requests.get(NQ = NUMBER)
x = response.json()
print(x)
