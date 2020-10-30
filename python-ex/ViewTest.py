import unittest
from unittest import mock
import sys

from qtpy.QtWidgets import QApplication
from qtpy.QtTest import QTest
from qtpy.QtCore import Qt

from View import View

app = QApplication(sys.argv)

class ViewTest(unittest.TestCase):

    def setUp(self):
        patch = mock.patch('View.Presenter')
        presenter = patch.start()
        self.addCleanup(patch.stop)
        self.mPresenter = presenter.return_value
        self.view = View()

    def test_init(self):
        self.assertEqual(self.view._nContacts, 0)
        self.mPresenter.onRead.assert_called_once()

    def test_addButtonPressed(self):
        self.view.firstNameField.text = mock.Mock()
        self.view.firstNameField.text.return_value = "test"
        self.view.lastNameField.text = mock.Mock()
        self.view.lastNameField.text.return_value = "test"
        self.view.addButtonPressed()
        # QTest.mouseClick(self.view.addButton, Qt.LeftButton)
        self.mPresenter.onAdd.assert_called_once_with("test", "test")


if __name__ == '__main__':
    unittest.main()

