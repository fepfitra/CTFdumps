import base64
flag = open("enc_flag").read()
while True:
    try:
        flag = base64.b64decode(flag).decode()
        if "pico" in flag:
            print(flag)
            break
    except:
        pass
