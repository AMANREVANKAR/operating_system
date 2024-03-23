import cmd
import os
import shutil

class CommandForgeCLI(cmd.Cmd):
    prompt = 'CommandForge>> '
    intro = 'Welcome to CommandForgeCLI. Type "help" for available commands.'

    def __init__(self):
        super().__init__()
        self.current_directory = os.getcwd()
        self.favorites = []

    def do_list(self, line):
        """List files and directories in the current directory."""
        files_and_dirs = os.listdir(self.current_directory)
        for item in files_and_dirs:
            print(item)

    def do_change_dir(self, directory):
        """Change the current directory."""
        new_dir = os.path.join(self.current_directory, directory)
        if os.path.exists(new_dir) and os.path.isdir(new_dir):
            self.current_directory = new_dir
            print(f"Current directory changed to {self.current_directory}")
        else:
            print(f"Directory '{directory}' does not exist.")

    def do_create_file(self, filename):
        """Create a new text file in the current directory."""
        file_path = os.path.join(self.current_directory, filename)
        try:
            with open(file_path, 'w') as new_file:
                print(f"File '{filename}' created in {self.current_directory}")
        except Exception as e:
            print(f"Error: {e}")

    def do_read_file(self, filename):
        """Read the contents of a text file in the current directory."""
        file_path = os.path.join(self.current_directory, filename)
        try:
            with open(file_path, 'r') as existing_file:
                print(existing_file.read())
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def do_delete_file(self, filename):
        """Delete a file in the current directory."""
        file_path = os.path.join(self.current_directory, filename)
        try:
            os.remove(file_path)
            print(f"File '{filename}' deleted from {self.current_directory}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def do_copy_file(self, args):
        """Copy a file to another location."""
        args = args.split()
        if len(args) != 2:
            print("Usage: copy_file <source_file> <destination_directory>")
            return
        source_file = os.path.join(self.current_directory, args[0])
        destination_dir = os.path.join(self.current_directory, args[1])
        try:
            shutil.copy(source_file, destination_dir)
            print(f"File '{args[0]}' copied to '{args[1]}'")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error: {e}")

    def do_move_file(self, args):
        """Move a file to another location."""
        args = args.split()
        if len(args) != 2:
            print("Usage: move_file <source_file> <destination_directory>")
            return
        source_file = os.path.join(self.current_directory, args[0])
        destination_dir = os.path.join(self.current_directory, args[1])
        try:
            shutil.move(source_file, destination_dir)
            print(f"File '{args[0]}' moved to '{args[1]}'")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error: {e}")

    def do_fav(self, filename):
        """Add a file to favorites."""
        file_path = os.path.join(self.current_directory, filename)
        if os.path.exists(file_path):
            if file_path not in self.favorites:
                self.favorites.append(file_path)
                print(f"File '{filename}' added to favorites.")
            else:
                print(f"File '{filename}' is already in favorites.")
        else:
            print(f"File '{filename}' not found.")

    def do_show_favorites(self, line):
        """Show all favorite files."""
        if self.favorites:
            print("Favorite Files:")
            for file_path in self.favorites:
                print(os.path.basename(file_path))
        else:
            print("No favorite files.")

    def do_quit(self, line):
        """Exit the CLI."""
        return True

    def postcmd(self, stop, line):
        print()  # Add an empty line for better readability
        return stop

if __name__ == '__main__':
    CommandForgeCLI().cmdloop()
