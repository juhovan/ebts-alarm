from urllib.request import HTTPCookieProcessor, build_opener, Request
from untangle import parse
from os import getenv

ebts = getenv('EBTS_IP')
user = getenv('EBTS_USER')
password = getenv('EBTS_PASSWORD')


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
             "opmode=login&passwd={password}&user={user}".format(password=password, user=user), True)
    print("Authenticated")


def set_message(slot, message):
    xml = _request("http://{ebts}/l4/kpdsetup".format(ebts=ebts),
                   "opmode=savewidget&id={slot}&type=6&msg={message}".format(slot=slot, message=message))
    return True


opener = build_opener(HTTPCookieProcessor())
