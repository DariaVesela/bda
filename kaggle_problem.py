
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

#def searchPassword(file, password):
    # search for a particular password in the file -> return line number?
try:
        with open("rockyou.txt", "r", encoding='ISO-8859-1') as file:
            password = input("Enter the password you're looking for: ")

            for line_num, line in enumerate(file, start=1): 
                if password in line.strip():

                    print(f"{password} is on line {line_num}.")
                print(f"{password} was not found.")

except FileNotFoundError:
        print("File not found")


