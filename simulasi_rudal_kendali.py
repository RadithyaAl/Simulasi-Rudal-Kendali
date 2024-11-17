"""
Deskripsi:
Program untuk mensimulasikan rudal kendali. Rudal bergerak menuju lokasi target
yang telah diinputkan diawal program.

batasan:
- sistem koordinat hanya berlaku untuk kuadran 1.
- kecepatan target diasumsikan selalu bernilai positif.
- kecepatan maksimum rudal adalah 300 meter per sekon (jika kecepatan target melebihi kecepatan maksimum rudal, maka rudal tidak akan bisa mencapai target)
- sudut elevasi target diasumsikan selalu bernilai antara 0 sampai 90 derajat.

Kamus : 
real_time = float

posisi_rudal_X = float
posisi_rudal_Y = float

posisi_awal_rudal_X = float
posisi_awal_rudal_Y = float

kecepatan_awal_rudal_X = float
kecepatan_awal_rudal_Y = float
net_kecepatan_awal_rudal = float

percepatan_rudal_X = integer
percepatan_rudal_Y = integer
net_percepatan_rudal = float

waktu_rudal_X = float
waktu_rudal_Y = float

kecepatan_rudal_X = float
kecepatan_rudal_Y = float
net_kecepatan_rudal = float


sudut_elevasi_target = float


posisi_awal_target_X = float
posisi_awal_target_Y = float

posisi_target_X = float
posisi_target_Y = float

kecepatan_target = float
sudut_elevasi_target = float

kecepatan_target_X = float
kecepatan_target_Y = float

waktu_target = float

jarak_rudal = float
jarak_target = float

"""




import math
import time
import os



# membersihkan terminal
os.system('cls')  

real_time = 0
# data-data rudal

posisi_rudal_X = 0
posisi_rudal_Y = 0

posisi_awal_rudal_X = 0
posisi_awal_rudal_Y = 0

kecepatan_awal_rudal_X = 0
kecepatan_awal_rudal_Y = 0
net_kecepatan_awal_rudal = 10

percepatan_rudal_X = 10
percepatan_rudal_Y = 10

waktu_rudal_X = 0
waktu_rudal_Y = 0

kecepatan_rudal_X = 0
kecepatan_rudal_Y = 0
net_kecepatan_rudal = 0



# data2 target


posisi_awal_target_X = int(input("Masukkan posisi target dalam sumbu X (meter) : "))
posisi_awal_target_Y = int(input("Masukkan posisi target pada sumbu Y (meter ) : "))

posisi_target_X = posisi_awal_target_X
posisi_target_Y = posisi_awal_target_Y

kecepatan_target = int(input("Masukkan kecepatan target (m/s) : "))
sudut_elevasi_target = int(input("Masukkan sudut elevasi target terhadap sumbu X (derajat) : "))
sudut_elevasi_target = (sudut_elevasi_target * 2 * math.pi) / 360

kecepatan_target_X = kecepatan_target * math.cos(sudut_elevasi_target)
kecepatan_target_Y = kecepatan_target * math.sin(sudut_elevasi_target)

waktu_target = 0

jarak_rudal = math.sqrt(posisi_rudal_X**2 + posisi_rudal_Y**2)
jarak_target = math.sqrt(posisi_target_X**2 + posisi_target_Y)

# fungsi untuk rudal
def koordinat_rudal_X(posisi_rudal_X, posisi_awal_rudal_X, waktu_rudal_X, percepatan_rudal_X, net_kecepatan_awal_rudal, sudut_elevasi_rudal):
    if percepatan_rudal_X != 0:
        posisi_rudal_X = posisi_awal_rudal_X + (net_kecepatan_awal_rudal * math.cos(sudut_elevasi_rudal) * waktu_rudal_X + 0.5 * percepatan_rudal_X * (waktu_rudal_X**2))
    elif percepatan_rudal_X == 0:
        posisi_rudal_X =posisi_awal_rudal_X + net_kecepatan_rudal * math.cos(sudut_elevasi_rudal) * waktu_rudal_X

    return posisi_rudal_X

def koordinat_rudal_Y(posisi_rudal_Y, posisi_awal_rudal_Y, waktu_rudal_Y, percepatan_rudal_Y, net_kecepatan_awal_rudal, sudut_elevasi_rudal):

    if percepatan_rudal_Y != 0:
        posisi_rudal_Y = posisi_awal_rudal_Y + (net_kecepatan_awal_rudal * math.sin(sudut_elevasi_rudal) * waktu_rudal_Y + 0.5 * percepatan_rudal_Y * (waktu_rudal_Y**2))
    elif percepatan_rudal_Y == 0:
        posisi_rudal_Y =posisi_awal_rudal_Y + net_kecepatan_rudal * math.sin(sudut_elevasi_rudal) * waktu_rudal_Y


    return posisi_rudal_Y




# fungsi untuk target

def koordinat_target_X(posisi_target_X, posisi_awal_target_X, kecepatan_target_X, waktu_target):
    posisi_target_X = posisi_awal_target_X + kecepatan_target_X * waktu_target

    return posisi_target_X

def koordinat_target_Y(posisi_target_Y, posisi_awal_target_Y, kecepatan_target_Y, waktu_target):
    posisi_target_Y = posisi_awal_target_Y + kecepatan_target_Y * waktu_target

    return posisi_target_Y



os.system('cls')
for i in range(5, 0, -1):
    print(f"Rudal meluncur dalam {i} detik.")
    time.sleep(0.8)
    os.system('cls')
print("Meluncurrrrrrr........")
time.sleep(1.5)




# fungsi utama
real_time = 0

jarak = math.sqrt((posisi_target_X-posisi_rudal_X)**2 + (posisi_target_Y - posisi_rudal_Y)**2)

while math.sqrt(posisi_rudal_X**2 + posisi_rudal_Y**2) <= math.sqrt(posisi_target_X**2 + posisi_target_Y**2) :
    if posisi_target_X != 0:
        sudut_elevasi_rudal = math.atan(posisi_target_Y / posisi_target_X)
    elif posisi_target_X == 0:
        sudut_elevasi_rudal = 0.5 * math.pi
    
    if posisi_rudal_X <= posisi_target_X :
        posisi_rudal_X = koordinat_rudal_X(posisi_rudal_X, posisi_awal_rudal_X, waktu_rudal_X, percepatan_rudal_X, kecepatan_awal_rudal_X, sudut_elevasi_rudal)

    if posisi_rudal_Y <= posisi_target_Y :
        posisi_rudal_Y = koordinat_rudal_Y(posisi_rudal_Y, posisi_awal_rudal_Y, waktu_rudal_Y, percepatan_rudal_Y, kecepatan_awal_rudal_Y, sudut_elevasi_rudal)
        

    posisi_target_X = koordinat_target_X(posisi_target_X, posisi_awal_target_X, kecepatan_target_X, waktu_target)
    posisi_target_Y = koordinat_target_Y(posisi_target_Y, posisi_awal_target_Y, kecepatan_target_Y, waktu_target)

    posisi_rudal_X = round(posisi_rudal_X, 2)
    posisi_rudal_Y = round(posisi_rudal_Y, 2)
    posisi_target_X = round(posisi_target_X, 2)
    posisi_target_Y = round(posisi_target_Y, 2)
    


    
    

    if kecepatan_rudal_X < 300:
        kecepatan_rudal_X = net_kecepatan_awal_rudal * math.cos(sudut_elevasi_rudal) + percepatan_rudal_X * waktu_rudal_X
        if kecepatan_rudal_X >= 300:
            percepatan_rudal_X = 0
            waktu_rudal_X = 0
            posisi_awal_rudal_X = posisi_rudal_X

    if kecepatan_rudal_Y < 300:
        kecepatan_rudal_Y = net_kecepatan_awal_rudal * math.sin(sudut_elevasi_rudal) + percepatan_rudal_Y * waktu_rudal_Y
        if kecepatan_rudal_Y >= 300:
            percepatan_rudal_Y = 0
            waktu_rudal_Y = 0
            posisi_awal_rudal_Y = posisi_rudal_Y

    net_kecepatan_rudal = round(math.sqrt(kecepatan_rudal_X**2 + kecepatan_awal_rudal_Y**2), 2)
    net_percepatan_rudal = round(math.sqrt(percepatan_rudal_X**2 + percepatan_rudal_Y**2), 2)
    jarak_rudal = round(math.sqrt(posisi_rudal_X**2 + posisi_rudal_Y**2), 2)
    jarak_target = round(math.sqrt(posisi_target_X**2 + posisi_target_Y), 2)

    waktu_rudal_X += 0.3
    waktu_rudal_Y += 0.3
    waktu_target += 0.3
    real_time += 0.3

    print("=============================================================")
    print(f"Koordinat Rudal ({posisi_rudal_X}, {posisi_rudal_Y})")
    print(f"Koordinat Target ({posisi_target_X}, {posisi_target_Y})")
    print(f"Kecepatan Rudal {net_kecepatan_rudal} m/s")
    print(f"Percepatan Rudal {net_percepatan_rudal} m/s2")
    print(f"Kecepatan Target {kecepatan_target} m/s")
    print(f"Waktu : {round(real_time)} detik")
    print("=============================================================")
    time.sleep(0.1)
    os.system('cls')

print("=============================================================")
print(f"Target berhasil dimusnahkan di koordinat ({posisi_rudal_X}, {posisi_rudal_Y})")
print(f"kecepatan maksimum rudal {net_kecepatan_rudal} m/s")
print(f"kecepatan target {kecepatan_target} m/s")
print(f"waktu tempuh {round(real_time, 2)} detik")
print(f"jarak tempuh = {jarak_rudal} meter")
print("=============================================================")