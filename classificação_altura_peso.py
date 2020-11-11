altura = float(input("Digite sua altura: "))
massa = float(input("Digite sua massa corporea: "))
if altura <= 1.20 and massa <=60:
    print("Categoraia A")
elif altura <= 1.20 and 90 >= massa >= 60:
    print("Categoraia D")
elif altura <= 1.20 and massa > 90:
    print("Categoraia G")
elif 1.20 > altura >= 1.70 and massa <=60:
    print("Categoria B")
elif 1.20 > altura >= 1.70 and 90 >= massa >= 60:
    print("Categoria E")
elif 1.20 > altura >= 1.70 and massa > 90:
    print("Categoria H")
elif altura > 1.70 and massa <=60:
    print("Categoria C")
elif altura > 1.70 and 90 >= massa >= 60:
    print("Categoria F")
elif altura > 1.70 and 90 and massa > 90:
    print("Categoria I")

