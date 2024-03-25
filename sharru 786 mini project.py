#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from tabulate import tabulate

contact_dict = {}


class ContactManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contact Manager")
        self.layout = QVBoxLayout()

        self.name_label = QLabel("Contact Name:")
        self.name_input = QLineEdit()

        self.number_label = QLabel("Contact Number:")
        self.number_input = QLineEdit()

        self.email_label = QLabel("Contact Email:")
        self.email_input = QLineEdit()

        self.add_button = QPushButton("Add Contact")
        self.add_button.clicked.connect(self.add_contact)

        self.view_button = QPushButton("View Contacts")
        self.view_button.clicked.connect(self.view_contact)

        self.search_label = QLabel("Search Contact:")
        self.search_input = QLineEdit()

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_contact)

        self.delete_label = QLabel("Delete Contact:")
        self.delete_input = QLineEdit()

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_contact)

        self.text_output = QTextEdit()

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.number_label)
        self.layout.addWidget(self.number_input)
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.view_button)
        self.layout.addWidget(self.search_label)
        self.layout.addWidget(self.search_input)
        self.layout.addWidget(self.search_button)
        self.layout.addWidget(self.delete_label)
        self.layout.addWidget(self.delete_input)
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.text_output)

        self.setLayout(self.layout)

    def add_contact(self):
        name = self.name_input.text()
        number = self.number_input.text()
        email = self.email_input.text()

        contact_dict.update({name: (number, email)})

        self.name_input.clear()
        self.number_input.clear()
        self.email_input.clear()

    def view_contact(self):
        contact_table = tabulate(contact_dict.items(), headers=["Contact Name", "Contact Details"])
        self.text_output.setPlainText(contact_table)

    def search_contact(self):
        s_name = self.search_input.text()
        if s_name in contact_dict:
            contact_info = contact_dict[s_name]
            self.text_output.setPlainText(f"Contact is present in dictionary\n{s_name}: {contact_info}")
        else:
            self.text_output.setPlainText("Contact not present")

        self.search_input.clear()

    def delete_contact(self):
        d_name = self.delete_input.text()
        if d_name in contact_dict:
            contact_dict.pop(d_name)
            self.text_output.setPlainText(f"Contact '{d_name}' deleted.")
        else:
            self.text_output.setPlainText("Contact not found.")

        self.delete_input.clear()


if __name__ == "__main__":
    app = QApplication([])
    contact_manager = ContactManager()
    contact_manager.show()
    app.exec_()


# In[ ]:




