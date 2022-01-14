import json

# list
names = ["Python", "Java", "JS", "Swift", "C#"]
# dictionary
book = {
    "name": "Python",
    "price": 500,
    "author": "Paul"
}
# dictionaries inside a list
books = [
    {
        "name": "Python",
        "price": 500,
        "author": "Paul"
    },
    {
        "name": "Java",
        "price": 550,
        "author": "John"
    }
]


# 自訂類別
class Book:

    def __init__(self, name, price, author):
        self.name = name
        self.price = price
        self.author = author


# list轉JSON字串
namesJsonStr = json.dumps(names)
print(f"namesJsonStr type: {type(namesJsonStr)}\nnamesJsonStr: {namesJsonStr}")
# JSON字串轉list
nameList = json.loads(namesJsonStr)
print(f"nameList type: {type(nameList)}\nnameList: {nameList}")
print()

# dictionary轉JSON字串
bookJsonStr = json.dumps(book)
print(f"bookJsonStr type: {type(bookJsonStr)}\nbookJsonStr: {bookJsonStr}")
# JSON字串轉dictionary
bookDic = json.loads(bookJsonStr)
print(f"bookDic type: {type(bookDic)}\nbookDic: {bookDic}")
print()

# list(含有多個dictionary)轉JSON字串
booksJsonStr = json.dumps(books)
print(f"type: {type(booksJsonStr)}\nJSON String: {booksJsonStr}")
# JSON字串轉list(含有多個dictionary)
bookList = json.loads(booksJsonStr)
print(f"bookList type: {type(bookList)}\nbookList: {bookList}")
print()

# 自訂物件先轉dictionary再轉JSON字串
bookJsonStr = json.dumps(Book("Python", 500, "Paul").__dict__)
print(f"type: {type(bookJsonStr)}\nJSON String: {bookJsonStr}")
# JSON字串轉dictionary
bookDic = json.loads(bookJsonStr)
print(f"bookDic type: {type(bookDic)}\nbookDic: {bookDic}")
infoList = bookDic['name']  # put the 'key_name'
print(infoList)
