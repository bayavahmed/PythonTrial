#Bismillah

komsuIller = ['Kirikkale', 'Kırsehir', 'Nevsehir', 'Kayseri', 'Sivas', 'Tokat', 'Amasya', 'Corum']
print('Yozgatin komsu illerini ogrenelim')
girilen = input('Ilk harfi buyuk yaziniz: ')

i = 0


while i < len(komsuIller):
    if (girilen == komsuIller[i]):
        print('Tebrikler!')
        break
    i = i + 1
else:
    print('Uzgunum yanlis cevap')
          


    
