from urllib.request import HTTPCookieProcessor, build_opener, Request
from untangle import parse
from os import getenv

ebts = getenv('EBTS_IP')
pin = getenv('EBTS_PIN')


def _request(url, data=None, auth=False):
    while True:
        if data:
            try:
                data = data.encode()
            except AttributeError:
                data = data

        req = Request(url, data=data)

        with opener.open(req, timeout=10) as response:
            body = response.read()
            body = body.decode()
            print(body)
            xml = parse(body)
            print(xml)

            if xml.response["code"] == "100":
                if auth:
                    print("Authentication failed!")
                    exit()

                do_auth()
                continue

            return xml


def do_auth():
    print("Authenticating...")
    _request("http://{ebts}/l4/auth".format(ebts=ebts),
             "opmode=elevate&pin={pin}".format(pin=pin), True)
    print("Authenticated")


def get_state():
    xml = _request(
        "http://{ebts}/l4/securitystate?opmode=widget&rl=5".format(ebts=ebts))
    state = int(xml.response.securitystate["id"])
    if state >= 1 and state <= 3:
        return state
    else:
        print("Invalid state!")


def set_state(state):
    xml = _request("http://{ebts}/l4/securitystate".format(ebts=ebts),
                   "pin={pin}&sid={state}&opmode=change".format(pin=pin, state=state))
    new_state = get_state()
    if state == new_state:
        return True
    else:
        print("Failed to change state")


opener = build_opener(HTTPCookieProcessor())
