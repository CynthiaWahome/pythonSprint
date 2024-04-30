guests = ["Mario Jones", "Ian Mugambi", "Cynthia", "Effie"]
guests.append("Sylvia")
guests.append("Olivia")
guests.append("Thomas")

print("I can invite only two people for dinner")
print("I am sorry", guests.pop(), "I cant invite you to dinner")
print("I am sorry", guests.pop(), "I cant invite you to dinner")
print("I am sorry", guests.pop(), "I cant invite you to dinner")
print("I am sorry", guests.pop(), "I cant invite you to dinner")

print(guests[0], "Youre still invited")
del guests[-1]
del guests [-1]
del guests[-1]

print(guests)
