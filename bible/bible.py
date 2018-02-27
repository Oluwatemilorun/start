import json
import sys

def init_bible(username="your") :
    print("opening " + username + " bible")

    bible_json = open("bible/bible.json", 'r')

    bible = json.load(bible_json)

    load_books(bible)

def load_books(bible) :
    sn = 1

    print("\n Old Testament \n")
    for books in bible :
        book_name = books["name"]
        book_abbrev = books["abbrev"]

        if sn <= 39 :
            print(" ~ " + str(sn) + " --- " + book_name + " (" + book_abbrev + ") --- ")

        if sn == 40 :
            print("\n New Testament \n")

        if sn >= 40 :
            print(" ~ " + str(sn) + " --- " + book_name + " (" + book_abbrev + ") --- ")

        sn = sn + 1
    
    is_correct = False
    while is_correct == False :
        book = input("Select Book (Input Name or Abbreviation) >")
        for books in bible :
            if books["name"] == book or books["abbrev"] == book :
                load_chapters(bible, book)
                is_correct = True
                break

        if is_correct == False :
            print("\n" + book + " is not a book name or abbreviation")


def load_chapters(bible, book) :
    for books in bible :
        if books["name"] == book or books["abbrev"] == book :
            n_chapter = len(books["chapters"])
            i = 1

            while i <= n_chapter :
                print("[" + str(i) + "]", end=" ")

                i = i + 1
            
            chapter = input("\n Select chapter >")

            while int(chapter) > n_chapter :
                print("\n" + books["name"] + " does not have a chapter " + chapter)
                chapter = input("Select chapter >")
            
            read_bible(bible, book, chapter)

            break
    
def read_bible(bible, book, chapter) :
    print("\n" + book + ", chapter - " + str(chapter) + "\n")
    for books in bible :
        if books["name"] == book or books["abbrev"] == book :
            index = 1

            while index < len(books["chapters"][int(chapter) - 1]) :
                print(str(index) + ". " + books["chapters"][int(chapter) - 1][index] + "\n")

                index = index + 1

            break
    
    load_options(bible, book, chapter)

def load_options(bible, book, chapter) :
    print("\n [1] Previous Chapter [2] Next Chapter [3] Exit ")
    option = input("Select option >")

    if option == '1' :
        if chapter == 1 :
            print("You are on the first chapter \n")
            load_options(bible, book, chapter)
        else:
            read_bible(bible, book, int(chapter) - 1)
    elif option == '2' :
        read_bible(bible, book, int(chapter) + 1)
    elif option == '3' :
        load_books(bible)
    else :
        print("Not an option \n")
        load_options(bible, book, chapter)