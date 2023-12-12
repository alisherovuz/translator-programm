translator = {

    "salom": "hello",
    "rahmat": "thank you",
    "hayr": "goodbye",
    "kitob": "book",
    "uy": "house",
    "toshkent": "Tashkent",
    "o'zbekiston": "Uzbekistan"
}

tanla = input("Assalomu alaykum uzbek-english lug'atimizga xush kelibsiz\n\nO'zbek tilidan Ingiliz tiliga tarjima qilish uchun 1 ni bosing\n\nIngiliz tilidan O'zbek tiliga tarjima qilish uchun 2 ni bosing\n\nDasturdan chiqish uchun 3 ni bosing\n\nJavobingiz:   ")
if tanla == '1':
    n = input("O'zbekcha so'z kiriting:  ")
    for k,y in translator.items():
        if k == n:
            print("So'zingiz tarjimasi:",y)
elif tanla == '2':
    n = input("Ingilizcha so'z kiriting:  ")
    for k, y in translator.items():
        if y == n:
            print("So'zingiz tarjimasi:", k)
elif tanla == '3':
    print("dastur faoliyatdan to'xtadi!!!")
