# a method is a function that acts upon a specific object

browser = "Google Chrome"

print(browser.find("C"))
# returns the first index of the substring
print(browser.find("Ch"))
print(browser.find("o"))
print(browser.find("G"))
print(browser.find("Z"))
# an ouput of -1 shows when index isn't available

print(browser.find("o"))
print(browser.find("o", 2))
print(browser.find("o", 5))
# the position of ("0", 5) starts at 5 and returns index position from 0 to give you 10

print("Ch" in browser)

print(browser.index("e"))
#print(browser.index("Z"))
# the Z crashes program


# rfind:  print(browser.rfind(substring,start:))
print(browser.rfind("o",1,-5))
print(browser.rfind("e",6))
print(browser.rfind("e",-1))
print("Chicken_butt".rfind("c",1))
print("chicken_butt".rfind("z"))   # -1 is returned when not found
