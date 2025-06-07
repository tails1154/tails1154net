import requests
import time
import pygame




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
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    pygame.mixer.init()
    pygame.mixer.music.load("assets/connect.mp3", namehint="mp3")
    pygame.mixer.music.play()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        screen.fill("black")





if __name__ == "__main__":
    main()
    pygame.quit()
