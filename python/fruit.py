#branching
fruits = ['crabapple', 'cardboard', 'grape', 'orange']
if fruits[0] == 'apple':
    print('Yum!')
elif fruits[0] == 'cardboard' or fruits[0] == 'sand':
    print('Yuck!')
else:
    print("Not bad.")

if 'apple' not in fruits[0]:
    print("Yuck")

age = 5
if age > 0 and age <= 2:
    print('baby')
elif age > 2 and age < 18:
    print('child')
else:
    print('adult')
