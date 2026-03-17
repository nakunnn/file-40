import time
import sys
import os
import random
from getpass import getpass

# Kode Warna
G = '\033[92m'
R = '\033[91m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def ketik(teks, delay=0.03):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# 1. Animasi Loading Awal
clear()
ketik(f"{C}[*] Memulai inisialisasi modul lokal...{W}")
time.sleep(0.5)
ketik(f"{C}[*] Mengecek status server database... {G}ONLINE{W}")
time.sleep(1)

# 2. Sistem Login
clear()
print(f"{R}======================================{W}")
print(f"{R}       LOGIN KREDENSIAL VIP           {W}")
print(f"{R}======================================{W}")

user = input(f"{Y}Username : {W}")
# getpass bikin ketikan password nggak kelihatan di layar
pw = getpass(f"{Y}Password : {W}") 

ketik(f"\n{C}[*] Memverifikasi data ke server...{W}", 0.05)
time.sleep(1.5)

# Cek Password (Passwordnya: VIP2026)
if pw != "VIP2026":
    print(f"{R}[!] AKSES DITOLAK: Password Salah! Akun dicatat.{W}")
    sys.exit()

print(f"{G}[+] AKSES DITERIMA. Selamat datang, {user}!{W}")
time.sleep(1.5)

# 3. Main Menu
clear()
print(f"{R}======================================{W}")
print(f"{R}      [ MASUKKAN ASCII ART DI SINI ]  {W}")
print(f"{R}======================================{W}")
print(f"{G}1. Inject Auto Headshot 100%{W}")
print(f"{G}2. Bypass Anti-Ban Server{W}")
print(f"{G}3. Exit{W}")
print(f"{R}======================================{W}")

pilih = input(f"{Y}Pilih menu (1/2/3): {W}")

if pilih == "1" or pilih == "2":
    ketik(f"\n{C}[*] Mempersiapkan injeksi payload...{W}")
    time.sleep(1)
    
    print(f"{G}[+] Target 'com.dts.freefireth' locked (PID: {random.randint(1000, 9999)}){W}")
    time.sleep(1)

    print(f"{Y}[*] Injecting parameters...{W}")
    time.sleep(1)

    # Efek hex code acak
    for _ in range(25):
        hex_val = ''.join(random.choices('0123456789ABCDEF', k=8))
        print(f"{G}0x{hex_val} -> WRITE_MEMORY_SUCCESS{W}")
        time.sleep(0.04)

    print(f"\n{C}[*] Finalisasi proses...{W}")
    time.sleep(1)
    print(f"\n{Y}--------------------------------------")
    print(" STATUS: ACTIVATED SUCCESSFULLY")
    print(f"--------------------------------------{W}\n")
else:
    print(f"{R}[!] Keluar dari program.{W}")
    sys.exit()
