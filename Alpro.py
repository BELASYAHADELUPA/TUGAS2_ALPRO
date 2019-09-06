print ("----------")
print ("Tel-U Give Away")
print ("----------")

opr = str(input("Operator : "))
IPK = float(input("IPK : "))

if opr == "Telkomsel" and IPK >= 3:
    print ("Congratulation you will get I-Phone X")
elif opr == "Telkomsel" and 2.75 <= IPK < 3 :
    print ("Congratulation you will get Playstation 4")
elif opr == "Telkomsel" and 2.25 <= IPK < 2.75 :
    print ("Congratulation you will get Voucher Oyo")
else:
    print ("Thank you for participate")
    