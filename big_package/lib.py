def try_me():
    fave = input('Enter your favourite number\n >  ')
    if fave.isnumeric() == False:
        print("That's not a number!")
    fave = int(fave)
    if fave == 69:
        return 'Nice'
    elif fave == 13:
        return 'Spooky'
    elif fave == 420:
        return 'Snoop DOGGGGG'
    else:
        return 'Boring'