import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        data = self.get_response_body()
        return json.loads(data)
    
url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

web = GetRequester(url)
print(web.load_json())