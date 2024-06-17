from main_files.command import CopyCommand, PasteCommand, SortNamesCommand
from main_files.invoker import Button
from main_files.receiver import TextEditor, SortNames

def main():
    """
    This is the main function of the program.
    It initializes a TextEditor, SortNames, and several Button objects.
    Then it performs a series of actions by clicking the buttons.
    """
    editor = TextEditor()
    names = ['John', 'Jane', 'Doe','Alice', 'Bob', 'Eve', 'Michael']
    sorteador = SortNames(names)
    copy_button = Button(CopyCommand(editor))
    paste_button = Button(PasteCommand(editor))
    sort_names = Button(SortNamesCommand(sorteador))

    copy_button.click()
    paste_button.click()
    sort_names.click()

if __name__ == "__main__":
    main()