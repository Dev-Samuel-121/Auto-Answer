import pygame
import time
import os

def reprodutor(nome,duracao):
    pygame.init()
    pygame.mixer.music.load(str(nome))
    pygame.mixer.music.play()
    time.sleep(int(duracao))

def get_file(directory, file):
    base = "Sounds"
    return os.path.join(str(os.getcwd()),str(base),str(directory),str(file))

def sucess():
    arquivo = get_file(directory="Success",file="notification-sound-269266.mp3")
    reprodutor(nome=str(arquivo), duracao=3)

def error():
    arquivo = get_file(directory="Error",file="error-5-199276.mp3")
    reprodutor(nome=str(arquivo), duracao=1)

def bip():
    arquivo = get_file(directory="Bip",file="htranchant_01-91654.mp3")
    reprodutor(nome=str(arquivo), duracao=1)

def reset(secound):
    int(secound)
    for i in range(0,secound,1):
        bip()
        time.sleep(1)
