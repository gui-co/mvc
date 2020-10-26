import sqlite3
import os


class Model:

    """
    SQLite connection
    """
    _connection = None

    """
    SQLite cursor.
    """
    _cursor = None

    """
    Set of contacts.
    """
    _contacts = set()

    def __init__(self):
        here = os.path.dirname(os.path.realpath(__file__))
        self._connection = sqlite3.connect(os.path.join(here, 'contacts.sqlite'))
        self._contacts = set()
        self._cursor = self._connection.cursor()
        try:
            self._cursor.execute("SELECT * FROM contacts")
            self._contacts = set(self._cursor.fetchall())
        except:
            self._cursor.execute("CREATE TABLE contacts ("
                                 "firstName TEXT,"
                                 "lastName  TEXT)")

    def __del__(self):
        self._connection.close()

    def addContact(self, firstName, lastName):
        """
        Add a contact.

        Args:
            firstName (str): contact first name
            lastName (str): contact last name

        Returns:
            bool: True if the contact has been added to the set
        """
        if (firstName, lastName) in self._contacts:
            return False
        self._contacts.add((firstName, lastName))
        self._cursor.execute("INSERT INTO contacts VALUES ('{0}', '{1}')"
                             .format(firstName, lastName))
        self._connection.commit()
        return True

    def getContacts(self):
        """
        Get all the contacts.

        Returns:
            set((str, str)): set of contacts (first name, last name)
        """
        return self._contacts

    def searchContact(self, lastName):
        return None

