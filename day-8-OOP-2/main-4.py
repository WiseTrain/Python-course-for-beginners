from ProductV2 import Book, Clothing, Electronics

if __name__ == "__main__":

    book1 = Book("Dune", 5.99, 5, "F.Herbert")
    book1.display()
    # setter
    book1.set_price(6.00)
    book1.display()
    
    book2 = Book("Nine Princes in Amber", 7.99, 3, "R.Zelazny")
    book2.display()

    electronics1 = Electronics("AOC 27G2SE 27\" FHD 165Hz Gaming Monitor", 359.00, 3, "AOC")
    electronics1.display()

    dress1 = Clothing("GATHERED LINEN BLEND DRESS", 119.00, 3, "S/M")
    dress1.display()

    # # https://stackoverflow.com/questions/1006169/how-do-i-look-inside-a-python-object
    # # how to display a structure of the class? 
    # print(type(dress1))
    # print(dir(dress1))
    # print(getattr(dress1, "quantity"))
    # print(callable(dress1.display))
