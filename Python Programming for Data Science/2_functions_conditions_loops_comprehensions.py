#######################################################
# FONKSİYONLAR, KOŞULLAR, DÖNGÜLER, COMPREHENSIONS
#######################################################
from collections.abc import dict_items

from PIL.ImImagePlugin import number
from dask.array.fft import ifft2
from mypyc.primitives.list_ops import new_list_set_item_op
from nltk.corpus import reuters
from openpyxl.styles.builtins import output
from pyarrow import dictionary

#######################################################
# Functions (Fonksiyonlar)
#######################################################

# Fonksiyon Okuryazarlığı
# ?print Bu kodu konsola yazmak daha mantıklı. Bu kod fonksiyonun içinde hangi parametrelerin çalıştığını gösterir.
# help(print) ile de çağrılabilir.
# sep aradaki boşluğu ifade eder. Bunu değiştirebiliriz.
print("a", "b")
print("a", "b", sep="__")
print("a", "b", end="?")

# Fonksiyon Tanımlama

# def function_name(arg or args):
#    statement(function body)


def calculate(x):
    print(x*2)

calculate(10)

# İki parametreli fonksiyon tanımlama

def summer(x,y):
    print(x+y)


# Docstring

# Fonksiyona bilgi notu eklemektir.
# Settings kısmından "Docstring" şeklinde aratıp "Python Integrated Tools" hangi şekilde Docstring yapılacağı değiştirilebilir.
# Fonksiyonu anlatmak için ilk kısımda ne yaptığı tek cümleyle anlatılır.
# Argümanların veri tipi ve ne yaptığı yazılır.
# Returns'ta çıkacak sonuç yazılır.
# Örnek bölümü de eklenebilir. (Examples) Bilgi bölümü için(Notes)

def summer(x,y):
    """
    Sum of two numbers
    Args:
        x: int, float
            First number
        y: int, float
            Second number
    Returns:
        int, float

    Examples:
    """
    print(x+y)

summer(3, 65)


# Fonksiyonların Statement/Body bölümü

def say_hi():
    print("Merhaba")
    print("Hello")
    print("Hi")


def say_hi(string):
    print(string)
    print("Hello")
    print("Hi")

say_hi("Makine Öğrenmesi")

def multiplication(a, b):
    c = a*b
    print(a, b, c)

multiplication(4, 6)


# Girilen değerleri bir liste içinde saklayacak fonksiyon

toplam_list = []

def ekle_list(x, y):
    z = x * y
    toplam_list.append(z)
    print(toplam_list)

ekle_list(3, 8)

# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)

# Fonksiyon içerisinde parametreleri tanımlamaya denir. a=1 gibi
# Print fonksiyonundaki sep, end gibi
# Boş bırakıldığında tanımlı değeri yazar ancak değer girilirse o değeri öncelik olarak alır.

def divide(a, b):
    print(a / b)

divide(1, 2)

def divide(a, b=4):
    print(a / b)

divide(5)

def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")

say_hi("Selam")
# Çıktısı Selam olacaktır.

# Ne Zaman Fonksiyon Yazılır?

# warm(ısı), moisture(nem), charge(pil)
(15+25) / 30
# Tek tek uğraşmamak için fonksiyona ihtiyaç duyulur.

# DRY prensibi

def calculate(warm, moi, cha):
    print((warm + moi) / cha)

calculate(30, 52, 79)


# Return: Fonksiyon çıktılarını girdi olarak kullanmak için kullanılan yapıdır.
# Returnden sonra yazılan ifadeler çıkar.


def calculate(warm, moi, cha):
    return (warm + moi) / cha

calculate(30, 52, 79) * 10
a = calculate(30, 52, 79)

def calculate(warm, moi, cha):
    warm = warm*2
    moi = moi*2
    cha = cha*2
    output = (warm + moi) / cha
    return warm, moi , cha, output

warm, moi , cha, output = calculate(30, 52, 79)
# Burda saklanan değerler fonksiyonun içinden çıkan değerlerdir.


# Fonksiyon İçerisinden Fonksiyon Çağırma

def calculate(warm, moisture, cha):
    return int((warm + moisture) / cha)

calculate(45,29, 32) * 10

def standartization(a, b):
    return a*10 / 100 * b * b

standartization(4, 32)

def all_calculate(warm, moisture, cha, b):
    a = calculate(warm, moisture, cha)
    p = standartization(a, b)
    return p*10
# return kısmına ne yazarsan o çıkar.

all_calculate(24, 42, 50, 25)


# Local ve Global Değişkenler
# Local değişkenler sadece o fonksiyonun vs içerisinde olan değişkenlerdir. Ancak global değişkenler her yerden erişilebilir.
# Local etki alanındaki bir değişken global etki alanındaki değişkeni etkileyebilir.


list_store = [1, 2]

def add_element(x, y):
    c = x * y
    list_store.append(c)
    print(list_store)

add_element(4, 5)

#######################################################
# Conditions(Koşullar)
#######################################################

# IF

if 1==4:
    print("eşittir")

number = 10
if number==10:
    print("number is 10")

def number_check(number):
    if number==10:
        print("number is 10")

number_check(10)

# Else

def number_check(number):
    if number==10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(13)

# Elif

def number_check(number):
    if number==10:
        print("number is 10")
    elif number<10:
        print("number is less than 10")
    else:
        print("number is greater than 10")

number_check(13)

#######################################################
# Loops (Döngüler)
#######################################################

# for döngüsü

students = ["John", "Mark", "Venessa", "Mariam"]

students[0]

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(int((salary * 120) / 100))

for salary in salaries:
    print(int((salary * 130) / 100))

def new_salary():
    for salary in salaries:
        print(int((salary * 120) / 100))
new_salary()

def new_sal(salary, rate):
    return int((salary * rate/100 + salary))

new_sal(1000, 20)

for salary in salaries:
    print(new_sal(salary,20))


for salary in salaries:
    if salary <3000:
        print(new_sal(salary, 40))
    else:
        print(new_sal(salary, 20))

salaries = [1000, 2000, 3000, 4000, 5000]


#######################################################
# Uygulama
#######################################################

# Soru: Aşağıdaki şekilde string değiştiren fonksiyon yazmak.
# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

len("miuul")
range(len("miuul"))

def alternating(string):
    new_string = ""
    # girilen stringin indexlerinde gez.
    for string_index in range(len(string)):
        # index çift ise büyük harfe çevir ve new_string'e ekle.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        #index tek ise küçük harfe çevir ve new_string'e ekle.
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("hi my name is john and i am learning python")


# break & continue(pas geç) & while

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary==4000:
        break
    print(salary)


for salary in salaries:
    if salary==3000:
        continue
    print(salary)
# 3000'i pas geçer.

# while
number=1

while number<5:
    print(number)
    number += 1



# Enumerate Otomatik Counter/Indexer ile for loop

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

# kaçtan başlamasını istiyorsanız enumerate(students, n)
for index, student in enumerate(students):
    print(index, student)

student_list = []
student_list2 = []

for index, student in enumerate(students):
    if index % 2 == 0:
        student_list.append(student)
    else:
        student_list2.append(student)

print(student_list)
print(student_list2)


# Uygulama - Mülakat Sorusu

# divide_student fonksiyonu yaz.
# Çift indexte yer alanları bir listeye
# Tek indexte yer alanları başka listeye
# Fakat bu liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]

# Yeni bir liste oluşturulur içine 2 boş liste açılır.

def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index %2 ==0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

st = divide_students(students)
st[0]


# Alternating fonksiyonunu enumerate ile gerçekleştirme

def alternating_with_enumerate(string):
    n_string = ""
    for index, string in enumerate(string):
        if index %2==0:
            n_string += string.upper()
        else:
            n_string += string.lower()
    print(n_string)

alternating_with_enumerate("deneme")


# Zip

# Bir liste içerisinde Tuple cinsinden 3 ayrı listeyi birbirine bağladı.

students = ["John", "Mark", "Venessa", "Mariam"]
department = ["mathematics", "statistics", "physics","astronomy"]
ages = [23, 30, 26, 22]

# list fonksiyonu liste oluşturma şeklidir.
list(zip(students, department, ages))

#######################################################
# lambda, map, filter, reduce
#######################################################


#######################################################
# Lambda
#######################################################
# Kullan-at fonksiyondur. Bir tanımlama işlemi yapılmadan kullanılabilir.


def summer(a, b):
    return  a+b

summer(3,5)* 10

# a ve b parametrelerinden oluşan bir fonksiyondur.":" şu işi yapar. (a+b)
new_sum = lambda a, b: a+b

new_sum(4,2)


#######################################################
# map
#######################################################

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return (x * 120) / 100
new_salary(1000)

for salary in salaries:
    print(new_salary(salary))


# Önce fonksiyon daha sonra nesne
# lambda burada new_salary fonksiyonunun yerine geçer.
list(map(new_salary, salaries))

list(map((lambda x: (x * 120)/ 100), salaries))

list(map(lambda x: x**2 , salaries))


#######################################################
# Filter
#######################################################
# Filtrelemek için kullanılır. Örneğin: 2'ye bölünenleri ayır.

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list(filter(lambda x: x%2 == 0, list_store))


#######################################################
# Reduce (İndirgemek)
#######################################################

from functools import  reduce

list_store = [1, 2, 3, 4]

reduce(lambda x, y: x + y, list_store)

#######################################################
# Comprehensions
#######################################################

# List Comprehensions

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return (x * 120) / 100

new_sal = []

for salary in salaries:
    new_sal.append(new_salary(salary))
    print(new_sal)

for salary in salaries:
    if salary <3000:
        new_sal.append(new_salary(salary))
    else:
        n_salary = (salary * 120) / 100
        new_sal.append(n_salary)
new_sal[0]

# Buraya kadarki kısım eski yaptıklarımız. List Comprehensions yapısı bundan sonraki kısımdadır.

# Öncelikle liste yapısı oluşturulur.

[salary * 2 for salary in salaries]

# Eğer else kullanılmıyorsa if sağ tarafa yazılır. Kullanılıyorsa for sağ tarafta kalır.

[salary * 2  for salary in salaries if salary<3000]

[salary * 2 if salary <3000 else salary*4 for salary in salaries]

[new_salary(salary) if salary <3000 else salary*3 for salary in salaries]

[new_salary(salary * 2) if salary <3000 else salary * 3 for salary in salaries]

# Örnek

students = ["John", "Mark", "Venessa", "Mariam"]       # Tüm öğrenciler

students_no = ["John", "Venessa"]                      # İstenmeyen öğrenciler küçük yazılacak geri kalanlar büyük.

[student.lower() if student in students_no else student.upper() for student in students]

[student.upper() if student not in students_no else student.lower() for student in students]


# Dict Comprehensions

dictionary = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4}

dictionary.keys()
dictionary.values()
dictionary.items()                # Her bir elemanı tuple şeklinde liste formunda erişmek için kullanılır.

# Dictionary çağrılamaz onun yerine dictionary.items() çağrılmalıdır.

{k: v**2 for (k, v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}

{k.upper(): v**2 for(k,v) in dictionary.items()}


#######################################################
# Uygulama - Mülakat Sorusu
#######################################################

# Çift sayıların karesi alınarak bir sözlüğe eklenmek isteniyor.
# Keyler orijinal sayı, valueler karesi alınmış sayılar olacak.

numbers = range(10)

new_dict = {}


for n in numbers:
    if n % 2 ==0:
        # new_dict[n]: key, n**2: value
        new_dict[n] = n**2

{n: n**2 for n in numbers if n %2==0}


# List & Dict Comprehension Uygulamalar

# Bir veri setindeki değişken isimlerini değiştirmek

# before:
# ["total", "speeding", "alcohol", "not_distracted", "no_previous", "ins_premium", "ins_losses", "abbrev"]

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

# Not: df =data frame (veri çerçevesi) verileri tablo şeklinde tutmak excel gibi

# Data frame'in değişkenlerinin isimlerini büyütme. Normal yöntemlerle

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())

A =[]

for col in df.columns:
    A.append(col.upper())

df.columns = A


# List Comprehension ile veri setindeki değişkenleri büyütme

import seaborn as sns
df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]


# İsminde "INS" olanların başına "FLAG" diğerlerine NO_FLAG ekle.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

["FLAG_"+col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

[col for col in df.columns if "INS" in col]                                          # İçinde "INS" geçenler

["FLAG_"+col for col in df.columns if "INS" in col]                                  # İçinde "INS" geçenlerin başına "FLAG"

["FLAG"+col if "INS_" in col else "NO_FLAG_" + col for col in df.columns]            # Sorunun cevabı

df.columns = ["FLAG_"+col if "INS" in col else "NO_FLAG_" + col for col in df.columns]


# Örnek
# Key'i string value'si aşağıdaki gibi bir sözlük oluşturmak.
# Sadece sayısal değişkenler için yapılması gerekiyor.

# Output :
# {"total": ["mean", "min", "max", "sum"],
#  "speeding": ["mean", "min", "max", "sum"],
#  "alcohol": ["mean", "min", "max", "sum"],
#  "not_distracted": ["mean", "min", "max", "sum"],
#  "no_previous": ["mean", "min", "max", "sum"],
#  "ins_premium": ["mean", "min", "max", "sum"],
#  "ins_losses": ["mean", "min", "max", "sum"]}

#  Listenin içinde yazanlar aslında birer fonksiyon, agg(aggrigation) fonksiyonunu kullanarak num_cols içindeki data framelerle eşler
#  ve listenin içindeki fonksiyonları data framedeki değişkenlere uygular.


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype !="O" ]
# "O" object yani kategorik değişkenleri temsil eder.
# Sadece sayısal değerlere ihtiyacımız olduğu için olmayanları seçtik.


soz = {}
agg_list = ["mean", "min", "max", "sum"]

# key değeri köşeli parantez ile yazılır value'ye eşitlenir.
for col in num_cols:
    soz[col] = agg_list

# Kısa yol (Comprehensions ile)
# head() boş bırakılırsa ilk 5ini getirir. 0-4

new_diction = {col:agg_list for col in num_cols }
df[num_cols].head()

df[num_cols].agg(new_diction)









