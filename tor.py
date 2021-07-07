from stem.control import Controller
from stem import Signal
import requests
def renew_ip():
    session = requests.session()
    string =session.get('https://httpbin.org/ip').text
    result1 =string[string.find('"',13)+1:string.find('"',15)]+ '\n'
    print(result1)
    session.proxies= {'http':'socks5://127.0.0.1:9050','https':'socks5://127.0.0.1:9050'}
    # signal TOR for a new connection 
    def renew_connection():
        with Controller.from_port(port = 9051) as controller:
            controller.authenticate(password = 'ghhmmss123*')
            controller.signal(Signal.NEWNYM)
            controller.close()
    renew_connection()
    string =session.get('https://httpbin.org/ip').text
    result =string[string.find('"',13)+1:string.find('"',15)] + '\n'
    print(result)
    if (result1 != result):
        print('====>  You IP is protected')
    else:
        print('====>  Your IP is not protected')
