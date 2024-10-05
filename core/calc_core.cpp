#include <iostream>
#include <stack>
#include <sstream>
#include <string>
#include <cmath>
#include <stdexcept>
#include <unordered_map>

using namespace std;

double applyOperation(char operation, double a, double b) {
    switch (operation) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/':
            if (b == 0) throw runtime_error("АХТУНГ: происходит деление на ноль, негодник");
            return a / b;
        case '^': return pow(a, b);  // возведение в степень
        default:
            throw invalid_argument("АХТУНГ: неверный оператор");
    }
}

// обратная польская нотации
double calculateRPN(const string& expression) {
    stack<double> operands;
    istringstream tokens(expression);
    string token;

    while (tokens >> token) {
        if (isdigit(token[0])) {
            // если токен - число, помещаем его в стек
            operands.push(stod(token));
        } else if (token.size() == 1 && string("+-*/^").find(token) != string::npos) {
            // если токен - оператор, извлекаем два операнда и применяем оператор
            if (operands.size() < 2) {
                throw invalid_argument("АХТУНГ: недопустимое выражение для польской нотации");
            }
            double b = operands.top(); operands.pop();
            double a = operands.top(); operands.pop();
            double result = applyOperation(token[0], a, b);
            operands.push(result);
        } else {
            throw invalid_argument("АХТУНГ: недопустимый токен в выражении");
        }
    }

    if (operands.size() != 1) {
        throw invalid_argument("АХТУНГ: недопустимое выражение для польской нотации");
    }

    return operands.top();
}

// функции для арифметических операций
extern "C" {
    double add(double a, double b) {
        return a + b;
    }

    double subtract(double a, double b) {
        return a - b;
    }

    double multiply(double a, double b) {
        return a * b;
    }

    double divide(double a, double b) {
        if (b == 0) throw runtime_error("АХТУНГ: происходит деление на ноль, негодник");
        return a / b;
    }

    // функция для питона
    double calculate_rpn(const char* expression) {
        try {
            return calculateRPN(string(expression));
        } catch (const exception& e) {
            cerr << "Error: " << e.what() << endl;
            return NAN;
        }
    }
}
