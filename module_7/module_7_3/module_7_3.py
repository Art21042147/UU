class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for chars in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(chars, '')
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = words.count(word)
        return result


finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())  # Все слова
print(finder1.find('TEXT'))  # 3 слово по счёту
print(finder1.count('teXT'))  # 4 слова teXT в тексте всего

finder2 = WordsFinder('Lewis Carroll - Jabberwocky.txt',
                      'Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words())
print(finder2.find('the'))
print(finder2.count('the'))
