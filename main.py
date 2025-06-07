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


        # End rendering
        pygame.display.flip()






if __name__ == "__main__":
    main()
    pygame.quit()
