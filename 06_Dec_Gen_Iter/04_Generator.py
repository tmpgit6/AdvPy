def get_name():
    yield "Thomas"
    yield "Ingo"
    yield "Sara"
    yield "Lena"



my_generator = get_name()

print(my_generator)


print(next(my_generator))

for name in my_generator:
    print(name)