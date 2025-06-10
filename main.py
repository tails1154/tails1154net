import requests
import time
import pygame
import socket
import json
import re
from weasyprint import HTML






def matchPortWtvHeadWaiter(line):
    print(line)
    pattern = r'^wtv-service: name=wtv-head-waiter.*?host=([^\s]+)\s+port=(\d+)'

    match = re.search(pattern, line, re.MULTILINE)
    if match:
        host = match.group(1)
        port = match.group(2)
        print(f"Port: {port}")
        return port
    else:
        print("Match not found")
def matchHostWtvHeadWaiter(line):
    pattern = r'^wtv-service: name=wtv-head-waiter.*?host=([^\s]+)\s+port=(\d+)'

    match = re.search(pattern, line, re.MULTILINE)
    if match:
        host = match.group(1)
        port = match.group(2)
        print(f"Host: {host}")
        return host
    else:
        print("Match not found")
      
def matchWtvChallenge(line):
    pattern = r'^wtv-challenge:\s*(.*)'
    
    
    match = re.search(pattern, line, re.MULTILINE)
    
    if match:
        challenge = match.group(1)
        print(f"Challenge: {challenge}")
        return challenge
    else:
        print("Match not found")
def matchPortWtvService(line, service):
    print(line)
    pattern = fr'^wtv-service: name={service}.*?host=([^\s]+)\s+port=(\d+)'

    match = re.search(pattern, line, re.MULTILINE)
    if match:
        host = match.group(1)
        port = match.group(2)
        print(f"Port: {port}")
        return port
    else:
        print("Match not found")
        
        
def matchWtvVisit(line):
     pattern = r'^wtv-visit:\s*(.*)'


    match = re.search(pattern, line, re.MULTILINE)

    if match:
        challenge = match.group(1)
        print(f"wtv-visit: {challenge}")
        return challenge
    else:
        print("Match not found")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
class WebTVRequests:
    def __init__(self, host, port):
        print("[DEBUG] Creating socket")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[DEBUG] Connecting socket")
        s.connect((host, port))
        print(f"[DEBUG] Connected to {host}:{port}")
        self.s = s
    def getNoResponse(self, url, headers=""):
        print("[DEBUG] Sending request")
        request = f"GET {url} HTTP/1.1\n{headers}\n\n"
        print(f"[DEBUG] Sending {request}")
        self.s.send(request.encode('utf-8'))
        print("[DEBUG] Sent request")
        
    def getResponse(self, url, headers=""):
        request = f"GET {url} HTTP/1.1\r\n{headers}\r\n\r\n"
        screen.fill('black')
        if connecting:
            roadImage = pygame.image.load("assets/road.gif").convert_alpha()
            screen.blit(roadImage, (0, 0))
        text_surface = font.render(url, True, (255, 255, 255))
        screen.blit(text_surface, (50, 50))
        pygame.display.flip()
        for _ in range(100):
            pygame.display.flip()

        print(f"[DEBUG] Sending:\n{request}")
        self.s.send(request.encode('utf-8'))

        response = b""
        self.s.settimeout(2)  # so it doesn't hang forever
        try:
            while True:
                chunk = self.s.recv(4096)
                if not chunk:
                    break
                response += chunk
        except socket.timeout:
            pass  # probably done receiving

        print("[DEBUG] Full response received")
        print(response.decode('utf-8', errors='replace'))
        return response

    def disconnect(self):
        self.s.close()











































def getText_ProxySocket(proxy_host, proxy_port, target_url, headers=""):
    print("[DEBUG] Creating socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[DEBUG] Connecting socket")
    s.connect((proxy_host, proxy_port))
    print(f"[DEBUG] Connected to {proxy_host}:{proxy_port}")
    print("[DEBUG] Sending request")
    request = f"GET {target_url}\nHost: {target_url}\n{headers}\n\n"
    print(f"[DEBUG] Sending {request} Encoded with utf-8")
    s.send(request.encode('utf-8'))
    print("[DEBUG] Sent data")
    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data
    s.close()
    print("[DEBUG] Got response")
    return response.decode('utf-8', errors='replace')

def getBytes_LimitedSpeed(url):
    req = requests.request("GET", url, stream=True)
    fulldata = bytearray()
    for data in req.iter_content(chunk_size=1024):
        time.sleep(0.0625)
        fulldata += data
    return bytes(fulldata)
def getText_LimitedSpeed(url):
    req = requests.get(url, stream=True)
    fulldata = ""
    for chunk in req.iter_content(chunk_size=1024):
        time.sleep(0.0625)
        if chunk:
            fulldata += chunk.decode('utf-8')  # Decode bytes to string
    return fulldata






def main():
    global ip
    global port
    global ssid
    global font
    global screen
    print("Starting WebTV Client")
    print("Reading config.json")
    with open("config.json", 'r') as file:
        data = json.load(file)

    ip = data['ip']
    port = data['port']
    ssid = data['ssid']
    print(f"Read config.json! ip: {ip} port: {port}")
    print("Starting pygame")
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.SysFont(None, 48)

    pygame.mixer.init()
    pygame.mixer.music.load("assets/connect.mp3", namehint="mp3")
    
    
    global splash
    global connecting
    splash = False
    connecting = True

    roadImage = pygame.image.load("assets/road.gif").convert_alpha()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill("black")


        # Put stuff below here

        if connecting:
            screen.blit(roadImage, (0, 0))
            pygame.display.flip()
            text_surface = font.render("Enter server ip and port", True, (0, 0, 0))
            screen.blit(text_surface, (0, 0))
            pygame.display.flip()
            pygame.time.wait(1000)
            pygame.mixer.music.play()
            screen.fill("black")
            screen.blit(roadImage, (0, 0))
            pygame.display.flip()


            # When I can (ever) read headers, I will fix this garbage code lol


            text_surface = font.render("wtv-1800:/preregister", True, (0, 0, 0))
            screen.blit(text_surface, (0, 0))
            pygame.display.flip()
            wtv = WebTVRequests(ip, port)
            res = wtv.getResponse("wtv-1800:/preregister?scriptless-visit-reason=10&0", f"wtv-client-serial-number: {ssid}").decode('utf-8', errors='replace')
            wtv.disconnect()
            ip = matchHostWtvHeadWaiter(res)
            port = int(matchPortWtvHeadWaiter(res))
            wtv = WebTVRequests(matchHostWtvHeadWaiter(res), int(matchPortWtvHeadWaiter(res)))
            wtv.getResponse("wtv-head-waiter:/login?", f"wtv-client-serial-number: {ssid}\r\nwtv-encryption: false")
            wtv.getResponse("wtv-head-waiter:/ValidateLogin?initial_login=true", f"wtv-client-serial-number: {ssid}\r\nwtv-encryption: false")
            wtv.disconnect()
            print("[DEBUG] Reconnecting because webtv")
            wtv = WebTVRequests(ip, port)
            res = wtv.getResponse('wtv-head-waiter:/login?no_response=true', f"wtv-client-serial-number: {ssid}\r\nwtv-encryption: false").decode('utf-8', errors='replace')
            challenge = matchWtvChallenge(res)
            print(challenge)
            wtv.disconnect()
            wtv = WebTVRequests(ip, port)
            wtv.getNoResponse('wtv-head-waiter:/login?no_response=true', f"wtv-client-serial-number: {ssid}\r\nwtv-encryption: false")
          #  wtv.getResponse('wtv-head-waiter:/ValidateLogin?initial_login=true&', f"wtv-client-serial-number: {ssid}\r\n wtv-encryption: false")
            res = wtv.getResponse("wtv-head-waiter:/login-stage-two?", f"wtv-client-serial-number: {ssid}\r\nwtv-encryption: false").decode('utf-8', errors='replace')
            wtv.disconnect()
            wtv = WebTVRequests(ip, int(matchPortWtvService(res, 'wtv-register')))
            res = wtv.getResponse("wtv-register:/splash?", f"wtv-client-serial-number: {ssid}\r\nwtv-encryption: false\r\nwtv-client-bootrom-version: 2046\r\nUser-Agent: Mozilla/4.0 WebTV/2.5.5 (compatible; MSIE 4.0)").decode('utf-8', errors='replace')
            HTML(string=res).write_png("temp.png")
            img = pygame.image.load("temp.png")


            screen.blit(img, (0, 0))



            # I know, this line is horrible, When I can get html rendering, I will fix it lol
            #splash_response = """<bgsound src="file://ROM/Sounds/Splash.mid">"""
#
#             if splash_response in res:
#                 pygame.mixer.music.stop()
#                 pygame.mixer.music.unload()
#                 pygame.mixer.music.load("assets/splash.mp3", namehint="mp3")
#                 pygame.mixer.music.play()
#                 splash = True
#             else:
#                 print("splash_response is not in res")
            #splash = True
            connecting = False

            # print(wtv1800)

#         if splash:
#
#             # Load the image
#             splash_image = pygame.image.load("assets/splash.gif").convert_alpha()
#
#             # Get the rect of the image and center it on the screen
#             image_rect = splash_image.get_rect(center=screen.get_rect().center)
#
#             # Draw the image to the screen
#             screen.blit(splash_image, image_rect)
#
#             pygame.display.flip()
            
            
            
            
            # if pygame.mixer.music.get_busy() != True:
            #    splash=False

        # End rendering
        pygame.display.flip()






if __name__ == "__main__":
    main()
    pygame.quit()
