Bu yazdığım kod bir dosyadan veri okuyup işleyen bir programdır. Temelinde, MEMORY dediğimiz programa dahil 8KD (kilo data) hafızaya veri yazıp ekrana çıktı alma ve kullanıcıdan giriş alma gibi fonksiyonlar vardır. Syntax yapısı şöyledir:
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
