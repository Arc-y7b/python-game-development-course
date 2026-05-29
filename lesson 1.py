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
      countrydb[country] = capital
      print("Country and capital added successfully")

    elif choice == 2:
      print("\nCountries:")
      for country in countrydb:
       print(country)

    elif choice == 3:
      print("\nCapital:")
      for capital in countrydb.values():
       print(capital)

    elif choice == 4:
     country = input ("Enter country: ").upper()

     if country in countrydb:
       print("Capital:",countrydb[country])
     else:
       print("country not found.")

    elif choice ==5:
      country = input("Enter country to delete:").upper()

      if country in countrydb:
        del countrydb[country]
        print("Country deleted successfully.")
      else:
       print("Country not found.")
    elif choice == 6:
      print("Exiting program...")

    else:
      print("Invalid choice.Please try again.")