import requests, os, sys
import argparse, configparser
import bit_ly

def get_args():
  parser = argparse.ArgumentParser(description="Bitly API interface")
  parser.add_argument('-config',
                      '--config',
                      default="config.ini",
                      help="конфигурационный файл")
  return parser.parse_args()


def get_config_info(filename):
  config = configparser.ConfigParser()
  config.read(filename)
  try:
    config['bitly']
  except:
    print('Error: config file does not match pattern')
    sys.exit()
  return config


def read_token():
  if os.getenv("BITLY_TOKEN") is not None:
    return os.getenv("BITLY_TOKEN")
  config = get_config_info(get_args().config)
  token = config['bitly']['token']
  if token and not token.isspace():
    return config['bitly']['token']
  print("Error: token is empty")
  sys.exit()


if __name__ == '__main__':
  token = read_token()

  link_for_check = input("Enter your link: ")
  try:
    bit_ly.get_information(token,link_for_check)
    print(bit_ly.count_clicks(token,link_for_check))
  except:
    try:
      print(f"Битлинк {bit_ly.get_short_link(token,link_for_check)}")
    except:
      print(f"Error: your link <{link_for_check}> is incorrect ")
      sys.exit()
