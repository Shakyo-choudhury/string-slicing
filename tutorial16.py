# string slicing
# extraction of strings from a parent string
# slicing a cake - analogy

# string[start:end]

string = "Hello, World!"
print("\nOriginal string:", string)
print("First character:", string[0])
print("Slice from index 7 to 12:", string[7:13])
print("Slice from index 1 to the end:", string[1:])

text = "Python is awesome"
print("\nText:", text)
print("Last character:", text[-1])
print("Reverse slice:", text[::-1])


url = "https://www.awesome.com"
domain_name = url[8:-4]
print("\nURL:", url)
print("Extracted domain name:", domain_name)