My = input("What is your name?")
Love = input("What is your BF/GF name?")
combine_string = My + Love
lower_case_string = combine_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t + r + u + e
l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e

love_score = int(true) + int(love)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}.And You go together like 2 different universe. ")
elif love_score >= 40 or love_score <= 50:
    print(f"Your love score is {love_score}. You are alright together")
else:
    print(f"Your love Score is {love_score}")

