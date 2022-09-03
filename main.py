posizione={"x":0,"y":0,"d":"N"} #input
comandi=("f","f","f") #input

for i in comandi:
    print("Posizione:",posizione["x"],posizione["y"],posizione["d"])

    if i=="f":
        if posizione["d"]=="N":
            posizione["x"]+=1
        if posizione["d"]=="E":
            posizione["y"]+=1
        if posizione["d"]=="S":
            posizione["x"]-=1
        if posizione["d"]=="W":
            posizione["y"]-=1
    elif i=="a":
        if posizione["d"]=="N":
            posizione["d"]="W"
        elif posizione["d"]=="W":
            posizione["d"]="S"
        elif posizione["d"]=="S":
            posizione["d"]="E"
        elif posizione["d"]=="E":
            posizione["d"]="N"
    elif i=="o":
        if posizione["d"]=="N":
            posizione["d"]="E"
        elif posizione["d"]=="E":
            posizione["d"]="S"
        elif posizione["d"]=="S":
            posizione["d"]="W"
        elif posizione["d"]=="W":
            posizione["d"]="N"

print("Posizione Fine:",posizione["x"],posizione["y"],posizione["d"])
