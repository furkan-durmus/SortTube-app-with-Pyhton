import random
# LİSTEDEKİ SON İTEMİ BULMA
"""

 a=["0","1","2","1","1","2","1","3","4"]
print(len(a)-1-a[::-1].index("1"))

"""
renkler = ["RED    ", "BLUE   ", "GREEN  "]
random.shuffle(renkler)
birinci=renkler[:]
random.shuffle(birinci)
ikinci=renkler[:]
random.shuffle(ikinci)
ucuncu=renkler[:]
dorduncu=["       "]*3

print("\n")
print("     |", birinci[2], "|", "              |", ikinci[2], "|", "               |", ucuncu[2], "|", "               |", dorduncu[2], "|")
print("     |", birinci[1], "|", "              |", ikinci[1], "|", "               |", ucuncu[1], "|", "               |", dorduncu[1], "|")
print("     |", birinci[0], "|", "              |", ikinci[0], "|", "               |", ucuncu[0], "|", "               |", dorduncu[0], "|")
print(" ___/-----------\___       ___/-----------\___        ___/-----------\___        ___/-----------\___")
print("       Tube-1                    Tube-2                      Tube-3                     Tube-4")
print("\n")




finish=False

while finish==False:
    source = -1
    src = ["       "] * 3
    srcSel = "       "
    while source>4 or source<1:
        source = int(input("Source(1-4):"))
        if source==1:
            src=birinci
        elif source==2:
            src=ikinci
        elif source==3:
            src=ucuncu
        elif source==4:
            src=dorduncu


        if 1<=source<=4 and src[0]=="       ":
            print("Selected Tube is Empty!Select another one.")
            source=-1



    if "       " not in src:
        srcSel=src[len(src)-1]
    else:
        srcSel=src[src.index("       ")-1]
    print("SELECTED COLOR:",srcSel)

    des="       "
    desSel="       "
    destination=-1
    while destination>4 or destination<1:
        destination = int(input("Destination(1-4):"))

        if destination==source:
            print("Same Tube! Select Different Tube.")
            destination=-1
        else:
            if destination == 1:
                des = birinci
                if des[2]!="       ":
                    print("This Tube is full, Select different tube!")
                    destination = -1
                else:
                    empty = des.index("       ")
                    des[empty] = srcSel
                    src[len(src) - 1 - src[::-1].index(srcSel)] = "       "



            elif destination == 2:
                des = ikinci
                if des[2] != "       ":
                    print("This Tube is full, Select different tube!")
                    destination = -1
                else:
                    empty = des.index("       ")
                    des[empty] = srcSel
                    src[len(src)-1-src[::-1].index(srcSel)] = "       "


            elif destination == 3:
                des = ucuncu
                if des[2] != "       ":
                    print("This Tube is full, Select different tube!")
                    destination = -1
                else:
                    empty=des.index("       ")
                    des[empty]=srcSel
                    src[len(src)-1-src[::-1].index(srcSel)] = "       "


            elif destination == 4:
                des = dorduncu
                if des[2] != "       ":
                    print("This Tube is full, Select different tube!")
                    destination = -1
                else:
                    empty = des.index("       ")
                    des[empty] = srcSel
                    src[len(src)-1-src[::-1].index(srcSel)] = "       "



    print("\n")
    print("     |", birinci[2], "|", "              |", ikinci[2], "|", "               |", ucuncu[2], "|",
          "               |", dorduncu[2], "|")
    print("     |", birinci[1], "|", "              |", ikinci[1], "|", "               |", ucuncu[1], "|",
          "               |", dorduncu[1], "|",)
    print("     |", birinci[0], "|", "              |", ikinci[0], "|", "               |", ucuncu[0], "|",
          "               |", dorduncu[0], "|", "              |")
    print(
        " ___/-----------\___       ___/-----------\___        ___/-----------\___        ___/-----------\___")
    print(
        "       Tube-1                    Tube-2                      Tube-3                     Tube-4")
    print("\n")

    if birinci[0]==birinci[1]==birinci[2] and ikinci[0]==ikinci[1]==ikinci[2] and ucuncu[0]==ucuncu[1]==ucuncu[2] and dorduncu[0]==dorduncu[1]==dorduncu[2] :
        finish=True
        print("YOU WIN!")

