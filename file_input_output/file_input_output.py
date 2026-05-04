#file input/output in python - reading and writing files

from pathlib import Path

#get path to demo_file.txt (next to this script)
demo_path = Path(__file__).resolve().parent / "demo_file.txt"
write_path = Path(__file__).resolve().parent / "writtenfile.txt"

print("=== READING FILES ===")

#1. readlines() - returns list of lines
with open(demo_path, "r") as file:
    lines_list = file.readlines()
    print("readlines():", lines_list)

print()

#2. read() - returns whole file as string
with open(demo_path, "r") as file:
    content_string = file.read()
    print("read():", repr(content_string))  #repr shows \n characters

print()

#3. reading line by line in a loop
print("line by line:")
with open(demo_path, 'r') as file:
    for line_num, line in enumerate(file, 1):
        print(f"  line {line_num}: {line.strip()}")  #strip removes \n

print()

#4. read and clean up newlines
with open(demo_path, 'r') as file:
    content = file.read()
    print("without trailing newline:", repr(content.rstrip()))

print("\n=== WRITING FILES ===")

#5. writing to file (overwrites existing)
with open(write_path, 'w') as file:
    file.write("This is line 1\n")
    file.write("This is line 2\n")
    print("wrote new content to writtenfile.txt")

#6. reading what we just wrote
with open(write_path, 'r') as file:
    print("file contains:", file.read())

#7. appending to file (adds to end)
with open(write_path, 'a') as file:
    file.write("This is line 3 (appended)\n")
    print("appended line 3")

#8. reading after append
with open(write_path, 'r') as file:
    print("file now contains:")
    for line in file:
        print("  ", line.strip())

print("\n=== FILE MODES ===")
print("'r' = read only")
print("'w' = write (overwrites existing file)")  
print("'a' = append (adds to end)")
print("'r+' = read and write")