file_obj = open("testing.txt", mode ="w", encoding ="utf-8")
file_obj.write("First line \n")
print("Hadiza is the main the main", file = file_obj)
print("Hadiza is the main the main", file = file_obj)

file_obj.close()

file_obj = open("testing.txt", mode ="r", encoding ="utf-8")
# file_obj.write("First line \n")
print(file_obj.read())

file_obj.close()