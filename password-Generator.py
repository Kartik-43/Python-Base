import random

s_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
C_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
s_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '/', '?', '\\', '`', '~', '₹', '.', ',', '<', '>', '"', "'"]
Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
password = []

len_p = int(input("Enter How Long of a Password You would Like to Have (Max Length - 20 characters) ? :- "))
if len_p > 20:
    print("The value should be shorter than 20")

else:
    R_C_S_C = None
    per = int(len_p / 4)
    R_S_A = random.choices(s_alphabets, k=int(per))
    R_S_C = random.choices(s_characters, k=int(per))
    R_C_A = random.choices(C_alphabets, k=int(per))
    R_N = random.choices(Numbers, k=int(per))
    per = len_p - (4 * int(per))
    if per == 3:
        R_C_S_A = random.choices(s_alphabets, k=int(per-2))
        R_C_S_C = random.choices(s_characters, k=int(per-1))
        for i in R_S_A:
            password.append(i)
        for i in R_S_C:
            password.append(i)
        for i in R_C_A:
            password.append(i)
        for i in R_N:
            password.append(i)
        for i in R_C_S_A:
            password.append(i)
        for i in R_C_S_C:
            password.append(i)

    else:
        R_C_S_A = random.choices(s_alphabets, k=int(per))
        for i in R_S_A:
            password.append(i)
        for i in R_S_C:
            password.append(i)
        for i in R_C_A:
            password.append(i)
        for i in R_N:
            password.append(i)
        for i in R_C_S_A:
            password.append(i)

    random.shuffle(password)
    random.shuffle(password)
    random.shuffle(password)
    random.shuffle(password)
    print(f"The Password Generated Of length {len_p} is\n\n")
    print("==========> ", *password, sep="")
