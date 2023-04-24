import time
import random

def cach1():
    time.sleep(0.5)
    print()
    print("-"*50)

def cach2():
    print("-"*50)
    print()
    time.sleep(0.5)

def game_over():
    while True:
        try:
            cach1()
            chon = int(input("1.Chơi lại\n2.Thoát\nChọn (1,2): "))
            cach2()
            if chon == 1:
                return True
            elif chon == 2:
                return False
            else:
                cach1()
                print("Vui lòng nhập đúng")
                cach2()
        except:
            cach1()
            print("vui lòng nhập đúng")
            cach2()

def choi_mot_nguoi():
    run = True
    while run == True:
        computer = random.choice(["DICTIONARY","COMPUTER","MOUSE","KEYBOARD","ACCOMPLISHMENT","RECORD","DISPLAY","MOTOBIKE",
                                "ICE SCREAM","CLOCK","APPLE","BRICK","TABLE","CHAIR","MY BODY","MY HEAD","ADOLESCENT","CHROME",
                                "PYTHON","PIZZA"])
        
        print("Trò chơi bắt đầu")
        net = 0

        m = computer

        computer = list("-"*len(computer))
        b = 0
        m = list(m)
        cach1()
        n = []
        while True:
            print(f"Bạn đã nhập: {n}")
            print(computer)
            player = input("Nhập đi: ")
            player = player.upper()
            n.append(player)

            print()
            if len(player) > 1:
                time.sleep(0.5)
                print()
                print("Vui lòng nhập từ có độ dài là 1")
                net+=1
                print(f"Số nét: {net}/12")
            
            else:
                for i in range(len(m)):
                    if m[i] == player:
                        computer[i] = player
                        b = 1

                    if m[i] == " " and player == "":
                        computer[i] = " "
                        b = 1

                if b == 0:
                    net += 1
                    time.sleep(0.5)
                    print()
                    print(f"Nhập sai =) {net}/12")
                else:
                    time.sleep(0.5)
                    print()
                    print("Hay lắm =)")
                    b = 0
            
            if net >= 12:
                cach1()
                print("Bạn thua rồi = ((")
                print(f"Số nét {net}/12")
                print(f"Đáp án {m}")
                time.sleep(0.5)
                cach2()
                time.sleep(1)
                kp = game_over()

                if kp == True:
                    kp = False
                    break

                else:
                    kp = True
                    break

            elif m == computer:
                cach1()
                print("XIN CHÚC MỪNG BẠN ĐÃ THẮNG!")
                print(f"Số nét {net}/12")
                print(f"Đáp án {m}")
                time.sleep(0.5)
                cach2()
                time.sleep(1)
                kp = game_over()

                if kp == True:
                    kp = False
                    break
                else:
                    kp = True
                    break
            else:
                print()
        
        if kp == True:
            run = False

def choi_hai_nguoi():
    run = True
    while run == True:
        while True:
            cach1()
            print("PLAYER 1")
            player1 = input("Nhập từ: ")
            player1 = player1.upper()
            cach2()
            if player1 != "":
                break
            else:
                cach1()
                print("Vui lòng nhập lại")
                cach2()
        
        print("\n"*100)
        m = list(player1)
        computer = list("-"*len(player1))
        n = []
        b = 0
        net = 0
        cach1()
        print("PLAYER 2")
        while True:
            print(computer)
            print(n)
            player2 = input("Nhập đi: ")
            player2 = player2.upper()
            n.append(player2)

            for i in range(len(m)):
                if player2 == m[i]:
                    computer[i] = player2
                    b = 1
                
                if player2 == "" and m[i] == " ":
                    computer[i] = " "
                    b = 1
            
            if b == 1:
                print()
                print("Hay lắm")
                print(f"Số nét {net}/12")
                print()
            else:
                print()
                net += 1
                print("Trượt =))")
                print(f"Số nét {net}/12")
            
            if computer == m:
                print()
                print("Xin chúc mừng PLAYER 2 đã thắng")
                print("PLAYER 1 đã thua = ((")
                print(f"Số nét {net}")
                time.sleep(1)
                kp = game_over()

                if kp == True:
                    break
                else:
                    break
            
            if net >= 12:
                print()
                print("Xin chúc mừng PLAYER 1 đã thắng")
                print("PLAYER 2 đã thua =((")
                print(f"Số nét {net}")
                time.sleep(1)
                kp = game_over()

                if kp == True:
                    break
                else:
                    break
        
        if kp == False:
            break

def menu():
    while True:
        try:
            cach1()
            chon = int(input("1.Chơi Một Người\n2.Chơi Hai Người\n3.Thoát\nChọn (1,2,3): "))
            cach2()
            
            if chon == 1:
                choi_mot_nguoi()

            elif chon == 2:
                choi_hai_nguoi()

            elif chon == 3:
                break
            
            else:
                cach1()
                print("Vui lòng nhập đúng")
                cach2()

        except:
            cach1()
            print("Vui lòng nhập đúng")
            cach2()
    

def main():
    print("Trò Chơi HangMan")
    while True:
        try:
            cach1()
            chon = int(input("1.Bắt Đầu\n2.Thoát\nChọn (1,2): "))
            cach2()
            if chon == 1:
                menu()

            elif chon == 2:
                print("Tạm biệt ^_^")
                print()
                break
            
            else:
                cach1()
                print("Vui lòng nhập đúng")
                cach2()

        except:
            cach1()
            print("Vui lòng nhập đúng")
            cach2()

if __name__ == "__main__":
    main()