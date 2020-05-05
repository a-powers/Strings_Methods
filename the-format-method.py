# injects dynamic values into string

# name, adjective, noun
mad_libs = "{} laughed at the {} {}."

print(mad_libs.format("Bubba","purple","cat"))
print(mad_libs.format("Butter","jelly","pop"))

mad_libs = "{1} laughed at the {2} {0}."

print(mad_libs.format("Bubba","purple","cat"))
print(mad_libs.format("Butter","jelly","pop"))


mad_libs = "{name} laughed at the {adjective} {noun}."

print(mad_libs.format(name = "Bubba",adjective = "purple",noun = "cat"))
print(mad_libs.format(name = "Butter",adjective = "jelly",noun = "pop"))

name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")

print(mad_libs.format(name = name, adjective=adjective, noun=noun))
