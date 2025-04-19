import os
from collections import Counter
import time

ls = os.listdir()
ls = [os.path.abspath(x) for x in ls if os.path.isfile(x) and x.endswith('.map')]
# print(ls)
debug = True
for eachmap in ls:
    maap = open(eachmap, 'r', encoding='utf-16-le',errors='ignore').readlines()
    # print(maap)
    if debug:
        logfile = open("log.txt", "a", encoding='utf-8')
    count = 0
    while count < len(maap):
        if maap[count] == "[spline]\n":
            patha = maap[count + 2]
            # print(patha)
            patha = patha.split("\\")
            # print(patha)
            fields = Counter(patha)
            duplicates = [field for field, count in fields.items() if count > 1]
            # print(f"{'\\'.join(duplicates)}\\{patha[-1]}")
            logfile.write(f"[LOG_splines] {time.time()} {eachmap} {patha} {duplicates}\n")
            # print(locals())
            if duplicates:
                seen = set()
                new_path = []
                for folder in patha:
                    if folder not in seen:
                        seen.add(folder)
                        new_path.append(folder)
                print(f"{'\\'.join(new_path)}")
                maap[count + 2] = "\\".join(new_path)
                with open(eachmap, 'w', encoding='utf-16', errors='ignore') as f:
                    f.writelines(maap)
                print(f"Updated path: {'\\'.join(new_path)}")
        
        if maap[count] == "[object]\n":
            patha = maap[count + 2]
            # print(patha)
            patha = patha.split("\\")
            # print(patha)
            fields = Counter(patha)
            duplicates = [field for field, count in fields.items() if count > 1]
            logfile.write(f"[LOG_object] {time.time()} {eachmap} {patha} {duplicates}\n")
            if duplicates:
                seen = set()
                new_path = []
                for folder in patha:
                    if folder not in seen:
                        seen.add(folder)
                        new_path.append(folder)
                print(f"{'\\'.join(new_path)}")
                maap[count + 2] = "\\".join(new_path)
                with open(eachmap, 'w', encoding='utf-16', errors='ignore') as f:
                    f.writelines(maap)
                print(f"Updated path: {'\\'.join(new_path)}")
            # print(f"{'\\'.join(duplicates)}\\{patha[-1]}")

        count += 1
    # break
    # for eachline in maap:
    #     if eachline == "[spline]":
pause = input("Press Enter to continue...")