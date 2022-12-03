import requests, os, sys
import bit_ly


def read_token():
  return os.environ["BITLY_TOKEN"]


if __name__ == '__main__':
    try:
        token = read_token()

        link_for_check = input("Enter your link: ")

        if bit_ly.is_bitlink(token, link_for_check):
            print(bit_ly.count_clicks(token, link_for_check))
        else:
            print(f"Битлинк {bit_ly.get_short_link(token, link_for_check)}")
    except KeyError as e:
        print(f"Error: {e} \n no token in system environment")
        sys.exit()
    except requests.exceptions.HTTPError as e:
        print(f"Error:{e} \n your link <{link_for_check}> is incorrect \n")
        sys.exit()
