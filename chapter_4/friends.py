fav_languages = {
    'Eve': 'python',
    'Adam': 'c',
    'Edward': 'ruby',
    'Anita': 'python',
}

friends = ['Anita', 'Edward']
for friend in fav_languages.keys():
    print(friend.title())

    if friend in friends:
        print(" Hi " + friend.upper() +
            ", I see your favourite language is " +
            fav_languages[friend].upper() + "!")

print(fav_languages.keys())