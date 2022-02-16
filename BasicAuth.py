import requests
import base64

def get_response(url):
    user= input("Insert the username : ")
    passwd = input("Insert the password : ")
    basic = f"{user}:{passwd}"
    basic_bytes = basic.encode("ascii")
    base64_bytes = base64.b64encode(basic_bytes)
    base64_string = base64_bytes.decode("ascii")
    headers = {"Authorization": f"Basic {base64_string}"}
    r = requests.get(url, headers=headers)
    print(f"{r.status_code}\n")
    return r.status_code


url = input("Insert the web URL : ")

while True:
    if 200 == get_response(url):
        break
