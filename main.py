
import csv

pokemons = []
searched = []
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by text in name")
    print("5. Search by length of name")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        for x in pokemons:
            print(pokemons.index(x) , x)
            
            
        
    elif choice == '2':
        pokemons.sort()
        for x in pokemons:
            print(x)
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        pokemons.sort(reverse = True)
        for x in pokemons:
            print(x)
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        search=input("what do you want to search?: ")
        for x in pokemons:
            if search in x:
                searched.append(x)
        for x in searched:
            print(x)
        searched.clear()
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/ref_string_startswith.asp
        
    elif choice == '5':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        length=int(input("Length: "))
        for x in pokemons:
            if length == len(x):
                searched.append(x)
        for x in searched:
            print(x)
        searched.clear()
    elif choice == '6':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 6")

    print("==========================")
