from utils import reading_csv


# worldcities.csv faylda berilgan ma'lumotlar orqali quyidagilarni bajaring.
# a) Country Uzbekistan bo'lgan shaharlarni txt faylga yozing
# b) Uzbekistan shaharlari lat va lng orqali quyidagi ko'rinishdagi
# location=https://my-location.org/?lat=41.284067&lng=69.147750 ma'lumotni txt faylga yozing.

def regions(file, file_txt):
    for line in reading_csv(file):
        country, region = line[4].strip(), line[7].strip()
        if country == "Uzbekistan":
            with open(file_txt, 'w') as txt:
                txt.write(region)


# print(regions('../CSV files/worldcities.csv', 'regions.txt'))

def address(file, file_txt):
    for line in reading_csv(file):
        country, region = line[4].strip(), line[7].strip()
        lat, lng = line[2].strip(), line[3].strip()
        if country == "Uzbekistan":
            with open(file_txt, 'a') as txt:
                txt.write(f"{region} lat {lat} lng {lng}\n")


print(address('../CSV files/worldcities.csv', 'lat_lng.txt'))
