empty_space = "    content           "
# strip focuses on the beginning and the end of the string, not the middle
print(empty_space.rstrip())
print(empty_space.lstrip())
print(empty_space.strip())

website = "www.python.org"

print(website.lstrip("w"))
print(website.rstrip(".org"))
print(website.strip("worg."))