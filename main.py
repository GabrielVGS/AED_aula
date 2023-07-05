from p import remove_p

words = """ O Internacional não tem jogo no meio desta semana, mas tem um compromisso importante. Nesta quarta-feira (5), às 13h (de Brasília), ocorre o sorteio das oitavas de final da Copa Libertadores. O Colorado conhecerá o seu adversário nesta fase da competição.
Classificado em primeiro no grupo B, o Inter já sabe que nas oitavas de final jogará o primeiro jogo fora de casa e fará o enfrentamento decisivo como mandante, no estádio Beira-Rio.
O Inter está no pote 1. Desta forma, enfrentará um dos clubes posicionados no pote 2. Este segundo pote é preenchido por clubes que classificaram em segundo lugar nos seus respectivos grupos.
Seja quem for o adversário, vai ser um confronto difícil. Oitavas de final nunca é fácil, pois jogar a primeira fase já difícil. Passamos pela primeira fase que era uma obrigação. Passada essa pressão, se estabelece uma nova realidade. Vamos jogar o segundo jogo em casa. Vamos aguardar pra analisar o adversário. – disse o técnico.
Mesmo após conhecer seu adversário, o Inter terá o mês de julho apenas com Brasileirão. Os jogos de ida das oitavas de final da Copa Libertadores serão disputados entre os dias 1 e 3 de agosto. Os duelos de volta entre 8 e 10 do mesmo mês."""


words = words.lower()
words_list = words.split(" ")
words_list = [remove_p(word) for word in words_list if word !=""]
c = 0
lst = []
used_words = []
for word in words_list:
    if word not in used_words:
        used_words.append(word)
        for i in words_list:
            if i == word:
                c += 1
        lst.append(c)
        c = 0

print(len(words_list))
s = ""
for i in range(len(used_words)):
    s += f"{used_words[i]};{lst[i]}\n"



with open("freq.csv","w") as cv:
    cv.write(s)
