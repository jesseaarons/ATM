print("selamat datang di teranesia ATM")
print("pilih option : ")
print("1. check uang anda")
print("2. ambil  uang anda")
print("3. setor-tunai")
option=int(input("silahkan pilih option :"))
if option==1:
    print("uang anda berjumlah Rp.10.000.000")
elif option==2:
    print("nominal uang anda ambil RP 5.000.000, mau ambil berapa?")
    print("1. RP. 500.000")
    print("2. RP. 1000.000")
    uang_kamu=10000000
    option2=int(input("option :"))
    if option2==1:
        hasil1=uang_kamu-500000
        print("uang kamu berjumlah :",hasil1)
    elif option2==2:
        hasil2=uang_kamu-1000000
        print("uang kamu berjumlah :",hasil2)
    else:
        print("keyword anda salah!")
elif option==3:
        print("setor-tunai")
        option3=int(input("masukan uang anda :"))
        hasil3=10000000+option3
        print("jumlah uang anda adalah", hasil3)
else:
    print=("keyword anda salah, mohon coba lagi")

