import re
with open('data.txt', 'r', encoding = 'utf-8') as raw:
    text = raw.read()
total_sum = 0

company_name = re.search(r'ДУБЛИКАТ\n(.*)\n', text).group(1)

bin = re.search(r'БИН (\d+)', text).group(1)

purchase = re.findall(r'\d+\.\n([^\n]+)\n([0-9, ]+) x ([0-9, ]+)\n([0-9, ]+)', text)

date = re.search(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}', text).group()

address = re.search(r'  ', text).group()

total_price = re.search(r'ИТОГО:\n([0-9, ]+)', text).group(1)
print(f'Название компании: {company_name}\nНомер BIN: {bin}\nДата: {date}\nАдрес: {address}\n')

def str_to_num(s):
    s = s.replace(' ', '')
    s = s.replace(',', '.')
    return float(s)
for i, item in enumerate(purchase):
    print(f'{i + 1}. {item[0]}')
    print(f'\t{item[1]} x {item[2]} = {item[3]}')
    total_sum += str_to_num(item[3])
print(f'Our sum: {total_sum}')