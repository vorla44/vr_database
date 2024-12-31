import sqlite3

# Luo yhteys tietokantaan (tai luo uusi tietokanta, jos sitä ei ole olemassa)
conn = sqlite3.connect('kuvat.db')
cursor = conn.cursor()

# Luo taulu, jos sitä ei ole jo olemassa
cursor.execute('''
CREATE TABLE IF NOT EXISTS Kuvat (
    id INTEGER PRIMARY KEY,
    kuva BLOB, 
    info TEXT,
    vuosi TEXT,
    url TEXT NOT NULL
)
''')

# Lue kuva tiedostosta
with open('../valokuvia/2005-2022/2011/2011-07-31/elli.jpg', 'rb') as file:
    kuva_data = file.read()
    info ="Aava, Vilja ja Elli kastetilaisuudessa"
    vuosi = "2011"
    url = "d:/Gigantti Cloud/valokuvia/2005-2022/2011/2011-07-31/elli.jpg"


# Lisää kuva tietokantaan
cursor.execute('INSERT INTO Kuvat (kuva, info, vuosi, url) VALUES (?, ?, ?, ?)', (kuva_data, info, vuosi, url))

# Tallenna muutokset ja sulje yhteys
conn.commit()
conn.close()

print("Kuva lisätty onnistuneesti!")
