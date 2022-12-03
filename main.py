import requests, os, sys
import argparse, configparser
import bit_ly


def read_token():
  return os.environ["BITLY_TOKEN"]


if __name__ == '__main__':
  try:
    token = read_token()
  except KeyError as e:
    print(f"Error: {e} \n no token in system enviroment")
    sys.exit()

  link_for_check = input("Enter your link: ")
  try:
    if bit_ly.is_bitlink(token, link_for_check):
      print(bit_ly.count_clicks(token, link_for_check))
    else:
      print(f"Битлинк {bit_ly.get_short_link(token,link_for_check)}")
  except requests.exceptions.HTTPError as e:
    print(f"Error:{e} \n your link <{link_for_check}> is incorrect \n")
    sys.exit()
