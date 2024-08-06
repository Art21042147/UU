calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [words.lower() for words in list_to_search]


print(string_info('Dudhsagar'))
print(string_info('Tiwanaku'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('parade', ['paradigma', 'separating', 'prepare']))
print(calls)
