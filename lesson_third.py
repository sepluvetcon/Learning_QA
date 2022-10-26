import requests

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
second_response = response
print(f"1) {first_response.url}\n2) {second_response.url}")
