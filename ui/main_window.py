import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QMainWindow, QWidget, QGridLayout, QPushButton, 
                             QLineEdit, QApplication, QMessageBox)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 300, 400)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QGridLayout(self.central_widget)
        
        # строка ввода для отображения результата
        self.result_line = QLineEdit()
        self.result_line.setReadOnly(True)
        self.result_line.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.result_line, 0, 0, 1, 4)

        # кнопочку "←" размещаю рядом со строкой ввода
        self.back_button = QPushButton("←")
        self.back_button.clicked.connect(lambda: self.on_button_click('←'))
        self.layout.addWidget(self.back_button, 0, 4)  # кнопка в первой строке, пятом столбце

        # кнопочки
        buttons = [
            'C', '+', '-', '*', '/', 
            '1', '2', '3', '√', '%', 
            '4', '5', '6', '(', ')', 
            '7', '8', '9', 'sin', 'cos', 
            '0', '.', '=', 'log', 'tan', 
            '%', '^', 'x', 'ctg', 'Graph'
        ]
        
        # создаю кнопочки и добавляю их в сетку
        for i, button in enumerate(buttons):
            self.create_button(button, i // 5 + 2, i % 5)  # начать со второй строки

        self.show()

    def create_button(self, text, row, col):
        button = QPushButton(text)
        button.clicked.connect(lambda: self.on_button_click(text))
        self.layout.addWidget(button, row, col)

    def on_button_click(self, text):
        if text == 'C':
            self.result_line.clear()
        elif text == '=':
            try:
                # заменяю ^ на ** перед выполнением выражения
                expression = self.result_line.text().replace('^', '**').replace(',', '.')
                result = eval(expression)
                self.result_line.setText(str(result))
            except Exception as e:
                self.result_line.setText("Ошибка")
        elif text == '←':
            current_text = self.result_line.text()
            self.result_line.setText(current_text[:-1])  # удаление последнего символа
        elif text in ('sin', 'cos', 'tan', 'ctg'):
            
            current_text = self.result_line.text()
            self.result_line.setText(f"{current_text}{text}(")  # убираю скобки, добавляю открывающую
        elif text == '√':
            current_text = self.result_line.text()
            self.result_line.setText(f"np.sqrt({current_text})")
        elif text == '%':
            current_text = self.result_line.text()
            self.result_line.setText(f"({current_text})/100")
        elif text == 'log':
            current_text = self.result_line.text()
            self.result_line.setText(f"np.log({current_text})")
        elif text == 'Graph':
            self.plot_graph()
        else:
            self.result_line.setText(self.result_line.text() + text)

    def plot_graph(self):
        try:
            expression = self.result_line.text()
            # создаю массив x
            x = np.linspace(-10, 10, 400)
            expression = expression.replace('^', '**').replace('ctg', '1/np.tan')
            
            # для вычисления выражения с массивом x
            y = eval(expression.replace('x', 'x'))
            
            # график
            plt.plot(x, y)
            plt.title(f'График функции: {expression}')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.axhline(0, color='black', linewidth=0.5, ls='--')
            plt.axvline(0, color='black', linewidth=0.5, ls='--')
            plt.ylim(-10, 10)
            plt.grid()
            plt.show()
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось построить график: {e}")

    def keyPressEvent(self, event):
        key = event.key()
        # обработка нажатия клавиш для цифр
        if key in (Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4,
                    Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9):
            self.on_button_click(str(key - Qt.Key_0))  # номер клавиши в строку
        elif key == Qt.Key_Plus:
            self.on_button_click('+')
        elif key == Qt.Key_Minus:
            self.on_button_click('-')
        elif key == Qt.Key_Asterisk:
            self.on_button_click('*')
        elif key == Qt.Key_Slash:
            self.on_button_click('/')
        elif key in (Qt.Key_Enter, Qt.Key_Return):
            self.on_button_click('=')
        elif key == Qt.Key_Backspace:
            self.on_button_click('←')
        elif key == Qt.Key_Period:
            self.on_button_click('.')
        elif key == Qt.Key_ParenLeft:
            self.on_button_click('(')
        elif key == Qt.Key_ParenRight:
            self.on_button_click(')')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
