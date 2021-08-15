import os
script = "netsh wlan show profile > txt.txt"
os.system(script)

networks = []
f = open("txt.txt", "r+")
for line in f:
    line = line.strip()
    if line.startswith('All'):
        find = line.find(":")
        wifi = line[find+1:].strip()
        networks.append(wifi)
f.close()
# print("networks : ", networks)

folders = []
for network in networks:
    network_name = network.replace(" ", "_")
    folders.append(f"pass_{network_name}.txt")
    script = f'netsh wlan show profile "{network}" key=clear > pass_{network_name}.txt'
    # print(script)
    os.system(script)
# print("folders : ", folders)

passwords = {}
for fn in folders:
    f = open(fn, "r+")
    for line in f:
        line = line.strip()
        if line.startswith('Key'):
            find = line.find(":")
            password = line[find+1:].strip()
            if password == "1":
                continue
            # print(password)
            passwords[fn[5:-4]] = password
    f.close()

print("=====================")
print(passwords)
print("=====================")

script = f"Del txt.txt "
for folder in folders:
    script+= folder + " "

os.system(script)
