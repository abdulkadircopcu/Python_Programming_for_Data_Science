print("Hello World")
print("Hello AI Era")

type("9")

a=9
x="hello ai era"
c=10

a * c
d= a - c
d




###############################################
# Virtual Environment (Sanal Ortam) ve Package Management (Paket Yönetimi)
###############################################

# Sanal ortamların listelenmesi:
# conda env list

# Sanal ortam oluşturma:
# conda create -n myenv         myenv=env ismi

# Sanal ortama geçiş yapmak için:
# conda activate myenv          myenv=env ismi
# conda deactivate              aktiflikten çıkarmak için

# Yüklü paketlerin listelenmesi:
# conda list

# Paket yüklemek için:
# conda install paket_ismi

# Birden fazla paket yüklemek için:
# conda install paket_ismi paket_ismi numpy scipy pandas (sadece boşluk)

# Paket silme:
# conda remove paket_ismi numpy

# Sürüme göre indirmek için:
# conda install paket_ismi=sürüm numarası   numpy=1.20.1                   pipte == kullanılırken condada = kullanılır.

# Güncellemek için:
# conda upgrade paket_ismi numpy

# Tüm paketlerin güncellenmesi:
# conda upgrade -all

# pip= pypi (python package index) Paket yönetim aracıdır.

# Paket yükleme:
# pip install paket_ismi

# Sürüme göre yüklemek için:
# pip install paket_ismi==sürüm_numarası                    pandas==1.2.1

# Paketlerin sürümlerini dışa aktarmak için:
# conda env export > environment.yaml

# Environment silmek için:
# conda env remove -n env_adi                            conda env remove -n deneme_env

# Var olan ortamı tekrar oluşturmak için:
# conda env create -f environment.yaml
# environment.yaml dosyası paketlerin sürümlerini gösterdiği için olması gerekir. Eski environmenti geri getirmeye yarar.



