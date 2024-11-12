import uuid

dosyaAdi = uuid.uuid4()
dosya = str(dosyaAdi)

print(dosyaAdi)

for i in range(1,10):
    print(uuid.uuid4())