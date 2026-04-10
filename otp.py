import random
def genotp():
    u_1=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    s_1=[chr(i) for i in range (ord('a'),ord('z')+1)]
    otp=''
    for i in range(2):
        otp=otp+random.choice(u_1)+str(random.randint(0,9))+random.choice(s_1)
    return otp

# import random
# upp=[ chr(i) for i in range(65,90+1)]
# low=[ chr(i) for i in range(ord('a'),ord('z')+1)]
# otp=""
# for i in range(4):
#     # otp+=random.choice(upp)+str(random.randint(0,9))+random.choice(low)
#     otp+=str(random.randint(0,9))
# print(otp)


# # print(ord('A'))
# # print(ord('Z'))