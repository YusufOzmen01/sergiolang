# Bu yazdığım kod bir dosyadan veri okuyup işleyen bir programdır. Temelinde, MEMORY dediğimiz programa dahil 8KD (kilo data) hafızaya veri yazıp ekrana çıktı alma ve kullanıcıdan giriş alma gibi fonksiyonlar vardır. Syntax yapısı şöyledir:
===================================
```
set <veri> : veri etiketinin olduğu kısma tamsayı ve yazı girip TMPMEMORY'ye kaydedilir.

write <address> : address etiketinin olduğu kısma 8KD'lik kısımdan (0-8192) bir adres girilerek TMPMEMORY asıl MEMORY'ye yazılır.

abs <addr1> <addr2> <out> : addr1 ve addr2 adreslerindeki sayıları toplayarak out adresine yazar.

sub <addr1> <addr2> <out> : addr1 ve addr2 adreslerindeki sayıları çıkartarak out adresine yazar.

div <addr1> <addr2> <out> : addr1 ve addr2 adreslerindeki sayıları bölerek out adresine yazar.

mul <addr1> <addr2> <out> : addr1 ve addr2 adreslerindeki sayıları çarparak out adresine yazar.

absStr <addr1> <addr2> <out> : addr1 ve addr2 adreslerindeki yazıları toplayarak out adresine yazar.

print <address> : address etiketindeki adreste bulunan değeri çıktılar.

inp <txt> <out> : txt etiketindeki değeri çıktılayarak kullanıcıdan giriş bekler. Giriş geldiğinde out adresine yazar.

dump <target> : target etiketlerine MEMORY'nin kaydedilmesini istediğiniz konumu yazın. 

load <target> : target kısmına önceden kaydediğiniz MEMORY'nin konumunu yazın ve o MEMORY dosyası şu anki projenize yüklenecek.
```

**Programı çalıştırırken main.py dosyasını çalıştırın ve çalıştırılacak dosyanın ismini yazın. Örneğin test.semu. Aşağıda örnek bir program verilmiştir.**
==========================================
**test.semu**
```
set Hello, World!
write 0
print 0
set Ismin Nedir? :
write 1
inp 2 1
print 2
set 5
write 3
set 10
write 4
abs 3 4 5
sub 4 3 6
div 4 3 7
mul 3 4 8
print 5
print 6
print 7
print 8
dump mem.hex
load mem.hex
```
