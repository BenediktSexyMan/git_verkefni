#Forritun Git Verkefni
val = input("Hvað viltu gera?\n1: tvær tölur?\n2: Nöfn?\n3: Hástafir og Lágstafir?\n4: Hætta?\n")
while val != "4":
    if val == "1":
        num1 = int(input("Gefðu mér tvær heiltölur!\n"))
        num2 = int(input())
        print("Tölurnar lagðar saman eru:", num1 + num2, "\nTölurnar margfaldaðar saman eru:", num1 * num2)
    if val == "2":
        fornafn = input("Hvert er nafn þitt?\n")
        eftirnafn = input("Hæ " + fornafn + "!\nHvert er eftirnafn þitt?\n")
        print("Hæ", fornafn + " " + eftirnafn)
    if val == "3":
        text = input("Gefðu mér texta!\n")
        ha = 0
        la = 0
        eftir = 0
        for x in range(len(text)):
            if text[x].isupper():
                ha += 1
            elif text[x].islower():
                la += 1
                if x > 0:
                    if text[x-1].isupper():
                        eftir += 1
        print("Það voru", ha, "hástafir\nÞað voru", la, "lágstafir\nÞað voru", eftir, "lágstafir sem fylgdu hástöfum!")
    val = input("Hvað viltu gera?\n1: 2 tölur?\n2: Nöfn?\n3: Hástafir og Lágstafir?\n4: Hætta?\n")
print("Takk Fyrir Mig!")
