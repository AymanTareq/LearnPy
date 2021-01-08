
## This is original script of exercise 17.
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

in_file = open(from_file)
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes long.")

print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit RETURN to continue , CTRL-C to abort.")
input('>')
out_file = open(to_file,'w')
out_file.write(in_data)

print("Allright, all done.")

out_file.close()
in_file.close()

# ## let's do this in shorter way.
# from_file = input("Enter the filename:")
# to_file = input("Enter the new filename:")

# content = open(from_file).read()
# f_obj = open(to_file,'w')
# f_obj.write(content)
# f_obj.close()

# print("You copied {} to {}".format(from_file,to_file))