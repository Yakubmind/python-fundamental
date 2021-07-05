"""
Tipe data Dictionary, menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
Dictionary = Kamus
"""

kamus = {}

kamus['anak'] = 'son'
kamus['ibu'] = 'mother'
kamus['bapak'] = 'father'
kamus ['istri']='wife'
kamus['mother']='ibu'

print (kamus)
print(kamus['anak'])
print(kamus['mother'])

print('data ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal':'2021-07-05',
    'driver_list': [
        {'nama': 'eko', 'jarak': 10},
        {'nama': 'dwi', 'jarak': 30},
        {'nama': 'tri', 'jarak': 100},
        {'nama': 'catur', 'jarak': 1000}
    ]

}

print(data_dari_server_gojek)
print(f"Driver di sekitar sini{data_dari_server_gojek['driver_list']}")
print(f"Driver #1{data_dari_server_gojek['driver_list'][0]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']}meter")


