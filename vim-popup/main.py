import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow
from PySide6.QtCore import QTimer, Qt
from editor import Editor
import time

from pynput import keyboard
Controller = keyboard.Controller()
Key = keyboard.Key

from clip import Clipboard
clipboard = Clipboard(Controller)


class Application:
    def __init__(self):
        self.key_pressed = False
        self.app = QApplication(sys.argv)
        self.widget = QWidget()
        self.widget.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.editor = Editor(self.widget)
        self.widget.show()
        self.widget.raise_()
        self.widget.hide()

        self.timer = QTimer()
        self.listener = keyboard.Listener(on_release=self.on_release)
        self.listener.start()
        self.timer.timeout.connect(self.check_key_press)
        self.timer.start(100)

    def on_release(self, key):
        if key == Key.alt:
            clipboard.original = clipboard.current
            clipboard.copy()
            time.sleep(.1)
            self.key_pressed = True

    def check_key_press(self):
        if self.key_pressed:
            self.key_pressed = False
            if not self.editor.isVisible():
                self.widget.show()
                self.widget.raise_()
                self.editor.setText(clipboard.current)
                clipboard.current = clipboard.original
            else:
                clipboard.current = self.editor.toPlainText()
                self.widget.hide()
                Controller.press(Key.cmd)
                Controller.tap(Key.tab)
                Controller.release(Key.cmd)
                time.sleep(.5)
                Controller.press(Key.cmd)
                Controller.tap("v")
                Controller.release(Key.cmd)

    def run(self):
        sys.exit(self.app.exec())

if __name__ == "__main__":
    application = Application()
    application.run()