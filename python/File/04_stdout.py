import sys
print("this is message for standard output")
print("this is message for standard output",file = sys.stdout)
sys.stdout.write("This is message for standard output")