import requests

first_response = requests.get("https://playground.learnqa.ru/api/check_type", params={"name": "Karomaddin"})
second_response = requests.post("https://playground.learnqa.ru/api/check_type", data={"login": "sepluvetcon"})
print(f"1) {first_response.text}\n2) {second_response.text}")
