import time
from playsound import playsound

print("Aplicativo Pomodoro:")
print("I. 25 minutos de trabalho, 5 minutos de descanso.")
print("II. 50 minutos de trabalho, 10 minutos de descanso.")
print("III. Inserir tempo personalizado.")

opcao = input("\nInsira a opção desejada: ")

match opcao:
    case 'I':
        print("\nO pomodoro está começando.")
        tempo = 25*60
        while tempo:
            min = tempo//60
            seg = tempo % 60
            timer = '{:02d}:{:02d}'.format(min, seg)
            print(" " + timer, end="\r")
            time.sleep(1)
            tempo -= 1
        playsound("alarme.wav")
        print("\nO tempo acabou, pausa para o descanso.")
        tempo = 5*60
        while tempo:
            min = tempo//60
            seg = tempo % 60
            timer = '{:02d}:{:02d}'.format(min, seg)
            print(" " + timer, end="\r")
            time.sleep(1)
            tempo -= 1
        playsound("alarme.wav")
        print("\nO tempo acabou, volte ao trabalho.")
    
    case 'II':
        print("\nO pomodoro está começando.")
        tempo = 50*60
        while tempo:
            min = tempo//60
            seg = tempo % 60
            timer = '{:02d}:{:02d}'.format(min, seg)
            print(" " + timer, end="\r")
            time.sleep(1)
            tempo -= 1
        playsound("alarme.wav")
        print("\nO tempo acabou, pausa para o descanso.")
        tempo = 10*60
        while tempo:
            min = tempo
            seg = tempo % 60
            timer = '{:02d}:{:02d}'.format(min, seg)
            print(" " + timer, end="\r")
            time.sleep(1)
            tempo -= 1
        playsound("alarme.wav")
        print("\nO tempo acabou, volte ao trabalho.")

    case 'III':
        trabalho = int(input("\nInsira quantos minutos de trabalho você deseja: "))
        descanso = int(input("Insira quantos minutos de descanso você deseja: "))
        tempo = trabalho*60
        while tempo:
            min = tempo//60
            seg = tempo % 60
            timer = '{:02d}:{:02d}'.format(min, seg)
            print(" " + timer, end="\r")
            time.sleep(1)
            tempo -= 1
        playsound("alarme.wav")
        print("\nO tempo acabou, pausa para o descanso.")
        tempo = descanso*60
        while tempo:
            min = tempo//60
            seg = tempo % 60
            timer = '{:02d}:{:02d}'.format(min, seg)
            print(" " + timer, end="\r")
            time.sleep(1)
            tempo -= 1
        playsound("alarme.wav")
        print("\nO tempo acabou, volte ao trabalho.")
    
    case _:
        print("Insira uma opção válida.")
