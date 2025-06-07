import requests
import time
import pygame
import socket
import json
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
        request = f"GET {url}\nHost: {url}\n{headers}\n\n"
        print(f"[DEBUG] Sending {request}")
        self.s.send(request.encode('utf-8'))
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


            text_surface = font.render("wtv-1800:/preregister", True, (0, 0, 0))
            screen.blit(text_surface, (0, 0))
            pygame.display.flip()
            wtv = WebTVRequests(ip, port)
            wtv.getNoResponse("wtv-1800:/preregister?scriptless-visit-reason=10&0", "wtv-client-serial-number: {ssid}")

            print(wtv1800)


        # End rendering
        pygame.display.flip()






if __name__ == "__main__":
    main()
    pygame.quit()
