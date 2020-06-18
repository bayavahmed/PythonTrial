#Bismillah

def harfNotu(point):
    if (point >=90) and (point <=100):
        return 'AA'
    elif (point >= 85) and (point <= 89):
        return 'BA'
    elif (point >= 80) and (point <= 84):
        return 'BB'
    elif (point >= 75) and (point <= 79):
        return 'CB'
    elif (point >= 70) and (point <= 74):
        return 'CC'
    elif (point >= 60) and (point <= 69):
        return 'DD'
    elif (point >= 55) and (point <= 59):
        return 'FD'
    elif (point >= 0) and (point <= 54):
        return 'FF'
    else :
        return 'Gecerli bir not giriniz!'

sayi = input ('Sinav puanini harfe çevirmek için not giriniz: ')

print (harfNotu(int(sayi)))
