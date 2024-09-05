gryff = 0
raven = 0
huffle = 0
sltyh = 0

print('Do you like Dawn or Dusk?')
print('1)Dawn')
print('2)Dusk')
answear = int (input('Enter your answer (1-2):'))
if answear == 1:
    print('Gryffindor +1')
    print('Ravenclaw +1')
    gryff += 1
    raven += 1
elif answear == 2:
    print('Hufflepuff +1')
    print('Slytherin +1')
    huffle += 1
    sltyh += 1
else:
    print('Wrong input')   

print('When I’m dead, I want people to remember me as:?')
print('1)The Good')
print('2)The Great')
print('3)The Wise')
print('4)The Bold')
answear = int (input('Enter your answer (1-4):'))
if answear == 1:
    print('Hufflepuff +1')
    huffle += 1
elif answear == 2:
    print('Slytherin +1')
    sltyh += 1
elif answear == 3:
    print('Ravenclav +1')
    raven += 1
elif answear == 4:
    print('Gryffindor +1')
    gryff += 1
else:
    print('Wrong input') 

print('Which kind of instrument most pleases your ear:?')
print('1)The violin')
print('2)The trumpet')
print('3)The piano')
print('4)The drum')
answear = int (input('Enter your answer (1-4):'))
if answear == 1:
    print('Slytherin +1')
    sltyh += 1
elif answear == 2:
    print('Hufflepuff +1')
    huffle += 1
elif answear == 3:
    print('Ravenclav +1')
    raven += 1
elif answear == 4:
    print('Gryffindor +1')
    gryff += 1
else:
    print('Wrong input') 

winner = max(gryff, sltyh, raven, huffle)

if gryff == winner:
    print('Gryffindor wins!')
if sltyh == winner:
    print('Slytherin wins!')
if huffle == winner:
    print('Hufflepuff wins!')
if raven == winner:
    print('Ravenclav wins!')