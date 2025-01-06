class WordsFinder:
    def __init__(self, name_file):
        self.name_file = name_file
    def get_all_words(self):
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = []
        with open(self.name_file, encoding = 'utf-8') as file:
            text = file.read().lower()
            for char in punc:
                text = text.replace(char, '')
            all_words = text.split()
        return all_words

    def find(self, word):
        words = self.get_all_words()
        result = {self.name_file: words.index(word.lower())} if word.lower() in words else None
        return result

    def count(self, word):
        words = self.get_all_words()
        result = {self.name_file: words.index(word.lower())}
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('text'))



