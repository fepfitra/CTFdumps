flag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"
print(flag)
dec = ""
for char in flag:
    ords = ord(char)
    if (ords >= ord("A") and ords <= ord("Z")):
        tmp = (ords - ord("A") + 13) % 26 + ord("A")
        print(tmp, chr(ords), chr(tmp))
        dec += chr(tmp)
        continue
        
    if (ords >= ord("a") and ords <= ord("z")):
        tmp = (ords - ord("a") + 13) % 26 + ord("a")
        print(tmp, chr(ords), chr(tmp))
        dec += chr(tmp)
        continue
    dec += char
print(dec)
