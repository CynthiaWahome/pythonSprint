def build_profile(First, Last, **user_info):
    profile = {}
    profile['first_name'] = First
    profile['last_name'] = Last

    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', Location = 'burkingham', Field = ' chemistry')
user_profile = build_profile('cynthia', 'wamzy',Hobby = 'python , family', Wishlist = 'fill up my passport with stamps')
print(user_profile)