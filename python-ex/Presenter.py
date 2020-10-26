from Model import Model


class Presenter:

    """
    Reference to the view.
    """
    _view = None

    """
    Reference to the model.
    """
    _model = None

    def __init__(self, view):
        self._view = view
        self._model = Model()

    def onAdd(self, firstName, lastName):
        """
        Triggered when a new contact has to be added.
        """
        ok = self._model.addContact(firstName, lastName)
        if ok:
            self._view.addContact(firstName, lastName)

    def onRead(self):
        """
        Read all the saved contacts and add them to the view.
        """
        contacts = self._model.getContacts()
        for c in contacts:
            self._view.addContact(c[0], c[1])

    def onSearch(self, key):
        """
        Triggered by search action.
        """
        results = self._model.searchContact(key)
        self._view.setSearchResults(results)

