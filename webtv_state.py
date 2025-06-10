# webtv_state.py
ip = None
port = None
ssid = None

def set_connection_info(new_ip, new_port, new_ssid=None):
    global ip, port, ssid
    ip = new_ip
    port = new_port
    if new_ssid is not None:
        ssid = new_ssid

def getIp():
    return ip

def getPort():
    return port

def getSsid():
    return ssid
