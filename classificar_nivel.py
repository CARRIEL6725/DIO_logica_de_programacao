nome_heroi = "Pacato"
nivel = 7001
nivel_heroi = ""

if nivel <= 1000:
    nivel_heroi = "Ferro"
elif nivel >= 1001 and nivel <= 2000:
    nivel_heroi = "Bronze"
elif nivel >= 2001 and nivel <= 5000:
    nivel_heroi = "Prata"
elif nivel >= 6001 and nivel <= 7000:
    nivel_heroi = "Ouro"
elif nivel >= 7001 and nivel <= 8000:
    nivel_heroi = "Platina"
elif nivel >= 8001 and nivel <= 9000:
    nivel_heroi = "Ascedente"
elif nivel >= 9001 and nivel <= 10000:
    nivel_heroi = "Imortal"
else:
    nivel_heroi = "Radiante"

print(f"O herói de nome {nome_heroi} está no nível de {nivel_heroi}.")
