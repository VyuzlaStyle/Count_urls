# Файл с функциями от API BIT.LY
import requests



def get_user(token):
  headers={
    "Authorization": f"Bearer {token}"
  }
  response = requests.get("https://api-ssl.bitly.com/v4/user", headers=headers)
  response.raise_for_status()
  return response.text


def get_short_link(token, url):
  headers={
    "Authorization": f"Bearer {token}"
  }
  payload = {
    "long_url" : f"{url}"
  }
  response = requests.post("https://api-ssl.bitly.com/v4/shorten",
                           headers=headers,
                          json = payload)
  response.raise_for_status()
  return response.json()['link']


def count_clicks(token,url):
  headers={
    "Authorization": f"Bearer {token}"
  }
  payload = {
    "unit" : "day",
    "units" : -1
  }
  response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary",
                           headers=headers,
                          params = payload
                          )
  response.raise_for_status()
  return response.json()['total_clicks']


def get_information(token,url):
  headers={
    "Authorization": f"Bearer {token}"
  }
  response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{url}",
                           headers=headers
                          )
  response.raise_for_status()
  return response.json()