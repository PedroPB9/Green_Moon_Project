from modules.my_module import *
from time import sleep

# Message Display
set_color("cyan", "=*" * 60)
set_color("yellow", "SEJA BEM VINDO(A) A", join=True)
set_color("green", "GREEN MOON!")
set_color("blue", "Aqui você poderá verificar a fase da lua mais recomendável para o plantio de seu alimento,")
set_color("blue", "E também, se a estação do ano, conforme a data inserida, é a correta para o cultivo de seu condimento.")
set_color("red", "ATENÇÃO!! A estação do ano pode vir a apresentar mudanças, de acordo com a região que você está!")
set_color("cyan", "=*" * 60)
sleep(0.6)
set_color("cyan", "Loading..."), set_color("cyan", "=*" * 60), sleep(6)

while True:
    # Date Input
    day = int(input(set_color("magenta", "Em que dia você deseja realizar o plantio? ", inpt=True)))
    month = int(input(set_color("magenta", "Em qual mês você pretende realizar o plantio? ", inpt=True)))
    year = int(input(set_color("magenta", "Em qual ano você quer realizar o plantio? ", inpt=True)))
    set_color("cyan", "=*" * 60)

    # Crop
    food = set_food()
    display_crop(food)
    set_color("cyan", "=*" * 60)
    sleep(0.65)
    set_color("cyan", "Loading..."), set_color("cyan", "=*" * 60), sleep(10)

    # Crop Input
    crop = str(input((set_color("magenta", "O que você gostaria de plantar? ", inpt=True)))).lower().strip()
    set_color("cyan", "=*" * 60)

    # Moon
    period_moon = get_moon(year, month, day)
    season = get_season(month, day)
    if period_moon == food[crop][0]:
        set_color("green", f"Correto! Plantar {crop} em {food[crop][0]} lhe proporcionará beneficíos!")

    else:
        set_color("red", f"{period_moon} não é o período ideal para plantar {crop}, o certo seria plantar em {food[crop][0]}.")

    # Season Check
    if season in food[crop][1]:
        set_color("blue", f"A estação escolhida para o plantio, {season.upper()}, é a recomendada.")
    elif food[crop][1] == "Ano Inteiro":
        set_color("cyan", f"{crop.upper()} pode ser plantado em qualquer período do ano!")
    else:
        set_color("red", f"A estação escolhida para o plantio, {season.upper()}, não é a recomendada!.")
        set_color("yellow", f"É preferível plantar {crop.upper()} em {food[crop][1].upper()}!")

    # Extra Info
    set_color("cyan", "=*" * 60)
    cur = str(input(set_color("magenta", f"Deseja ver o porquê de plantar {crop} em {food[crop][0]}[S/N]? ", inpt=True))).strip().upper()
    set_color("cyan", "=*" * 60)
    if cur == "SIM" or cur == "S":
        curiosity(food[crop][0])
        set_color("cyan", "=*" * 60)
        sleep(0.55)
        set_color("cyan", "Loading..."), set_color("cyan", "=*" * 60), sleep(10)

    set_color("red", "AVISO! \nO PROGRAMA PODE TER UMA MARGEM DE ERRO DE 1 DIA PARA MAIS, OU PARA MENOS NA HORA DE ANALISAR AS FASES DA LUA! ")
    set_color("cyan", "=*" * 60)

    #Record Data
    file = "status.txt"
    f = opfile(file)
    f.write(f"STATUS: COMIDA --> {crop} // LUA CORRESPONDENTE --> {food[crop][0]} // PERIODO RECOMENDADO --> {food[crop][1]}\n")
    f.close()

    #Continue?
    keep_running = str(input(set_color("magenta", "Você deseja prosseguir com a operação [S/N]? ", inpt=True)).strip().upper())
    set_color("cyan", "=*" * 60)
    if keep_running not in "SIM":
        set_color("green", "Obrigado por usar este código!")
        break