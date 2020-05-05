phone_number = "555 555 1234"

print(phone_number.replace(" ", "-"))
print(phone_number.replace("5", "9", 2))



def fancy_cleanup(a:str):
    return a.strip().replace("g","z").replace(" ","!")
print(fancy_cleanup("grade grade"))