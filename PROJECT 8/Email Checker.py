email = input("Enter Email to check : ")
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):  # XOR for .com or .in
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print("WRONG EMAIL...")
                else:
                    print("RIGHT EMAIL...")
            else:
                print("WRONG EMAIL...")
        else:
            print("WRONG EMAIL..")
    else:
        print("WRONG EMAIL...")
else:
    print("WRONG EMAIL...")
