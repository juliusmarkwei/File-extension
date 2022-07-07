"""

print out any file's extension

"""

filename = input("Input the Filename >: ")
file_extension = filename.split(".")
if "." in filename:
    print("The extension of the file is : " + repr(file_extension[-1]))
else:
    print("\nEnter filename with extension".upper())
