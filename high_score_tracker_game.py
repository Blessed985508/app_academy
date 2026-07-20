#The High-Score Tracker Game

end="stop" 





while True: 
    input_entered = input("Enter a game score next to the flashing cursor: ").strip().lower()
    if input_entered == end :
        print("Game session has ended!")
        break
    else: 
        input_entered = int(input_entered)


        if input_entered > 100:
            print("Wow! Thats a new score!")
        else :
            print("Good try, keep playing")  