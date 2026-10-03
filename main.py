import json




books = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "available": True
    },
    {
        "id": 2,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True
    },
    {
        "id": 3,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "year": 1999,
        "available": True
    }
]




members = [
    {
        "id": 1,
        "name": "Ali",
        "email": "ali@example.com"
    }
]




def save_data():
    data = {
        "books": books,
        "members": members
    }

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully.")


def load_data():
    global books, members

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        books = data["books"]
        members = data["members"]

        print("Data loaded successfully.")

    except FileNotFoundError:
        print("No saved data found. Starting with default data.")



def show_books():
    print("\n--- Books ---")

    for book in books:
        print("ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Year:", book["year"])

        if book["available"]:
            print("Available: Yes")
        else:
            print("Available: No")

        print()


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter publication year: "))

    new_id = len(books) + 1

    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }

    books.append(new_book)

    print("Book added successfully.")


def remove_book(book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("Book removed successfully.")
            return

    print("Book not found.")


def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            print("\nBook found:")
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Year:", book["year"])

            if book["available"]:
                print("Available: Yes")
            else:
                print("Available: No")

            return book

    print("Book not found.")
    return None



def show_members():
    print("\n--- Members ---")

    for member in members:
        print("ID:", member["id"])
        print("Name:", member["name"])
        print("Email:", member["email"])
        print()


def add_member():
    name = input("Enter member name: ")
    email = input("Enter member email: ")

    new_id = len(members) + 1

    new_member = {
        "id": new_id,
        "name": name,
        "email": email
    }

    members.append(new_member)

    print("Member added successfully.")


def borrow_book(member_id, book_id):
    for member in members:
        if member["id"] == member_id:

            for book in books:
                if book["id"] == book_id:

                    if book["available"]:
                        book["available"] = False
                        print("Book borrowed successfully.")
                    else:
                        print("Book is not available.")

                    return

            print("Book not found.")
            return

    print("Member not found.")


def return_book(book_id):
    for book in books:
        if book["id"] == book_id:

            if not book["available"]:
                book["available"] = True
                print("Book returned successfully.")
            else:
                print("Book is already available.")

            return

    print("Book not found.")

def show_statistics():
    total_books = len(books)

    available_books = 0
    borrowed_books = 0

    for book in books:
        if book["available"]:
            available_books += 1
        else:
            borrowed_books += 1

    total_members = len(members)

    print("\n========================")
    print("      STATISTICS")
    print("========================")

    print("Total books:", total_books)
    print("Available books:", available_books)
    print("Borrowed books:", borrowed_books)
    print("Total members:", total_members)


load_data()



while True:

    print("\n--- Library Management System ---")

    print("1. Show books")
    print("2. Add book")
    print("3. Remove book")
    print("4. Search book")
    print("5. Show members")
    print("6. Add member")
    print("7. Borrow book")
    print("8. Return book")
    print("9. Save data")
    print("10. Statistics")
    print("11. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        show_books()


    elif choice == "2":
        add_book()


    elif choice == "3":
        book_id = int(input("Enter book ID: "))
        remove_book(book_id)


    elif choice == "4":
        book_id = int(input("Enter book ID: "))
        find_book(book_id)


    elif choice == "5":
        show_members()


    elif choice == "6":
        add_member()


    elif choice == "7":
        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
        borrow_book(member_id, book_id)


    elif choice == "8":
        book_id = int(input("Enter book ID: "))
        return_book(book_id)


    elif choice == "9":
        save_data()
        
    elif choice == "10":
        show_statistics()



    elif choice == "11":
        print("Goodbye!")
        break


    else:
        print("Invalid choice.")
