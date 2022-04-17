
import pickle
class Tbook:
    author = "?"
    title = ""
    count = 0


m = open ( "books.TXT" , 'rb')
bb = pickle.load( m )
print(bb.author, bb.title, bb.count , sep = ", " )
m.close()
