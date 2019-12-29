# TipeData: Dictionary adalah sebuah struktur data asiosiatif atau menggunakan mapping
# format : member1 = {key:value,key:value}

# CONTOH 1:
print("=" * 5, "CONTOH 1: Umum", "=" * 5)
member1 = {"ID":101,
           "Nama":"Rizky Khapidsyah",
           "Pekerjaan":"Manusia",
           "Status Member":"Gold"}

print(member1)
print("\n")

# Cara Untuk Mengakses Data Di Dictionary
print(member1["ID"])
print(member1["Nama"])
print(member1["Pekerjaan"])
print(member1["Status Member"])

# Cara Untuk Mengakses Key nya saja
print(member1.keys())

# Cara Untuk Mengakses Value nya saja
print(member1.values())

# Cara Untuk Mengakses Semuanya (Key dan Valuenya)
print(member1) # atau :
print(member1.items())

print('\n')

# CONTOH 2:
print("=" * 5, "CONTOH 2: Member List", "=" * 5)
member2 = {"ID":102,
           "Nama":"Bambang Aditya",
           "Pekerjaan":"Manusia",
           "Status Member":"Silver"}


member3 = {"ID":103,
           "Nama":"Dwi Pradana",
           "Pekerjaan":"Manusia",
           "Status Member":"Gold"}

daftarMember = {102:member2, 103:member3}

print(daftarMember[102])
print(daftarMember[103])

