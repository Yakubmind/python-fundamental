#tipe data skalar / sederhana
anak1="pujo"
anak2="eko"
anak3="poniman"
anak4="paijo"

print(anak1)
print(anak2)
print(anak3)
print(anak4)

#tipe data list/daftar/array
anak = ['pujo', 'eko', 'poniman', 'paijo']
print(anak)
anak.append('putro')
print(anak)

#sapa anak ke 2
print(f'Hai {anak[1]}!')

#sapa semua anak - cara1
for a in anak:
    print(f'Hai {a}!')

#sapa semua ana - cara ribet
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}')
