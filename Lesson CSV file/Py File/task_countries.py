from utils import reading_csv


# countries of the world.csv file da berilgan ma'lumotlar orqali quyidagi ma'lumotlarni chiqaring.
# a) Population 20 000 000 dan ko'p bo'lgan mamlakatlar ro'yxatini chiqaring. ✔
# b) C bilan boshlanadigan davlatlar ro'yxatini txt file ga yozing.
# c) GDP 1000 dan baland bo'lganlar ro'yxatini qaytaring.

def get_population(file):
    result = []
    for line in reading_csv(file):
        try:
            name, count = line[0].strip(), int(line[2].strip())
        except (ValueError, IndexError) as e:
            print(e)
        else:
            if count > 20_000_000:
                result.append(f"Country {name} Population {count}")
    return result


def get_country_c(file):
    result = []
    for line in reading_csv(file):
        try:
            name = line[0].strip()
        except Exception as e:
            print(e)
        else:
            if name[0] == "C":
                result.append(name)
    return result


def get_1000_gdp(file):
    result = []
    for line in reading_csv(file):
        try:
            gpd = int(line[8].strip())
        except Exception as e:
            print(e)
        else:
            if gpd > 1000:
                result.append(gpd)

    return result


