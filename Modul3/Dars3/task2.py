def text_generator(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        for i in text:
            yield i


for letter in text_generator('../Files/test.txt'):
    print(letter)
