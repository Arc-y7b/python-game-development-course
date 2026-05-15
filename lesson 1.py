countrydb={}
while True:
    print("1. insert")
    print("2. Display all countrys")
    print("3. Display all capitals") 
    print("4. Get capitals")
    print("5. Delete")

    choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    country = input("enter country : ").upper()
     capital = input("enter capital : ").upper()
    countryDb[country] = capital