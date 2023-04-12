file = open("./warm", "rb").read()
file = str(file)

front = file.find("pico")
end = file.find("}",front) + 1
print(file[front:end])
