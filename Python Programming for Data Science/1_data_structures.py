# VERİ YAPILARI (DATA STRUCTURES)
######################################
# - Sayılar = integer(int), float, complex
# - Karakter dizileri =strings(str)
# - Boolean (True-False) bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set
from statsmodels.sandbox.regression.example_kernridge import upper
from statsmodels.sandbox.regression.runmnl import tree0

# Sayılar (int)
x=46
type(x)

# Sayılar (float)
y=10.4
type(y)

# Sayılar (complex)
z = 2j + 1
type(z)

# Strings
x = "Hello AI Era"
type(x)

# Boolean
True
False
type(True)
3 == 2
type(4 == 2)

# Liste

x=["btc","eth","xrp"]
type(x)

# Sözlük (Dictionary): dict
# Sözlük oluştururken {} kullanılır.
# Key ve value değerlerinden oluşur. İlk yazılan key, ikinci yazılan value(değer)dir.

x={"name": "Peter", "Age": 36}
type(x)

# Tuple
x = ("python", "ml", "ds")
type(x)

# Set (Kümeler)
x = {"python", "ml", "ds"}
type(x)


# !!!! Not: Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collections(arrays) olarak geçmektedir.

#######################################################
# Sayılar
#######################################################

a = 5
b = 10.5
a * 3
a * b / 10
a ** 2

# Dönüştürme

int(b)
float(a)

c = a * b / 10
int(c)
#######################################################
# Karakter Dizileri
#######################################################

print("john")

name = "John"
print(name)


# Çok Satırlı Karakter Dizileri

# long_str = """Veri Yapıları: Hızlı Özet,
# Sayılar :Int, Float, Complex,
# Karakter Dizileri (Str)"""
# print(long_str)

# Karakter Dizilerinde Eleman Seçme

name
name[0]

# Karakter Dizilerinde Slice İşlemi
# Sonraki yazılan dahil değil

name[0:2]
# long_str[1:20]

# Karakter Dizileri İçinde Eleman Sorgulama

# long_str

# "veri" in long_str            # Büyük harf küçük harf duyarlılığı vardır.


#######################################################
# Karakter Dizisi Methodları (String Methods)
#######################################################

# dir: içine yazılan str veya int ile ilgili kullanılabilecek methodları gösterir.

dir(int)
dir(str)

# len : boyut bilgisi için kullanılır.

name="john"
type(name)

len(name)
len("miuul")

# !!!!Not: Methodlar ve fonksiyonların işlevleri aynıdır. Tek farkı fonksiyonlar bağımsız, methodlar classlar içinde tanımlanmış olmasıdır.

# Upper() & Lower() :küçük büyük dönüşümleri

"miuul".upper()
"MIUUL".lower()

# replace: karakter değiştirmek için kullanılır

hi = "Hello AI Era"
hi.replace("l","n")

# split: böler

"Hello AI Era".split()

# strip: kırma

" ofofo ".strip()
"ofofo".strip("o")

# capitalize: ilk harfleri büyütür.

"miuul".capitalize()

dir("deneme")

"foo".startswith("f")

#######################################################
# Liste
#######################################################
# Değiştirilebilir.
# Sıralıdır. Index işlemi yapılabilir.
# Kapsayıcıdır. Birden fazla veri yapısını tutabilir.

notes = [1, 2, 3, 4]
type(notes)

names = ["a", "b", "v"]
type(names)

not_name = [1, 2, 3, True, "a", "b", [1, 2, 3]]

not_name[0]
not_name[6]
not_name[6][0]

notes[0] = 99
not_name[0:4]

# Liste Methodları

dir(list)

len(notes)
len(not_name)

# append: listelere eleman ekler.

notes.append(3)

# pop: indexe göre eleman siler.
notes.pop(4)

#insert: indexe göre ekler. İlk yazılan index numarası, 2.yazılan ise girilmek istenen değerdir.

notes.insert(2,45)

#######################################################
# Sözlük (Dictionary)
#######################################################
# Değiştirilebilir.
# Sırasız. (3.7 sürümünden sonra sıralı olmuştur.)
# Kapsayıcı

# key- value

dictionary = {"REG" : "Regression",
              "LOG" : "Logistic Regression",
              "CART" : "Classification and Reg"}
dictionary["REG"]

dictionary= {"REG" : ["RMSE", 10],
             "LOG" : ["MSE", 20],
             "CART" : ["SE", 30],}
dictionary["REG"]
dictionary["CART"][1]

# Key sorgulama (İçinde olup olmama)

"CART" in dictionary

# Keye göre Value çağırma
# İki şekilde de yapılabilir.
dictionary["REG"]
dictionary.get("REG")

# Value değiştirme
dictionary["REG"] = ["YSA", 40]

# Tüm keylere ve valuelere erişmek
dictionary.keys()
dictionary.values()

# Tüm çiftleri Tuple formatına çevirme
# Sözlüğü liste içerisinde key ve valueları Tuple cinsinde verir.
dictionary.items()

# Key ve value güncelleme yoksa eklemek için de update kullanılır.
dictionary.update({"REG" : 11})
dictionary.update({"SA" : ["AS", 31]})


#######################################################
# Tuple (Demet) Listelerin değişmez halidir.
#######################################################
# Değiştirilemez.
# Sıralıdır.
# Kapsayıcıdır.

d = ("john", "kerem", 1, 3)
d[0]
d[0:3]

d[0] = 35
# Hata verir.
d = list(d)
d[3] = 40
d = tuple(d)

#######################################################
# Set (Küme)
#######################################################

# Değiştirilebilir.
# Sırasızdır. Eşsizdir.
# Kapsayıcıdır.

# İki kümenin farkı :difference()

set1 = set([1, 3 , 5 ])
set2 = set([1, 2 , 3 ])

# set1'de olup set2'de olmayan
set1.difference(set2)
set1 - set2
# set2'de olup set1'de olmayan
set2.difference((set1))

# İki kümede de birbirine göre olmayanlar: symmetric_difference()
set1.symmetric_difference(set2)

# İki kümenin kesişimi: intersection()
set1.intersection(set2)

# İki kümenin birleşimi: union()
set1.union(set2)

# İki kümenin kesişimi boş mu? isdisjoint()
set1 = {7, 8, 9}
set2 = {5, 6, 7, 8, 9, 10}
set1.isdisjoint(set2)

# İlk yazılan 2.nin alt kümesi midir? issubset()
set1.issubset(set2) # True
set2.issubset(set1) # False

# İlk yazılan 2.yi kapsıyor mu? issuperset()
set1.issuperset(set2)    # False
set2.issuperset(set1)    # True


name = "VBO_Bootcamp"
type = "new_term"
f"Name:{name} type:{type}"





