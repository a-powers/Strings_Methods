word = "queueing"

print(word.count("e"))
print(word.count("u"))
print(word.count("q"))
print(word.count("Q"))
print(word.count("z"))

print(word.count("ue"))
print(word.count("ing"))
print(word.count("u") + word.count("e"))


def vowel_count(word: str):
    return word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")
print(vowel_count("superkalifragilisticexpealodcious"))



def find_my_letter(a:str, b:chr):
    return a.rfind(b) 
print(find_my_letter(a = "Butter",b = "u"))