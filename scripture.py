# load_pairs()
# load_verses()

import json


def save_json(file_name, content):
    with open(file_name, 'w') as file:
        json.dump(content, file)


def open_json(file_name):
    with open(file_name, 'r') as file:
        content = json.load(file)
    return content


class Scripture:
    def __init__(self):
        self.pairs = open_json('structured_data/pairs.json')
        self.book = open_json('structured_data/book of mormon.json')
        with open('The Book Of Mormon.txt', 'r') as file:
            self.content = file.readlines()

    def load_scripture(self, book: str, chapter: int, verse: int) -> str:
        """
        Finds verse content by book, chapter, verse in json file and return it.

        :param book: use .pairs to know which book to use (the correct spelling)
        :param chapter: A chapter number from the book
        :param verse: A verse number from the chapter
        :return: verse from book, chapter, verse
        """
        return self.book[self.pairs[book.lower()]][str(chapter)][verse]

    def get_scripture_group(self, book: str, chapter: int, start_verse: int, end_verse: int) -> list:
        """
        Passes the variables to load_scripture and appends it to list to be returned as list of verses.

        :param book: use .pairs to know which book to use (the correct spelling)
        :param chapter: A chapter number from the book
        :param start_verse: A starting verse number from the chapter
        :param end_verse: An ending verse number from the same chapter
        :return: a list of verses from same chapter and book
        """
        return [self.load_scripture(book, chapter, verse) for verse in range(start_verse, end_verse + 1)]

    def print_group(self, book: str, chapter: int, start_verse: int, end_verse: int, html=False) -> None:
        """
        Passes the variables to get_scripture_group to be printed as html for website viewing or as plain text.

        :param book: use .pairs to know which book to use (the correct spelling)
        :param chapter: A chapter number from the book
        :param start_verse: A starting verse number from the chapter
        :param end_verse: An ending verse number from the same chapter
        :param html: if true, print as html, otherwise print as text
        """
        a_list = self.get_scripture_group(book, chapter, start_verse, end_verse)
        verse = start_verse
        if html:
            for each in a_list:
                print('<div>')
                print(f'<p>{book} {chapter}:{verse}</p>')
                print(f'<p>{each}</p>')
                print('</div>')
                verse += 1
        else:
            for each in a_list:
                print(f'{book} {chapter}:{verse}')
                print(each)
                verse += 1

    def print_scriptures(self, book: str, scriptures: list, html=False) -> None:
        """
        Shortcut to print_group by passing in print_group for each of multiple chapter:verse from same book in a list.

        :param book: use .pairs to know which book to use (the correct spelling)
        :param scriptures: a list of formatted string as 'chapter:start_verse-end_verse' (all numbers).
        :param html: if true then print as html otherwise print as plain
        """
        for each_group in scriptures:
            chapter, verses = each_group.split(':')
            start_verse, end_verse = verses.split('-')
            self.print_group(book, int(chapter), int(start_verse), int(end_verse), html)
