import os

# current working directory
def present():
    print(f"\033[32m\nPresent directory: {os.getcwd()}\n\033[0m")
    ch = input(f"\nEnter to exit ")


# list the content of directory
def list_directory(path="."):
    print(f"\033[32m\nContent of {os.path.abspath(path)} : \033[0m")
    for item in os.listdir(path):
        print(f" - {item}")
    print()
    ch = input(f"\nEnter to exit ")


# change the current working directory
def change_directory(path):
    try:
        os.chdir(path)
        print(f"\033[32m\nDirectory changed to {os.path.abspath(path)} \033[0m")
    except FileNotFoundError:
        print(f"\033[31m\nError : Directory {path} not found \033[0m")
    finally:
        ch = input(f"\nEnter to exit ")

# open and read file
def open_file(path):
    try:
        with open(path, 'r') as file:
            print(f"\033[32m\nFile {os.path.abspath(path)} opened \033[0m")
            print(file.read())
            file.close()
    except FileNotFoundError:
        print(f"\033[31m\nError : File {path} not found \033[0m")
    except PermissionError:
        print(f"\033[31m\nError : Permission denied to open file {path} \033[0m")
    finally:
        ch = input(f"\nEnter to exit ")

# edit file with options to modify, delete or append lines
def edit_file(file_path):
    try:
        with open(file_path, 'r') as file:
            print(f"\033[32m\nFile {os.path.abspath(file_path)} opened \033[0m")
            lines = file.readlines()
            print(f"\033[32m\nCurrent file content:\033[0m")

        i = 1
        for line in lines:
            print(f"{i} - {line}", end="")
            i += 1
        text = "\n\nEdit Mode:\nOptions:\n - Enter 'm <line_number>' to modify a line.\n - Enter 'd <line_number>' to delete a line.\n - Enter 'a' to append a new line.\n - Enter 'save' to save changes and exit.\n - Enter 'cancel' to discard changes and exit.\n"
        print(f"\033[32m{text}\033[0m")
        while True:
            command = input("> ").strip()
            if command.lower() == 'save':
                # Save changes back to the file
                with open(file_path, 'w') as file:
                    file.writelines(lines)
                print(f"\033[32m\nFile saved successfully!\033[0m")
                break
            elif command.lower() == 'cancel':
                print(f"\033[32m\nChanges discarded!\033[0m")
                break
            elif command.startswith('m '):
                # Modify a specific line
                try:
                    line_no = int(command.split()[1])
                    if 1 <= line_no <= len(lines):
                        new_content = input(f"\nEnter new content for line {line_no}: ")
                        lines[line_no - 1] = new_content + '\n'
                        print(f"\033[32m\nLine {line_no} updated.\033[0m")
                    else:
                        print(f"\033[31m\nError : Line number out of range.\033[0m")
                except ValueError:
                    print(f"\033[32m\nError : Invalid line number.\033[0m")
            elif command.startswith('d '):
                # Delete a specific line
                try:
                    line_no = int(command.split()[1])
                    if 1 <= line_no <= len(lines):
                        lines.pop(line_no - 1)
                        print(f"\033[32m\nLine {line_no} deleted.\033[0m")
                    else:
                        print(f"\033[31m\nError : Line number out of range.\033[0m")
                except ValueError:
                    print(f"\033[31m\nError : Invalid line number.\033[0m")
            elif command.lower() == 'a':
                # Append a new line at the end
                new_content = input("\nEnter new line content:\n> ")
                lines.append(new_content + '\n')
                print(f"\033[32m\nNew line appended.\033[0m")
            else:
                print(f"\033[31m\nError: Invalid command. Please try again.\033[0m")

    except FileNotFoundError:
        print(f"\033[31m\nError: File not found!\033[0m")
    except PermissionError:
        print(f"\033[31m\nError: Permission denied!\033[0m")
    except Exception as e:
        print(f"\033[31m\nAn unexpected error occurred: {e}\033[0m")
    finally:
        ch = input(f"\nEnter to exit ")
    

# create a new file
def create_file(path):
    try:
        with open(path, 'w') as file:
            print(f"\033[32m\nFile {os.path.abspath(path)} created successfully.\033[0m")
    except:
        print(f"\033[31m\nError: Unable to create file {os.path.abspath(path)}\033[0m")
    finally:
        ch = input(f"\nEnter to exit ")


# run a Python script
def run_python_script(path):
    if not path.endswith('.py'):
        print(f"\033[31m\nError: Only Python (.py) files can be executed!\033[0m")
        ch = input(f"\nEnter to exit ")
        return
    if not os.path.exists(path):
        print(f"\033[31m\nError: File not found!\033[0m")
        ch = input(f"\nEnter to exit ")
        return
    print(f"\033[32m\nRunning Python script: {path}\n\033[0m")
    os.system(f'python "{path}"')
    ch = input(f"\nEnter to exit ")



# main function for main menu
def main():
    while True:
        print("\033[2J\033[H", end="")
        note = """/====================================================================\\
|| ╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐  ╔═╗┬┬  ┌─┐  ╔╦╗┌─┐┌┐┌┌─┐┌─┐┌─┐┬─┐ ||
|| ║║║├┤ │  │  │ ││││├┤    │ │ │  ╠╣ ││  ├┤   ║║║├─┤│││├─┤│ ┬├┤ ├┬┘ ||
|| ╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘  ╚  ┴┴─┘└─┘  ╩ ╩┴ ┴┘└┘┴ ┴└─┘└─┘┴└─ ||
\\====================================================================/"""
        print(f"{note}\n\n\n")
        print(f"\033[33mMAIN MENU :\n\n- pwd : Present directory\n- ls : List Directory\n- cd : Change Directory\n- o : Open File\n- e : Edit File\n- mk : Create a File\n- run : Run Python Script\n- exit : Exit\n\033[0m")
        
        choice = input("Enter your choice :\n> ")
        if choice == 'pwd':
            present()
        elif choice == 'ls':
            list_directory()
        elif choice == 'cd':
            path = input("\nEnter directory path:\n> ")
            change_directory(path)
        elif choice == 'o':
            path = input("\nEnter file path:\n> ")
            open_file(path)
        elif choice == 'e':
            path = input("\nEnter file path:\n> ")
            edit_file(path)
        elif choice == 'mk':
            path = input("\nEnter file name:\n> ")
            create_file(path)
        elif choice == 'run':
            path = input("\nEnter Python script path:\n> ")
            run_python_script(path)
        elif choice == 'exit':
            bye = """:   ____    U  ___ u   U  ___ u  ____    ____   __   __U _____ u     _   :
:U /"___|u   \\/"_ \\/    \\/"_ \\/ |  _"\\U | __")u \\ \\ / /\\| ___"|/   U|"|u :
:\\| |  _ /   | | | |    | | | |/| | | |\\|  _ \\/  \\ V /  |  _|"     \\| |/ :
: | |_| |.-,_| |_| |.-,_| |_| |U| |_| |\\| |_) | U_|"|_u | |___      |_|  :
:  \\____| \\_)-\\___/  \\_)-\\___/  |____/ u|____/    |_|   |_____|     (_)  :
:  _)(|_       \\\\         \\\\     |||_  _|| \\\\_.-,//|(_  <<   >>     |||_ :
: (__)__)     (__)       (__)   (__)_)(__) (__)\\_) (__)(__) (__)   (__)_):"""
            print(f"\n{bye}\n")
            ch = input('Enter to exit ')
            break
        else:
            print(f"\033[31m\nInvalid choice. Please choose a valid option.\033[0m")
main()