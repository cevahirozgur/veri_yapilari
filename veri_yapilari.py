#Sayılar
#tam sayılar | integer (int),
#ondalıklı sayılar | float (float)
#karmaşık sayılar | complex

#Karakter Dizileri
#strings (str)

#String Birleştirme (+)

first_name = "Cevahir"
last_name = "Özgür"

print(first_name + " " + last_name)

#Karakter Dizilerinin Elemanlarına Erişmek (Index ile)

language = "python"
first_character = language[0]
print(first_character)

#Karakter Dizilerinde Slice İşlemi (Dilimleme)
# [start : stop : step-over]

language = "python"

range_1 = language[0:2]
range_1

range_2 = language[0::1]
range_2

range_3 = language[::2]           #2şer atla
range_3

reverse_string = language[::-2]   #Tersten 2şer atla


#Boolean (Mantıksal Operatörler)
#True / False

True or False

True and False

#Liste (list)
#list[0] = “x” (Önceden atadığımız listenin ilk elemanını x ile değiştirir.)

list = ["Alex", 24,"Lui"]
list[0] = "x"
list

#yedek_liste = list[:] (Listeyi kopyalar.)

list = ["Alex", 24,"Lui"]
yedek_liste = list[:]
yedek_liste

#Listelere Eleman Ekleme
#append : Liste sonuna eleman ekler.

scores = [54,63,75,29]
scores.append(85)
print(scores)

#insert : Listede önce indeksi bulur ona göre elemanı ekler.
scores.insert(2,14)
print(scores)

#extend : Bir listeyi başka bir listeye ekler

a_list = ["Alex", 24,"Lui"]
b_list = [65,"Cindy", 48, "Leo",41]

b_list.extend(a_list)
print(b_list)

#len : Listenin eleman sayısını belirtir.

scores = [54,63,75,29]
len(scores)

#pop : indekse göre eleman siler.

b_list = [65,"Cindy", 48, "Leo",41]
b_list.pop(1)
b_list

#Dictionary (dict)

user = {"name" : "Cevahir",
        "age" : 25,
        "country" : "Turkey"}

user.keys()
Out: dict_keys(['name', 'age', 'country'])
user.values()
Out: dict_values(['Cevahir', 25, 'Turkey'])

#key-Value değerini güncellemek

user.update({"age" : 32})
user

#key-value çiftlerini tuple halinde listeye çevirme

user = {"name" : "Cevahir",
        "age" : 25,
        "country" : "Turkey"}

user.items()

#Tuple (Demet)

t = (65, "Cindy", 48, "Leo", 41)
type(t)
Out: tuple

#indexe göre eleman çağırma

t[1:4]

#"TUPPLE"lar DEĞİŞTİRİLEMEZ
# t = (65,"Cindy", 48, "Leo",41)
# t[0] = 12
# Out: ERROR

#Eğer değiştirmek istersek listeye çeviririz.
#İstediğimiz değeri değiştirdikten sonra listeyi tekrar tuple haline dönüştürürüz

t = list(t)
t[0] = 12
t = tuple(t)
t

