import requests
import time
import pygame
import socket
import json

def getText_ProxySocket(proxy_host, proxy_port, target_url):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((proxy_host, proxy_port))

    request = f"GET {target_url} HTTP/1.1\r\n\r\n"
    s.send(request.encode('utf-8'))

    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data
    s.close()
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
    print("Starting WebTV Client")
    print("Reading config.json")
    with open("config.json", 'r') as file:
        data = json.load(file)

    ip = data['ip']
    port = data['port']
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
            wtv1800 = getText_ProxySocket(ip, port, "wtv-1800:/preregister")
            print(wtv1800)


        # End rendering
        pygame.display.flip()






if __name__ == "__main__":
    main()
    pygame.quit()
