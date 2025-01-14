import requests, json

response = requests.get("https://digitalprojects.wpi.art/gauguin/artworks")
response.raise_for_status()
print(type(response))
print(response.status_code == requests.codes.ok)
print(len(response.text))

with open('gauguin.json', 'w', encoding='utf-8') as f:
    f.write(response.text)