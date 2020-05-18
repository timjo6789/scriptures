from scripture import Scripture

a = Scripture()
print(a.load_scripture('1st nephi', 3, 7))

# print(a.load_scripture('1st nephi', 2, 2))
# a.print_group('alma', 46, 3, 23)

a.print_scriptures('alma', ['46:3-23', '47:1-36', '48:10-17'])


# do this for the allscripture.txt to get old testament, new testament, pearl of great price and D&C
def load_pair(current_book, file_name):
    """
    Open a scripture file to return key-pair as book-chapter_list_of_total_verses.

    Opens a file with this pattern
    NE1 0:0 verse content
    NE1 0:1 verse content
    NE2 0:0 verse content
    where NE1 is book and 0:0 is chapter:verse

    :param current_book: type in the first book of the txt file
    :param file_name: type in file location of books
    :return: dict pairs of name of book to a list with index as chapter and content as list of verses
    """
    book_chapter_verse = {current_book: {}}
    with open(file_name, 'r') as file:
        current_chapter = 0
        current_verse = 0

        for each in file.readlines():
            try:
                # basically I'm scrapping data from raw txt file into specific variables
                book, chapter_verse = each.split(' ')[0:2]  # example: ['NE1', '0:0']
                chapter, verse = [int(x) for x in chapter_verse.split(':')]  # example [0, 0]

                # also get verse content
                verse_content = ' '.join(each.split(' ')[2:]).strip()
            except ValueError:
                # this skips any invalid line of entry
                continue
            except IndexError:
                # this skips any invalid line of entry
                continue

            # these if statements are simply change-based trigger
            # check book then chapter then verse, this order matters
            # useful for skipping repetitive book, chapter, and verses (if any)

            if current_book != book:
                current_book = book
                book_chapter_verse.setdefault(book, {})

            if current_chapter != chapter:
                current_chapter = chapter

            if current_verse != verse:
                current_verse = verse
                # put verse content directly into chapter list
                book_chapter_verse[current_book].setdefault(current_chapter, [])
                book_chapter_verse[current_book][current_chapter].append(verse_content)

    return book_chapter_verse
