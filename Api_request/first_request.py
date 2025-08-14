import json
from nturl2path import url2pathname
import requests as request

def main():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    data = request.get(url)
    response = data.json()
    print(response['data']['content'])

if __name__ == "__main__" :
    main()
