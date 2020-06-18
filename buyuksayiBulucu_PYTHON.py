#Bismillah

def buyuksayi(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    elif b == a:
        return 'sayilar esit'
    else:
        print ('tanimsiz')

print('Girilen iki sayinin buyugunu bulan yazilim')

firstNumber = input('Ilk sayiyi giriniz: ')
secondNumber = input('Ikinci sayiyi giriniz: ')
print (buyuksayi(firstNumber, secondNumber))
