#include <iostream>
#include <stack>
#include <sstream>
#include <string>
#include <cmath>
#include <stdexcept>
#include <unordered_map>
#include <cctype>

using namespace std;

bool isOperator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '^' || c == '%';
}

// проверка, является ли токен числом
bool isNumber(const string& token) {
    try {
        stod(token);  // попробуем преобразовать в число (тут творится магия)
        return true;
    } catch (...) {
        return false;
    }
}

bool isFunction(const string& token) {
    return token == "sin" || token == "cos" || token == "tan" || 
           token == "sqrt" || token == "log" || token == "ctg";
}

// приоритеты (важные какие) операторов
int getPrecedence(char op) {
    switch (op) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
        case '%':
            return 2;
        case '^':
            return 3;
        default:
            return 0;
    }
}

// преобразование инфиксной нотации в обратную польскую нотацию
string infixToRPN(const string& expression, double xValue) {
    stack<char> operators;
    ostringstream rpn;
    string token;

    for (size_t i = 0; i < expression.length(); ++i) {
        char c = expression[i];

        // без пробелов
        if (isspace(c)) {
            continue;
        }

        // если это цифра, переменная x или число с точкой
        if (isdigit(c) || c == 'x' || c == '.') {
            token += c;
            while (i + 1 < expression.length() && (isdigit(expression[i + 1]) || expression[i + 1] == '.')) {
                token += expression[++i];
            }
            if (token == "x") {
                rpn << xValue << " ";
            } else {
                rpn << token << " ";
            }
            token.clear();
        } 
        else if (isalpha(c)) {
            token += c;
            while (i + 1 < expression.length() && isalpha(expression[i + 1])) {
                token += expression[++i];
            }
            if (isFunction(token)) {
                operators.push('f');
            } else {
                throw invalid_argument("АХТУНГ: недопустимый токен в выражении: " + token);
            }
        }
        else if (c == '(') {
            operators.push('(');
        } else if (c == ')') {
            while (!operators.empty() && operators.top() != '(') {
                rpn << operators.top() << " ";
                operators.pop();
            }
            operators.pop();  // убираю скобку
        } 
        else if (isOperator(c)) {
            while (!operators.empty() && getPrecedence(operators.top()) >= getPrecedence(c)) {
                rpn << operators.top() << " ";
                operators.pop();
            }
            operators.push(c);
        } 
        else {
            throw invalid_argument("АХТУНГ: недопустимый токен в выражении: " + string(1, c));
        }
    }

    while (!operators.empty()) {
        rpn << operators.top() << " ";
        operators.pop();
    }

    return rpn.str();
}

// выполнение арифметической операции
double applyOperation(char operation, double a, double b) {
    switch (operation) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/':
            if (b == 0) throw runtime_error("АХТУНГ: происходит деление на ноль, негодник");
            return a / b;
        case '^': return pow(a, b);
        case '%': return fmod(a, b);
        default:
            throw invalid_argument("АХТУНГ: неверный оператор");
    }
}

// вычисление тригонометрических функций
double applyFunction(const string& function, double value) {
    if (function == "sin") return sin(value);
    if (function == "cos") return cos(value);
    if (function == "tan") return tan(value);
    if (function == "ctg") {
        if (value == 0) throw runtime_error("АХТУНГ: ctg не определен для этого значения");
        return 1 / tan(value);
    }
    if (function == "sqrt") {
        if (value < 0) throw invalid_argument("АХТУНГ: невозможно вычислить квадратный корень из отрицательного числа");
        return sqrt(value);
    }
    if (function == "log") {
        if (value <= 0) throw invalid_argument("АХТУНГ: логарифм из неположительного числа невозможен");
        return log(value);
    }
    throw invalid_argument("АХТУНГ: неверная математическая функция");
}

// вычисление выражения в обратной польской нотации
double calculateRPN(const string& expression) {
    stack<double> operands;
    istringstream tokens(expression);
    string token;

    while (tokens >> token) {
        if (isNumber(token)) {
            operands.push(stod(token));
        } else if (isalpha(token[0]) && isFunction(token)) {
            if (operands.empty()) {
                throw invalid_argument("АХТУНГ: недопустимое выражение для функции");
            }
            double value = operands.top(); operands.pop();
            operands.push(applyFunction(token, value));
        } else if (token.length() == 1 && isOperator(token[0])) {
            if (operands.size() < 2) {
                throw invalid_argument("АХТУНГ: недопустимое выражение для польской нотации");
            }
            double b = operands.top(); operands.pop();
            double a = operands.top(); operands.pop();
            operands.push(applyOperation(token[0], a, b));
        } else {
            throw invalid_argument("АХТУНГ: недопустимый токен в выражении: " + token);
        }
    }

    if (operands.size() != 1) {
        throw invalid_argument("АХТУНГ: недопустимое выражение для польской нотации");
    }

    return operands.top();
}

// функции для работы с питоном
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

    // вычисление выражения в инфиксной нотации с переменной x
    double calculate_infix(const char* expression, double xValue) {
        string rpn = infixToRPN(string(expression), xValue);
        return calculateRPN(rpn);
    }

    double calculate_rpn(const char* expression) {
        try {
            return calculateRPN(string(expression));
        } catch (const exception& e) {
            cerr << "Error: " << e.what() << endl;
            return NAN;
        }
    }
}
