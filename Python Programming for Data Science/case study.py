# Görev 2
# String ifadeyi büyük harflerle ve kelime kelime ayırınız.
from pexpect.replwrap import python

text = "The goal is to turn data into information, and information into insight."
buyutme = text.upper()
ayirma = buyutme.split()
print(ayirma)


# Görev 3

lst= ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
len(lst)
lst[0]
lst[10]
lst[0:4]
lst.pop(8)
lst.append(3)
lst.insert(8, "N")


# Görev 4
# Verilen sözlük yapısına aşağıdakileri uygulayınız.

dict= {"Christian": ["America", 18],
       "Daisy": ["England", 12],
       "Antonio": ["Spain", 22],
       "Dante": ["Italy", 25]}

dict.keys()
dict.values()
dict["Daisy"] =["Daisy", 13]
dict.update({"Ahmet": ["Turkey", 24]})
dict.pop("Antonio")

# Görev 5
# Argüman olarak bir liste olan, listenin içerisindeki tek ve çift sayıları farklı listelere atayan ve bu listeleri return eden bir fonksiyon.

lis= [2, 13, 18, 93, 22]
tek_list = []
cift_list = []

def func():
    for l in lis:
        if l %2 ==0:
            cift_list.append(l)
        else:
            tek_list.append(l)
    return

func()

# Görev 6
# İlk 3 öğrenci mühendislik fak başarı sırası, son 3 tıp fak başarı sırası. Fakültelere göre öğrencileri yaz

students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, student in enumerate(students[0:3],1):
    print(f"Mühendislik Fakültesi {index}. öğrenci {student}")

for index, student in enumerate(students[3:],1):
    print(f"Tıp Fakültesi {index}. Öğrenci {student}")

# Görev 7
# Aşağıda 3 adet liste verilmiştir. Dersin kodu, kredisi ve kontenjan bilgisi yer almaktadır. Zip kullanarak dersleri bastırınız.



ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

list(zip(ders_kodu,kredi,kontenjan))




# Görev 8
# Aşağıda 2 adet set(küme) verilmiştir. Eğer 1.küme 2. kümeyi kapsıyor ise ortak elemanlarını, kapsamıyor ise 2.kümenin
# 1.kümeden farkını yazdıracak fonksiyonu yazınız.

kume1 = {"data", "python"}
kume2 = {"data", "function", "qcut", "lambda", "python", "miuul"}

def kume_farki(kume1, kume2):
    if kume1.issuperset(kume2):
        ortak = kume1.intersection(kume2)
        return ortak
    else:
        fark = kume2.difference(kume1)
        return fark

kume_farki(kume1,kume2)

#######################################################
# Case Study 2 (List Comprehensions)
#######################################################

# Görev 1
# List Comprehensions yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

df.columns = ["NUM_" + col.upper()  if df[col].dtype!="O" else col.upper() for col in df.columns]

# Görev 2
# "car_crashes" verisinde isminde "no" barındırmayan değişkenlerin isminin sonuna "FLAG" yaz.

df = sns.load_dataset("car_crashes")
df.columns

[col.upper() if "NO" in col.upper() else col.upper() + "_FLAG" for col in df.columns]


# Görev 3
# List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden farklı olan değişkenlerin isimlerini seçiniz ve
# yeni bir data frame oluşturunuz.

df = sns.load_dataset("car_crashes")
df.columns

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]

new_df = df[new_cols]






