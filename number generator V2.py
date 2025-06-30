from tqdm import tqdm

print("This tool is for creating numbers wordlist for brute-force attack\n")


filelocation = input("Enter the location where you want to save the file : ")
file_name = input("Enter the file name (e.g., numbers): ")
FNL = filelocation+file_name + ".txt"


n = input("Enter the maximum number of numbers you want: ")


print("This is your file: " + FNL)
print(n)


try:
    with open(FNL, "w") as file:
        
        for number in tqdm(range(int(n)), desc="Generating wordlist", unit=" number"):
            file.write(f"{number:09}\n")
    print(f"\nWordlist created successfully and saved to "+FNL)
except Exception as e:
    print(f"An error occurred: {e}")
input("Press Enter to Exit")
