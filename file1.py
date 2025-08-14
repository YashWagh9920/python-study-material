file = open('Exp03.txt','w')
file.write("This is the write command\n")
file.write("It allows us to write in a particular file\n")
file.write('Welcome to SIES GST\n')
file = open('Exp03.txt', 'a')
file.write("This will add this line")
file = open('Exp03.txt', 'r')
#-------------------------------------------------------------------------------
for each in file:
 print (each)
file= open('Exp03.txt','r') 
content=file.read()
print('content using read():',content)
file= open('Exp03.txt','r') 
content=file.readline()
print('content using readline():',content)
file= open('Exp03.txt','r') 
content=file.readlines()
print('content using readline():',content)
file.close()
#-------------------------------------------------------------------------------
file_path = "Exp04.txt"
try:
 # Attempt to open the file in read mode
 with open(file_path, "r") as file:
 # Read content from the file
  content = file.read()
 print("Content of the file:")
 print(content)
except FileNotFoundError:
 # Handle the case where the file does not exist
 print(f"Error: File '{file_path}' not found.")
except PermissionError:
 # Handle the case where permission to open the file is denied
 print(f"Error: Permission denied to open the file '{file_path}'.")
except Exception as e:
 # Handle any other exceptions that might occur
 print(f"An error occurred: {e}")
#-----------------------------------------------------------------------------
 import os
from pathlib import Path

def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
#-----------------------------------------------------------------------------
import os

def delete_directory(directory_name):
    try:
        os.rmdir(directory_name)
        print(f"Directory '{directory_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory_name}' does not exist.")
    except OSError as e:
        print(f"Error deleting directory '{directory_name}': {e}")
#-----------------------------------------------------------------------------
def check_directory_exists(directory_name):
 if os.path.exists(directory_name):
  print(f"Directory '{directory_name}' exists.")
 else:
  print(f"Directory '{directory_name}' does not exist.")
#-----------------------------------------------------------------------------
import os

def list_directory_contents(directory_name):
    try:
        contents = os.listdir(directory_name)
        print(f"Contents of directory '{directory_name}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Directory '{directory_name}' does not exist.")
#-----------------------------------------------------------------------------
def change_working_directory(new_directory):
 try:
  os.chdir(new_directory)
  print(f"Changed working directory to '{new_directory}'.")
 except FileNotFoundError:
  print(f"Directory '{new_directory}' does not exist.")
 except PermissionError:
  print(f"No permission to access directory '{new_directory}'.")
#-----------------------------------------------------------------------------
def get_current_working_directory():
 cwd = os.getcwd()
 print(f"Current working directory: {cwd}")
if __name__ == "__main__":
 # Test the functions
 create_directory("Experiments_directory")
 check_directory_exists("Experiments_directory")
 list_directory_contents("Experiments_directory")
 change_working_directory("Experiments_directory")
 get_current_working_directory()
 delete_directory("Experiments_directory")
#-----------------------------------------------------------------------------



