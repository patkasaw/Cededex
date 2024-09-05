import random
symbols = ['🍒',' 🍇', '🍉','7️⃣']

def play():
    question = str(input('Dou you want to play the Jackpot 💰 ? Answear: YES/NO\n'))

    if question == 'YES':
        results = (random.choices(symbols, k = 3))
        print(f'{results[0]} | {results[1]} | {results[2]}')        
            
        if (results[0] == ' 7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'):
            print('Jackpot! 💰')
        else:
            play()   

    else:
        print('Thanks for playing!')

play()