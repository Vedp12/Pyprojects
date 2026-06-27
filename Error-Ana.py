with open ("Txt_file.txt","r") as file:
    error_count = 0
    for check in file:
        print(check)
        if "error" in check:
            error_count += 1
print(error_count)
