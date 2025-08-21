def totalPartidas(partidasGanhas, partidasPerdidas):
    total = partidasGanhas - partidasPerdidas

    if total <= 10:
       nivel = "Ferro"
    elif 11 <= total <= 20:
        nivel = "Bronze"
    elif 21 <= total <= 50:
        nivel = "Prata"
    elif 51 <= total <= 80:
        nivel = "Ouro"
    elif 81 <= total <= 90:
        nivel = "Diamante"
    elif 91 <= total <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
        
    return total, nivel


partidas = int(input("Fale quantas partidas voce ganhou: "))
partidas2 = int(input("Fale quantas partidas voce perdeu: "))

total, nivel = totalPartidas(partidas, partidas2)
print(f"O Herói tem de saldo de {total} está no nível de {nivel}")




