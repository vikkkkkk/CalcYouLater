import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)   # создаю экземпляр приложения
    window = MainWindow()          # создаю главное окно
    window.show()                  # показываю окно
    sys.exit(app.exec_())          # запускаю главный цикл приложения

if __name__ == "__main__":
    main()
