with open("python.txt", 'w') as f: #'w' , 'r', 'a'
    f.write("success\n")
    f.write("Devops\n")

with open("python.txt", 'r') as f1:
    print(f1.readlines())



