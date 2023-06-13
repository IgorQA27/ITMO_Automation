class Buttom:

    def __init__(self, text, link):
        self.text = text
        self.link = link

# Создадим элементы класса
home = Buttom('Домой', '/home')
catalog_msk = Buttom('Каталог', '/msk/catalog')

# Получаем доступ к атрибутам
print(home.text)
print('Кнопка' + home.text + 'имеет ссылку' + home.link)

print('/n')

print(catalog_msk.text)
print('Кнопка' + catalog_msk.text + 'имеет ссылку' + catalog_msk.link)


class ButtomTwo:

    def __init__(self, text, link, loc):
        self. text = text
        self. link = link
        self. loc = loc


    def click(self):
        return "клик по лолкатору - {}".format(self.loc)


# Создаем экземпляры класса
home_two = ButtomTwo('Домой', '/home', 'button#home')

# Вызываем метод
print(home_two.click())


class Input:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text
search = Input('jk', '')

print(search.loc)

class Buttom:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text
click = Buttom('', '')

print(search.text)

class Title:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
read = Title('', '')

print(search.loc)

class Page:
    def __init__(self, url):
        self.url = url


    def get(self):
        print(self.url)

home = Page('https://www.google.com/')
home.get()

