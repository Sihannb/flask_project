with open("requirements.txt", "rb") as f:
    content = f.read()

# enlever BOM
content = content.lstrip(b'\xef\xbb\xbf')

with open("requirements.txt", "wb") as f:
    f.write(content)
print("Fichier nettoyé ✅")