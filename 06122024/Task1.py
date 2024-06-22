year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 400 ==0:
        if year % 100 == 0:
            print("Leap year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")

start_year = int(input("Enter the starting year: "))
end_year = int(input("Enter the ending year: "))

print(f"Leap years between {start_year} and {end_year}:")
for year in range(start_year, end_year + 1):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year)
            else:
                continue
        else:
            print(year)
