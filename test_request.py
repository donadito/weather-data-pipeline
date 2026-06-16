import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current=temperature_2m"

response = requests.get(url, timeout=10)

print(response.status_code)
print(response.text[:200])