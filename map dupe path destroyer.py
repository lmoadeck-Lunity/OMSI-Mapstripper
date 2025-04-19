import os
from collections import Counter

ls = os.listdir()
ls = [os.path.abspath(x) for x in ls if os.path.isfile(x) and x.endswith('.map')]
# print(ls)
for eachmap in ls:
    maap = open(eachmap, 'r', encoding='utf-16-le',errors='ignore').readlines()
    # print(maap)
    count = 0
    while count < len(maap):
        if maap[count] == "[spline]\n":
            patha = maap[count + 2]
            # print(patha)
            patha = patha.split("\\")
            # print(patha)
            fields = Counter(patha)
            duplicates = [field for field, count in fields.items() if count > 1]
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