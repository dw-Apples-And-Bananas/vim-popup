from pynput.keyboard import Controller, Key
import pyperclip


class Clipboard:
    _current:str
    def __init__(self, keyboard:Controller):
        self.keyboard = keyboard

    @property
    def current(self):
        self._current = pyperclip.paste()
        return self._current

    @current.setter
    def current(self, value):
        pyperclip.copy(value)

    def cmd_tap(self, key):
        self.keyboard.press(Key.cmd)
        self.keyboard.tap(key)
        self.keyboard.release(Key.cmd)

    def copy(self): self.cmd_tap("c")
    def paste(self):self.cmd_tap("v")
