#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

# 这是一个菜单接口，提供一个菜单允许用户输入他
# 们的选择

import sys
from notebook import Note,Notebook

class Menu:
    """
    显示一个菜单供用户选择
    """
    def __init__(self):
        self.notebook=Notebook()
        self.choices={
            "1":self.show_notes,
            "2":self.search_notes,
            "3":self.add_note,
            "4":self.modify_note,
            "5":self.quit
        }

    def display_menu(self):
        print("""
        Notebook Menu

        1.Show all Notes
        2.Search Note
        3.Add Note
        4.Modify Note
        5.Quit

        """)

    def run(self):
        """
        展示菜单和反馈用户选择
        :return:
        """
        while True:
            self.display_menu()
            choice=input("输入选项：")
            action=self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self,notes=None):
        if not notes:
            notes=self.notebook.notes
        for note in notes:
            print("{0}:{1}\n{2}".format(note.id,note.tags,note.memo))

    def search_notes(self):
        filter=input('Search for:')
        notes=self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo=input('Enter a memo:')
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_note(self):
        id=input('Enter a note id:')
        memo=input('Enter new memo：')
        tags=input('Enter new tags:')

        if memo:
            self.notebook.modify_memo(id,memo)
        if tags:
            self.notebook.modify_tags(id,tags)

    def quit(self):
        print('Thank you for using your notebook today.')
        sys.exit(0)


if __name__=="__main__":
    Menu().run()