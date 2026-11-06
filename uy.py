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
# >>>>>>>>>>>>>>>>>>>>>>>>>-3-<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def merge_unique_ids(active_users: list[str], new_users: list[str]) -> list:
    all_users=[x.strip() for x in active_users + new_users if x.strip()]
    return(list(set(all_users)))
active_users=input("Namuna:active_users =[U1001, U1002, U1003, U1004, U1001] ',' bilan ajrating!!!\n active_users :").split(",")
new_users=input("\nNamuna:active_users = [U1003, U1005, U1006 ,U1002, U1007] ',' bilan ajrating!!!\n new_users :").split(",")

print("Noyob ID lar ro'yxati:",merge_unique_ids(active_users,new_users))
# >>>>>>>>>>>>>>>>>>>>>>>>>-4-<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def sorted_by_price(products: list) -> list:
    return sorted(products, key=lambda x: int(x[1]),reverse=True)

products=[]
for x in range(int(input("Nechta mahsulot:"))):
    print(f"---{x+1}-Mahsulot---")
    nomi = input("Mahsulot nomi: ")
    narxi = input("Narxi: ")
    miqdori = input("Soni: ")

    products.append((nomi,narxi,miqdori))

natija=sorted_by_price(products)

for x in natija:
    print(x)