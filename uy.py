# >>>>>>>>>>>>>>>>>>>>>>>>>-1-<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def majority_element(nums: list) -> int:
    if not nums:
        return -1
    dct={}
    for x in nums:
        if x not in dct:
            dct[x]=1
        else:
            dct[x]+=1
    return max(dct, key=dct.get)

son=input("Sonlar (masalan: 2,2,1,1,1,2,2) shu tartibda kiritilsin:\n:")

if son.strip() == "":
    nums=[]
else:
    nums=[int(x) for x in son.split(",")]

kop_son=majority_element(nums)
if kop_son != -1:
    print("Eng ko'p takrorlangan son:",kop_son )
else:
    print("bo'sh ro'yxat",kop_son)
# >>>>>>>>>>>>>>>>>>>>>>>>>-2-<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def search_by_genre(cinema: list, genre: str) -> list:
    natija=[]
    for film in cinema:
        if film["genre"].lower()==genre.lower():
            natija.append(film)
    return natija

cinema = [
    {"title": "Avatar", "genre": "Fantastika", "price": 40000},
    {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
    {"title": "Oq yo'l", "genre": "Drama", "price": 25000},
    {"title": "Dune", "genre": "Fantastika", "price": 35000},
]    

janr=input("Qaysi janrdagi film qidiryapsiz (masalan: Fantastika, Drama, Detektiv)\n:")

natija=search_by_genre(cinema,janr)

if natija:
    for f in natija:
       print(f"{f['title']} | {f['genre']} | {f['price']} so'm")
else:
    print(" [] Bunday janrdagi film topilmadi")