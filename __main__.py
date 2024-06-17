from main_files.command import CopyCommand, PasteCommand
from main_files.invoker import Button
from main_files.receiver import TextEditor


# Rest of your code

def main():
    editor = TextEditor()
    copy_button = Button(CopyCommand(editor))
    paste_button = Button(PasteCommand(editor))

    copy_button.click()
    paste_button.click()

if __name__ == "__main__":
    main()