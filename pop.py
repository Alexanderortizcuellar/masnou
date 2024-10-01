from PyQt5.QtWidgets import QApplication, QTextEdit, QCompleter
from PyQt5.QtCore import QStringListModel, Qt


class CompleterTextEdit(QTextEdit):
    def __init__(self, words, parent=None):
        super().__init__(parent)

        # Set up the completer with the list of words
        self.completer = QCompleter(words, self)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

        self.completer.setWidget(self)
        self.completer.activated.connect(self.insert_completion)
        #self.completer.highlighted.connect(self.insert_completion)

    def insert_completion(self, completion):
        cursor = self.textCursor()
        extra = len(completion) - len(self.completer.completionPrefix())
        cursor.movePosition(cursor.Left, cursor.KeepAnchor, extra)
        cursor.insertText(completion)
        self.setTextCursor(cursor)

    def text_under_cursor(self):
        cursor = self.textCursor()
        cursor.select(cursor.WordUnderCursor)
        return cursor.selectedText()

    def keyPressEvent(self, event):
        super().keyPressEvent(event)

        completion_prefix = self.text_under_cursor()
        if len(completion_prefix) < 1:
            self.completer.popup().hide()
            return

        # If there's a valid prefix, update the completer and show suggestions
        self.completer.setCompletionPrefix(completion_prefix)
        cr = self.cursorRect()
        cr.setWidth(
            self.completer.popup().sizeHintForColumn(0)
            + self.completer.popup().verticalScrollBar().sizeHint().width()
        )
        self.completer.complete(cr)  # Show the completer at the current cursor position


app = QApplication([])

# List of words for completion
words = ["guava", "banana", "banano", "bananas", "bananitos"]

# Create the custom QTextEdit with autocompletion
text_edit = CompleterTextEdit(words)

# Show the text edit
text_edit.show()

app.exec_()
