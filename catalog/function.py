import json
from os import path


class JsonC:

    def __init__(self):
        self.filename = 'catalog/data.json'

    def to_file(self, row):
        rows = []
        if path.exists(self.filename):
            with open(self.filename) as file:
                rows = json.loads(file.read())
                row.extend(rows)
                row = row[-5:]
        with open(self.filename, 'w') as file:
            file.write(json.dumps(row))

    def from_file(self):
        if not path.exists(self.filename):
            return None
        with open(self.filename) as file:
            return json.loads(file.read())


class Construct:
    def __init__(self):
        self.part1 = open('catalog/templates/catalog/part1.html').read()
        self.part2 = open('catalog/templates/catalog/part2.html').read()

    def join_html(self, data):
        if data:
            return self.part1 + data + self.part2
        else:
            data = '<p>Данных пока нет, чтобы они появились, пожалуйста, заполните форму на странице контакты.</p>'
            return self.part1 + data + self.part2


def construct_html():
    file_path = path.join('catalog', 'templates', 'catalog', 'messages.html')
    if path.exists('catalog/data.json'):
        with open(file_path, 'w') as file:
            file.write(Construct().join_html(construct_html2()))
    else:
        with open(file_path, 'w') as file:
            file.write(Construct().join_html(None))


def construct_html2():
    html = [
        '<table class="table"><thead><tr><th scope="col">№ записи</th><th scope="col">Имя</th>',
        '<th scope="col">Телефон</th><th scope="col">Почта</th><th scope="col">Сообщение</th></tr>',
        '</thead><tbody>']
    rows = JsonC().from_file()
    count = 1
    for row in rows:
        str_ = f'''<tr><th scope="row">{count}</th>
        <td>{row["name"]}</td><td>{row["tel"]}</td>
        <td>{row["email"]}</td><td>{row["text"]}</td></tr>'''
        html.append(str_)
        count += 1
    html.append('</tbody></table>')
    return ''.join(html)
