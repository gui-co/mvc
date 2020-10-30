import os

from qtpy.QtCore import *
from qtpy.QtWidgets import QMainWindow, QLabel
from qtpy import uic

from Presenter import Presenter


class View(QMainWindow):

    """
    Reference to the presenter.
    """
    _presenter = None

    """
    Number of contacts.
    """
    _nContacts = 0

    def __init__(self, parent=None):
        super(View, self).__init__(parent)
        here = os.path.dirname(os.path.realpath(__file__))
        uic.loadUi(os.path.join(here, "view.ui"), self)
        self._presenter = Presenter(self)
        self._nContacts = 0
        self.addButton.clicked.connect(self.addButtonPressed)
        # self.searchButton.clicked.connect(self.searchButtonPressed)
        self.searchField.textEdited.connect(self.searchButtonPressed)
        self._presenter.onRead()

    def addContact(self, firstName, lastName):
        """
        Add a contact on the displayed list.

        Args:
            firstName (str): contact first name
            lastName (str): contact last name
        """
        self.contactsList.addWidget(QLabel(firstName), self._nContacts, 0)
        self.contactsList.addWidget(QLabel(lastName), self._nContacts, 1)
        self._nContacts += 1

    def addButtonPressed(self):
        """
        Triggered when the 'add' button is pressed.
        """
        firstName = self.firstNameField.text()
        lastName = self.lastNameField.text()
        if firstName and lastName:
            self.firstNameField.clear()
            self.lastNameField.clear()
            self._presenter.onAdd(firstName, lastName)

    def searchButtonPressed(self):
        self._presenter.onSearch(self.searchField.text())

    def setSearchResults(self, results):
        for i in reversed(range(self.searchResults.count())):
            self.searchResults.itemAt(i).widget().setParent(None)

        n = 0
        for contact in results:
            self.searchResults.addWidget(QLabel(contact[0]), n, 0)
            self.searchResults.addWidget(QLabel(contact[1]), n, 1)
            n += 1

