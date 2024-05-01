guests = ["Abel Matunda", "John Doe", "Jane Smith", "Martin Luther"]
print(len(guests))

mountains = ["Kenya", "Everest", "Kilimanjaro", "Kilimambogo"]
rivers = ["Nyando", "Tana", "Nile", "Athi"]
countries = ["Seychelles", "Mauritius", "South Africa","Botswana"]
cities = ["Bujumbura", "Kinsasha", "Lagos", "Pretoria", "Daresalaam"]
languages = ["Swahili", "French","Khosa","Pigme","Espanol"]

mountains.sort()
print(mountains)

rivers.sort(reverse=True)
print(rivers)

print(sorted(languages))
print(languages)

cities.reverse()
print(cities)

# combining sorted and reverse
reversed_cities = sorted(cities)
reversed_cities.reverse()
print(reversed_cities)

