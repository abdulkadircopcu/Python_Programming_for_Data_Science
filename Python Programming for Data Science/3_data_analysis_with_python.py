#######################################################
# Python ile Veri Analizi (Data Analysis with Python)
#######################################################
# - NumPy
# - Pandas
# - Matplotlib & Seaborn (Veri Görselleştirme)
# - Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional Exploratory Data Analysis)
from pickletools import float8

#######################################################
# NumPy (Numerical Python)
#######################################################
# Neden NumPy
# NumPy Array'i Oluşturmak
# NumPy Array Özellikleri
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi
# Slicing
# Fancy Index
# NumPy'da Koşullu İşlemler
# Matematiksel İşlemler


# NumPy' ın Listelerden farkı:
# - Verimli veri saklama, hız (Sabit bir veri tipini saklar. Bütün verilerin yapısı aynıdır.)
# - Vektörel İşlemler (Listelerden daha kolaydır.)


# Neden NumPy
# Klasik Python yolu

a= [1, 2, 3, 4]
b= [2, 3, 4, 5]
# Liste elemanları birbiriyle çarpılıyor
ab= []

for i in range(len(b)):
    ab.append(a[i] * b[i])

# NumPy yolu

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a*b

# Numpy Array oluşturma

import  numpy as np

np.array([1, 2, 3, 4, 5])                      # Liste üzerinden NumPy array' i
type(np.array([1, 2, 3, 4, 5]) )               # NumPy numpy.ndarray

np.zeros(10, dtype=int)                 # 0lardan oluşan array
np.random.randint(2, 15, size = 13)                  # Verilen iki değer(ilk kısım boş bırakılırsa 0 sayılır) arasında istediğin kadar sayı seçip array oluşturma
np.random.normal(50, 0.1, size = (4, 2))        # 1. Ortalaması, 2. standart sapması ve 3, boyutu verilen normal dağılıma uyan bir array

# Yaygın kullanımda sıfırdan array oluşturulmaz. Var olan bir array NumPy' a aktarılır.


# NumPy Array Özellikleri

# ndim = boyut sayısı
# shape = boyut bilgisi
# size = toplam eleman sayısı
# dtype = array veri tipi

import numpy as np

a= np.random.randint(50000, size= (5,2))
a.ndim
a.shape
a.size
a.dtype


# Reshaping (Yeniden Şekillendirme)

import numpy as np

np.random.randint(1, 15, size= 9)
np.random.randint(1, 15, size= 9).reshape(3,3)

ar = np.random.randint(1, 15, size= 9)
ar.reshape(3,3)


# Index Seçimi

import numpy as np

a= np.random.randint(10, size =10)
a[0]
a[0:6]                                             # Index seçimi ancak slicing denir.
a[0::6]
a[0]= 6


b = np.random.randint(10, size= (3, 5))            # Önce satır sonra sütun
b[2,3]
b[1,4] = 24

b[0,3] = 4.3                                       # Float veri eklense bile int olarak alır. 4.9 = 4
b

b[:, 0]                                            # İlk yazılan satır, 2. yazılan sütun değeridir. (:) hepsini seç anlamına gelir.
b[1,:]                                             # 1. satır bütün sütunlar

b[0:2, 0:3]


# Fancy Index

import numpy as np

v = np.arange(0, 30, 3)                                  # Sayı aralığı (2.yazılan dahil değil)ve kaçar artacağı verilir.
v[1]
v[4]


catch = [1, 2 ,4]                                        # Index değerleri
v[catch]                                                 # Listenin içindeki index değerlerini getirir.



# NumPy' da Koşullu İşlemler

f = np.array([1, 2, 3, 4, 5])

# Klasik döngü ile 3ten küçükleri bulma

ab = []
for i in f:
    if i<3:
        ab.append(i)
ab

# NumPy ile

f = np.array([1, 2, 3, 4, 5])

f < 3                                          # array in bütün elemanlarıyla denedi ve küçüklere True, büyük olanlara False

f[f < 3]
f[f <= 3]
f[f != 3]
f[f == 3]

k = f[f < 3]


# Matematiksel İşlemler

import numpy as np

d = np.array([1, 2, 3, 4, 5])

d / 5
d * 3
d * 5 / 10
d ** 2
d - 1


np.subtract(d, 1)                                  # Çıkarma
np.add(d, 1)                                       # Toplama
np.mean(d)                                         # Ortalama
np.sum(d)                                          # Hepsinin toplamı
np.min(d)
np.max(d)
np.var(d)                                          # Varyans almak için

d = np.subtract(d, 1)


# NumPy ile İki Bilinmeyenli Denklem Çözümü

# 5*x*0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])                                 # İlk yazılan 1.elemanın (x0) katsayılarıdır, 2.yazılan 2.elemanın(x1) katsayılarıdır.
b = np.array([12, 10])

np.linalg.solve(a, b)




