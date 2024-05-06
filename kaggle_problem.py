
# BDA 1st seminar

# if __name__ == "__main__":
#     try:
#         with open("rockyou.txt", "r", encoding='ISO-8859-1') as file:
#             total = 0 
#             for line in file:
#                 total += 1
#                 print(total)
#     except FileNotFoundError:
#         print("File not found")


# QUESTION: Create a search_password function to search for a password in a given file.
# Find: 1234
# 1233242432
# mary

def searchPassword(file_name):
    # search for a particular password in the file -> return line number?
    # pass filenames as params
    # use the guard
    # use the functions

    try:
        with open(file_name, "r", encoding='ISO-8859-1') as file:
            password = input("Enter the password you're looking for: ")

            for line_num, line in enumerate(file, start=1): 
                if password in line.strip():
                    print(f"{password} is on line {line_num}.")
                    return
                 # once found, exit function
                else:
                    print(f"{password} was not found.") # put this outside the loop - only should execute after you've gone through the entire file

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    searchPassword("rockyou.txt")
