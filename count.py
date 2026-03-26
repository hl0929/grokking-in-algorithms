import os

with open("docs/README.md", "r", encoding="utf-8") as f:
    data = [i for i in f.read().strip().split("\n") if "md" in i]
count1 = len(data)
print("Count1:", count1)

filename_list = []
for filename in os.listdir("docs/content"):
    if "md" in filename and not filename.startswith("_"):
        filename_list.append(filename)
count2 = len(filename_list)
print("Count2:", count2)


if count1 == count2:
    print("No Diff")
else:
    print("Diff")