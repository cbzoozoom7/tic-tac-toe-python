move = 0
one = " "
two = " "
three = " "
four = " "
five = " "
six = " "
seven = " "
eight = " "
nine = " "
win = 0
while one == " " or two == " " or three == " " or four == " " or five == " " or six == " " or seven == " " or eight == " " or nine == " ":
    if one == two == three != " " or four == five == six != " " or seven == eight == nine != " " or one == four == seven != " " or two == five == eight != " " or three == six == nine != " " or one == five == nine != " " or three == five == seven != " ":
        print "Player 2 wins."
        one = "X"
        two = "X"
        three = "X"
        four = "X"
        five = "X"
        six = "X"
        seven = "X"
        eight = "X"
        nine = "X"
        win = 1
    else:
        print "1|2|3"
        print "-+-+-"
        print "4|5|6"
        print "-+-+-"
        print "7|8|9"
        move = input("Player 1: Make your move. ")
        if move == 1:
            if one == " ":
                one = "O"
            else:
                print "That's cheating!"
        elif move == 2:
            if two == " ":
                two = "O"
            else:
                print "That's cheating!"
        elif move == 3:
            if three == " ":
                three = "O"
            else:
                print "That's cheating!"
        elif move == 4:
            if four == " ":
                four = "O"
            else:
                print "That's cheating!"
        elif move == 5:
            if five == " ":
                five = "O"
            else:
                print "That's cheating!"
        elif move == 6:
            if six == " ":
                six = "O"
            else:
                print "That's cheating!"
        elif move == 7:
            if seven == " ":
                seven = "O"
            else:
                print "That's cheating!"
        elif move == 8:
            if eight == " ":
                eight = "O"
            else:
                print "That's cheating!"
        elif move == 9:
            if nine == " ":
                nine = "O"
            else:
                print "That's cheating!"
        else:
            print "Invalid input."
        print one, "|", two, "|", three
        print "--+---+--"
        print four, "|", five, "|", six
        print "--+---+--"
        print seven, "|", eight, "|", nine
    
        if one == " " or two == " " or three == " " or four == " " or five == " " or six == " " or seven == " " or eight == " " or nine == " ":
                if one == two == three != " " or four == five == six != " " or seven == eight == nine != " " or one == four == seven != " " or two == five == eight != " " or three == six == nine != " " or one == five == nine != " " or three == five == seven != " ":
                    print "Player 1 wins."
                    one = "O"
                    two = "O"
                    three = "O"
                    four = "O"
                    five = "O"
                    six = "O"
                    seven = "O"
                    eight = "O"
                    nine = "O"
                    win = 1
                else:
                    print "1|2|3"
                    print "-+-+-"
                    print "4|5|6"
                    print "-+-+-"
                    print "7|8|9"
                    move = input("Player 2: Make your move. ")
                    if move == 1:
                        if one == " ":
                            one = "X"
                        else:
                            print "That's cheating!"
                    elif move == 2:
                        if two == " ":
                            two = "X"
                        else:
                            print "That's cheating!"
                    elif move == 3:
                        if three == " ":
                            three = "X"
                        else:
                            print "That's cheating!"
                    elif move == 4:
                        if four == " ":
                            four = "X"
                        else:
                            print "That's cheating!"
                    elif move == 5:
                        if five == " ":
                            five = "X"
                        else:
                            print "That's cheating!"
                    elif move == 6:
                        if six == " ":
                            six = "X"
                        else:
                            print "That's cheating!"
                    elif move == 7:
                        if seven == " ":
                            seven = "X"
                        else:
                            print "That's cheating!"
                    elif move == 8:
                        if eight == " ":
                            eight = "X"
                        else:
                            print "That's cheating!"
                    elif move == 9:
                        if nine == " ":
                            nine = "X"
                        else:
                            print "That's cheating!"
                    else:
                        print "Invalid input."
                    print one, "|", two, "|", three
                    print "--+---+--"
                    print four, "|", five, "|", six
                    print "--+---+--"
                    print seven, "|", eight, "|", nine
if win != 1:
    if one == two == three != " " or four == five == six != " " or seven == eight == nine != " " or one == four == seven != " " or two == five == eight != " " or three == six == nine != " " or one == five == nine != " " or three == five == seven != " ":
        print "Player 1 wins."
    else:
        print "Cat, the board is full"