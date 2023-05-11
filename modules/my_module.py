from astral import moon
from datetime import date

def set_color(color, txt, join=False, inpt=False):
    c = {"red": '\033[31;1m', "green": '\033[32;1m', "yellow": '\033[33m',
         "blue": '\033[34;1m', "magenta": '\033[35m', "cyan": '\033[36;1m', "end": '\033[m'}
    if not inpt:
        if join:
            print(c[color]+txt+c["end"], end=' ')
        else:
            print(c[color] + txt + c["end"])
    else:
        return f'{c[color]}{txt}{c["end"]}'


def display_crop(food):
    set_color("yellow", "Alimentos disponíveis: ")
    for key in food.keys():
        set_color("yellow", f"-- {key.capitalize()}")
    set_color("cyan", "=*" * 60)
    set_color("red", "DIGITE CONFORME O INFORMADO NA LISTA ACIMA!")


def set_food():
    return {"batata": ["Lua Minguante", "Primavera/Verão"], "cenoura": ["Lua Minguante", "Ano Inteiro"], "beterraba": ["Lua Minguante", "Ano Inteiro"],
        "couve": ["Lua Nova", "Outono"], "banana": ["Lua Nova", "Ano Inteiro"], "cebolinha": ["Lua Nova", "Primavera"], "espinafre": ["Lua Nova", "Primavera"],
        "soja": ["Lua Crescente", "Primavera"], "arroz": ["Lua Crescente", "Primavera/Verão"], "tomate": ["Lua Crescente", "Primavera"], "feijao": ["Lua Crescente", "Primavera"],
        "milho": ["Lua Crescente", "Primavera"], "abobora": ["Lua Crescente", "Primavera/Verão"], "berinjela": ["Lua Crescente", "Outono/Inverno"],
        "alface": ["Lua Cheia", "Ano Inteiro"], "repolho": ["Lua Cheia", "Ano Inteiro"], "couve-flor": ["Lua Cheia", "Primavera/Verão"]}


def get_moon(year, month, day):
    dt = date(year, month, day)
    value = moon._phase_asfloat(dt)
    mn = ''
    if 0 <= value <= 6.99:
        mn = "Lua Nova"
    elif value <= 13.99:
        mn = "Lua Crescente"
    elif value <= 20.99:
        mn = "Lua Cheia"
    else:
        mn = "Lua Minguante"
    return mn


def curiosity(moon):
    if moon == "Lua Cheia":
        set_color("blue", "Nessa fase a lua apresenta muita iluminação e força gravitacional por conta do alinhamento com a Terra e o sol.\n"
                          "Desta maneira, a seiva que ainda estava no caule, "
                          "sobe ainda mais, \nficando concentrada totalmente nas folhas e ramos.")
    elif moon == "Lua Crescente":
        set_color("blue", "As características principais dessa fase são: O aumento gradual da luz refletida do sol até"
                          " estar quase completamente iluminada, \nE a pouca influência da força da gravidade da lua."
                          "\nCom isso, a seiva que subiu pelo caule durante a fase nova, flui vagarosamente ainda pelo "
                          "caule, \njá atingindo ramos e folhas, proporcionando o desenvolvimento dos mesmos.")
    elif moon == "Lua Minguante":
        set_color("blue", "Nesta fase a influência da lua sobre a Terra é baixa. "
                          "\nIsso acontece porque ela não está alinhada com o sol e por isso, a sua força de gravidade e sua luminosidade é menor."
                          "\nCom isso, a gravidade da Terra exerce maior influência, uma vez que não está “competindo” com a força gravitacional da lua. "
                          "\nDesta forma, a seiva tem dificuldade de subir para o caule, ou seja, ir contra a gravidade da Terra, "
                          "\nficando, assim, concentrada nas raízes da planta.")
    elif moon == "Lua Nova":
        set_color("blue", "Nessa fase, o sol, a Terra e a lua estão completamente alinhados, somando forças gravitacionais. "
                          "\nIsso faz com que a seiva dos alimentos plantados seja “puxada” para cima, em direção ao caule.")

    set_color("green", "Resumindo, entre a lua minguante e nova deve ser plantado tudo que nasce abaixo do solo."
                       "\nE entre a lua crescente e cheia, tudo que nasce acima do solo.")


def get_season(m, d):
    s = ''
    if 3 <= m <= 6:
        if m == 3 and d < 21:
            s = "Verão"
        elif m == 6 and d >= 21:
            s = "Inverno"
        else:
            s = "Outono"
    elif 6 < m <= 9:
        if m == 9 and d >= 23:
            s = "Primavera"
        else:
            s = "Inverno"
    elif 9 < m <= 12:
        if m == 12 and d >= 21:
            s = "Verão"
        else:
            s = "Primavera"
    elif m < 3:
        s = "Verão"

    return s


def opfile(fl):
    try:
        a = open(fl, 'rt')
    except (FileNotFoundError, FileNotFoundError):
        a = open(fl, 'x')
    finally:
        a.close()
        return open_to_append(fl)


def open_to_append(fi):
    return open(fi, 'a')