import TkEasyGUI as eg

from presenter.presenter import Presenter
from presenter.handler import Handler
from view.view import Interface

def main():
    interface = Interface()
    presenter = Presenter(window=interface.window)
    handler = Handler(presenter)

    while True:
        event, values = interface.window.read()
        handler.handle(event, values)

        if event is None:
            break

        if event == eg.WIN_CLOSED:
            break

    interface.close()

if __name__ == '__main__':
    main()