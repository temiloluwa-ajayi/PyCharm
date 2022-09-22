# with open('temp_file.text', mode='w', encoding='utf-8') as file_object:
#     print(file_object.tell())
#     file_object.write("Life is good with Banke\n")
#     file_object.seek(10)
#     print(file_object.tell())
#     file_object.write("Life is good with Banke\n")
#     file_object.writelines("Life\n is\n good\n with\n Banke\n")
#     file_object.writelines(['Life\n', 'is\n', 'great\n', 'with\n', 'C12\n'])
#
#
# with open('temp_file.text', mode='r', encoding='utf-8') as file:
#     # print(file.readline()) #OR
#     # print(file.readlines())
#
#     for idx, line in enumerate(file.readlines(), start=1):
#         print(f"{idx}. {line.upper()}")


from pathlib import Path
path = Path("./folder/sub-folder/text.txt")

print(path.resolve()) #Gives the absolute path from the system
path.parent.mkdir(parents=True, exist_ok=True)
path.touch(exist_ok=True) #Prints the directory of whta was created.

open('text.txt', mode='w')
with path.open(mode='a') as f:
    f.write("Hello")