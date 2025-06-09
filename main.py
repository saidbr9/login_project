from auth import login 

print("=== LOGIN SEDERHANA ===")
user = input("Username: ")
pw = input("password: ")

if login(user, pw):
    print(f"Login berhasil! Selamat datang, {user}.")
else:
    print("Login gagal! Username atau password salah.")

print("Fitur logout aktif")
