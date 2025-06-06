akun_tersimpan = {
    "said":"12345",
    "admin": "admin123",
    "budi": "password",
    "ricky": "jawa"
}

def login(username, password):
    if username in akun_tersimpan:
        if akun_tersimpan[username] == password:
            return True
    return False 
