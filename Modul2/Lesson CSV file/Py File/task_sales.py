from utils import reading_csv


# Sales_April_2019.csv faylda berilgan ma'lumotlar orqali quyidagilarni bajaring.
# a) Macbook Pro Laptop mahsulotdan nechta buyurtma bo'lganini aniqlang.
# b) Price Each ustun orqali 300 dan katta bo'lgan buyurtmalarni txt faylga yozing.
# c) 04/10/19 sanadan keyingi buyurmalarni boshqa csv faylga yozing

def count_laptop(file):
    count = 0
    for line in reading_csv(file):
        try:
            product, count_order = line[1].strip(), int(line[2].strip())
        except ValueError as e:
            print(e)
        else:
            if product == "Macbook Pro Laptop":
                count += count_order
    return count


def price_each_300(file, txt):
    for line in reading_csv(file):
        try:
            each = (line[3].strip())
            print(each)
        except ValueError as e:
            print(e)
        else:
            if "300" < each:
                with open(txt, 'w') as f:
                    f.write(each)


print(price_each_300('../CSV files/Sales_April_2019.csv', 'each_journal.txt'))
