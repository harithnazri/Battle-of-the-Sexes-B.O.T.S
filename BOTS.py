playerInput = str(input("Input > ")).lower()

if playerInput != "roll":
            pos = playerInput.split(" ")
            pos.remove('roll')
            pos = list(map(int,pos))
            for x in pos:
                x -= 1
                print(pos)