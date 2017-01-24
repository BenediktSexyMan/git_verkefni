#Forritun Git Verkefni
val = input("Hvað viltu gera?\n1: 2 tölur?\n2: Nöfn?\n3:")
while val != "4":
    if val == "1":
        num1 = int(input("Gefðu mér tvær heiltölur!\n"))
        num2 = int(input())
        print("Tölurnar lagðar saman eru:", num1 + num2, "\nTölurnar margfaldaðar saman eru:", num1 * num2)
    if val == "2":
        fornafn = input("Hvert er nafn þitt?\n")
        eftirnafn = input("Hæ " + fornafn + "!\nHvert er eftirnafn þitt?\n")
        print("Hæ", fornafn + " " + eftirnafn)
