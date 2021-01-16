searched_book = input()
book = input()

found_book = True
book_count =0

while book != searched_book:
    if book == "No More Books":
        found_book = False
        break
    book_count +=1
    book = input()

if found_book:
    print(f"You checked {book_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")