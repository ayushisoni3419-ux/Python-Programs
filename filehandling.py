# ==========================================
# File Handling in Python
# Topics Covered:
# 1. Write to a File
# 2. Read a File
# 3. Append to a File
# 4. Count Number of Lines
# 5. Search for a Word
# ==========================================

# ---------- Write to a File ----------
with open("students.txt", "w") as file:
    file.write("Ayushi\n")
    file.write("Riya\n")
    file.write("Rahul\n")
    file.write("Aman\n")

print("Data written successfully.\n")


# ---------- Read a File ----------
print("Reading File:")
with open("students.txt", "r") as file:
    data = file.read()
    print(data)


# ---------- Append to a File ----------
with open("students.txt", "a") as file:
    file.write("Priya\n")

print("New data appended successfully.\n")


# ---------- Count Number of Lines ----------
count = 0

with open("students.txt", "r") as file:
    for line in file:
        count += 1

print("Total Lines:", count)
print()


# ---------- Search for a Word ----------
word = input("Enter a name to search: ")

with open("students.txt", "r") as file:
    data = file.read()

if word in data:
    print(word, "is present in the file.")
else:
    print(word, "is not present in the file.")