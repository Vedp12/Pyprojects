import os

def select_pdfs():
    # 1. Set the folder path where your PDFs are located
    folder_path = r'/home/tux_106/Documents/PyProj/pra/' 
    
    # 2. List all files ending with .pdf
    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(f)] 
    
    if all_files == False:
    
        return "FILE is not available"
    

    # 3. Take input from user
    search_word = input("Enter the starting letter(s) to filter PDFs: ")
    
    # 4. Filter files that start with that word (case-insensitive)
    filtered_files = [f for f in all_files if f.lower().startswith(search_word.lower())]
    
    # 5. Display results
    print(f"\nFound {len(filtered_files)} file(s):")
    for i, file in enumerate(filtered_files):
        print(f"{i+1}: {file}")
        
    return filtered_files

# Run the selection
selected = select_pdfs()

"""
import os
import glob

# Path to your folder
path = r'/home/tux_106/Documents/PyProj/pra/'
os.chdir(path)

# Filter by user input
prefix = input("Enter prefix: ")
files = glob.glob(f"{prefix}*.pdf")

# Print found files
for f in files:
    print(f"Applying script to: {f}")
    # -- INSERT YOUR PDF PROCESSING LOGIC HERE --
"""