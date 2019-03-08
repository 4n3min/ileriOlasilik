# PigeonHole Odevi4 mart 2019



'''
Bir torbada 10 Kırmızı, 10 mavi, 10 yeşil top olsun. Bu torbadan rastgele toplar seçiliyor.
4 tane topun ayni renk olmasi için en az kac top seçilmelidir?
'''
print(__doc__)
import math

renk=3 # toplam renk adedi(yuva)
kalem=3
k= kalem+1 # seçilecek kalem sayısı Guvercin yuvası ilkesine gore 3+1 olacaktır.

enAzTop = math.ceil((renk*kalem+1)/renk)
print('Seçilmesi gereken top adeti :' ,enAzTop)

