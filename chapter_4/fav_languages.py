fav_languages = {
    'jen': 'python', 
    'sarah': 'C',
    'edwardo': 'ruby',
    'phil': 'python',
    }

for name, language in fav_languages.items():
    print(name.upper() + "'s favorite language is " + language.upper() + "!")

# Keys
for name in fav_languages.keys():
    print(name.upper(), 'Value is',fav_languages[name])


# for name in fav_languages:
#     print(name.title())