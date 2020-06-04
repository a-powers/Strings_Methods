### the f means formatted string, it analyzes what is in the curly braces; can be upper case



name = "Bubba and Butter"
adjective = "green"
noun = "alien"

mad_libs = f"{name} laughed at the {adjective} {noun}."
print(mad_libs)

mad_libs = F"{name} laughed at the {adjective} {noun}."
print(mad_libs)

print(f"2 + 2 is {2 + 2}")


print(f"Hi little {adjective} {noun}.  We're {name}.")