from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QKeyEvent, QTextCursor
from spellchecker import SpellChecker
spell = SpellChecker()

NORMAL = "NORMAL"
INSERT = "INSERT"

class Editor(QTextEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self._mode = NORMAL
        self.setCursorWidth(8)
        self.setFontFamily("Menlo")

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if value == NORMAL:
            self.setCursorWidth(8)
        elif value == INSERT:
            self.setCursorWidth(1)
        self._mode = value

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == 16777216:
            self.mode = NORMAL
        if self.mode == INSERT:
            return super().keyPressEvent(event)
        if event.key() == 73:
            self.mode = INSERT
        if event.key() == 65 and self.mode == NORMAL:
            html = self.toHtml()
        print(event.key())

    def keyReleaseEvent(self, event:QKeyEvent):
        cursor = self.textCursor()
        pos = self.textCursor().position()
        text = self.toPlainText()
        before, after = text[0:pos].split(" ")[-1], text[pos::].split(" ")[0]
        start, end = pos-len(before), pos+len(after)
        word = before+after


        # a = text[0:pos].split(" ")
        # a[-1] = "<u>"+a[-1]
        # b = text[pos::].split(" ")
        # b[0] += "</u>"
        # new = " ".join(a)+" ".join(b)
        # print(new)
        
        # self.setHtml(new)
        # cursor.movePosition(QTextCursor.Left, QTextCursor.MoveAnchor, pos)
        # self.setTextCursor(cursor)
