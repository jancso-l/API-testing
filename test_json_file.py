import json
import jsonpath
import requests


def test_json():
    url = "https://dogapi.dog/api/v2/breeds?page[number]=1&page[size]=5"
    response = requests.get(url)
    json_response = json.loads(response.text)
    name = jsonpath.jsonpath(json_response, "data[0].attributes.name")
    assert name[0] == "Affenpinscher"