import pickle
class Tbook:
    author = "?"
    title = ""
    count = 0
b = Tbook()
Fout = open ("books.TXT", "wb")
b.title = "MyMy"
b.author = "Tyrgenev I.C"
b.count = "200"
pickle.dump(b, Fout)
Fout.close()
