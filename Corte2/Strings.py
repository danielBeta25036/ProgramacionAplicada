s = "abracadabra"

print(len(s))
print(s.index("a"))

print(s[0])
print(s[3:5])


# this will give us an error
s[0] = "b"

print('h' in 'abcd') # False

print('ab' in 'abcd') # False


print(['a', 'b'] in ['a', 'b', 'c', 'd']) # False


abc_list = list("abracadabra")
print(abc_list)

l = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

s = "".join(l)
print(s)
animals = ('cat', 'dog', 'fish')

# a space-separated list
print(" ".join(animals))

# a comma-separated list
print(",".join(animals))

# a comma-separated list with spaces
print(", ".join(animals))

print("cat    dog fish\n".split())


print("cat|dog|fish".split("|"))


print("cat, dog, fish".split(", "))

print("cat, dog, fish".split(", ", 2))

