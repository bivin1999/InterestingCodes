cipher=input().strip()
cipher=cipher[::-1]
plain=""
for c in cipher:
    plain+=chr(((ord(c)-68)%26)+65)
print(plain)