#### PYTHON ALIŞTIMALAR ####
### Görev 1 - Verilen değerlerin veri yapılarını inceleyiniz ####

x = 8
type(x)


y = 3.2
type(y)


z = 8j + 18
type(z)


a = "Hello World"
type(a)


b = True
type(b)


c = 23 < 22
type(c)


l = [1, 2, 3, 4]
type(l)


d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d)


t = ("Machine Learning", "Data Science")
type(t)


s = {"Python", "Machine Learning", "Data Science"}
type(s)


##### Görev 2 - Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
##### Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight."

text.upper().replace(',', '').split()


#### Görev 3 - Verilen listeye aşağıdaki adımları uygulayınız.
# Adım 1: Verilen listenin eleman sayısına bakınız.
# Adım 2: Sıfırıncı ve onuncu indeksteki elemanlarını çağırınız.
# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesini oluşturunuz.
# Adım 4: Sekizinci indeksteki elemanı siliniz.
# Adım 5: Yeni bir eleman ekleyiniz.
# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
# Adım 1:
len(lst)
# Adım 2:
lst[0]
lst[10]
# Adım 3:
data_list = lst[0:4]
data_list
# Adım 4:
del list[8]
lst
# Adım 5:
lst.append('0')
lst
# Adım 6:
lst.insert(8, "N")
lst


#### Görev 4 - Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

#Adım1: Key değerlerin erişiniz.
#Adım2: Value'lara erişiniz.
#Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
#Adım4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
#Adım5: Antonio'yu dictionary'den siliniz.

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Adım 1:
dict.keys()
# Adım 2:
dict.values()
# Adım 3:
dict.update({'Daisy': ["England", 13]})
dict
# Adım 4:
dict.update({'Ahmet': ["Turkey",24]})
dict
# Adım 5:
dict.pop('Antonio')
dict


#### Görev 5 - Argüman olarak bir liste alan,
# listenin içerisinde tek ve çift sayıları ayrı listeye atayan
# ve bu listeleri return eden fonksiyon yazınız.

# l = [2, 13, 18, 93, 22]
# def func(..):
#    ...
#    ...
#    return ..
# even_ list, odd_list = func(l)

l = [2,13,18,93,22]
def func(list):

    even_list = []
    odd_list = []

    for i in list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list,odd_list

        even,odd = func(l)
        func(l)



#### Görev - 4: Aşağıda verilen listede mühendislik ve tıp fakültelerinde
# dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken
# son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, ogrenci in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi",i," . öğrenci:", ogrenci)
    else:
        i += 2
        print("Tıp Fakültesi",i, ". öğrenci:", ogrenci)

muhendislik_sirasi = range(1,4)
tip_sirasi = range(1,4)



#### Görev 7 - Aşağıda 3 adet liste verilmiştir.
# Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır.
# Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "Psy1001", "Huk1005", "Sen2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu,kredi,kontenjan):
print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} dır.")



#### Görev 8 - Aşağıda 2 adet set verilmiştir. Sizden istenilen:
# eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
# eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

# beklenen çıktı:
# {'function', 'qcut', 'miuul', 'lambda'}
# issuperset() metodu, intersection ve difference metodları
def kume(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1, kume2)
kume(kume2,kume1)

