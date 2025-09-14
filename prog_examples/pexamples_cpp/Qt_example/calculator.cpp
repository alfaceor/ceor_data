#include <iostream>
#include <string>
#include <vector>
#include <map>

#include <QApplication>
#include <QWidget>
#include <QVBoxLayout>
#include <QPushButton>
#include <QLabel>
#include <QLineEdit>
#include <QDoubleValidator>
#include <QCommandLineParser>
#include <QMessageBox>

// =========================================================================
// Core Application Logic (GUI-agnostic)
// This is the heart of your application. It contains all the
// business logic and should not depend on any GUI libraries.
// It can be compiled as a static or dynamic library.
// =========================================================================

class CalculatorCore {
public:
    static double add(double a, double b) {
        return a + b;
    }
    static double subtract(double a, double b) {
        return a - b;
    }
    static double multiply(double a, double b) {
        return a * b;
    }
    static double divide(double a, double b) {
        if (b == 0.0) {
            throw std::runtime_error("Division by zero is not allowed.");
        }
        return a / b;
    }
};

// =========================================================================
// Command-Line Interface (CLI)
// This function handles the application's CLI mode.
// It parses arguments and calls the core logic.
// =========================================================================

int runCLI(int argc, char *argv[]) {
    // Use Qt's powerful command-line parser
    QCoreApplication a(argc, argv);
    QCommandLineParser parser;
    parser.setApplicationDescription("Cross-platform CLI and GUI application.");
    parser.addHelpOption();
    parser.addVersionOption();

    // Define the command-line options
    parser.addOption({"o", "operation", "Specify the operation (add, subtract, multiply, divide)."});
    parser.addOption({"v1", "value1", "The first value."});
    parser.addOption({"v2", "value2", "The second value."});

    parser.process(a);

    // Get the values from the command line
    const QString operation = parser.value("operation");
    const QString value1Str = parser.value("value1");
    const QString value2Str = parser.value("value2");

    // Check for required arguments
    if (operation.isEmpty() || value1Str.isEmpty() || value2Str.isEmpty()) {
        parser.showHelp(1);
        return 1;
    }

    // Convert string arguments to double
    bool ok1, ok2;
    double val1 = value1Str.toDouble(&ok1);
    double val2 = value2Str.toDouble(&ok2);

    if (!ok1 || !ok2) {
        std::cerr << "Error: Invalid numeric values provided." << std::endl;
        return 1;
    }

    double result = 0.0;
    try {
        if (operation == "add") {
            result = CalculatorCore::add(val1, val2);
        } else if (operation == "subtract") {
            result = CalculatorCore::subtract(val1, val2);
        } else if (operation == "multiply") {
            result = CalculatorCore::multiply(val1, val2);
        } else if (operation == "divide") {
            result = CalculatorCore::divide(val1, val2);
        } else {
            std::cerr << "Error: Unknown operation '" << operation.toStdString() << "'." << std::endl;
            return 1;
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    std::cout << "Result: " << result << std::endl;
    return 0;
}

// =========================================================================
// Graphical User Interface (GUI)
// This function handles the application's GUI mode.
// It creates a window and uses the same core logic.
// =========================================================================

int runGUI(int argc, char *argv[]) {
    QApplication app(argc, argv);
    QWidget window;
    window.setWindowTitle("Calculator GUI");
    window.setFixedSize(300, 200);

    QVBoxLayout *layout = new QVBoxLayout(&window);

    QLabel *label1 = new QLabel("Value 1:");
    QLineEdit *line1 = new QLineEdit();
    line1->setValidator(new QDoubleValidator());

    QLabel *label2 = new QLabel("Value 2:");
    QLineEdit *line2 = new QLineEdit();
    line2->setValidator(new QDoubleValidator());

    QLabel *resultLabel = new QLabel("Result: ");

    QHBoxLayout *buttonLayout = new QHBoxLayout();
    QPushButton *addButton = new QPushButton("Add");
    QPushButton *subButton = new QPushButton("Subtract");
    QPushButton *mulButton = new QPushButton("Multiply");
    QPushButton *divButton = new QPushButton("Divide");

    buttonLayout->addWidget(addButton);
    buttonLayout->addWidget(subButton);
    buttonLayout->addWidget(mulButton);
    buttonLayout->addWidget(divButton);

    layout->addWidget(label1);
    layout->addWidget(line1);
    layout->addWidget(label2);
    layout->addWidget(line2);
    layout->addWidget(resultLabel);
    layout->addLayout(buttonLayout);

    // Connect signals to slots (using C++ lambdas for simplicity)
    QObject::connect(addButton, &QPushButton::clicked, [&]() {
        bool ok1, ok2;
        double val1 = line1->text().toDouble(&ok1);
        double val2 = line2->text().toDouble(&ok2);
        if (ok1 && ok2) {
            double result = CalculatorCore::add(val1, val2);
            resultLabel->setText(QString("Result: %1").arg(result));
        } else {
            QMessageBox::warning(&window, "Input Error", "Please enter valid numbers.");
        }
    });

    QObject::connect(subButton, &QPushButton::clicked, [&]() {
        bool ok1, ok2;
        double val1 = line1->text().toDouble(&ok1);
        double val2 = line2->text().toDouble(&ok2);
        if (ok1 && ok2) {
            double result = CalculatorCore::subtract(val1, val2);
            resultLabel->setText(QString("Result: %1").arg(result));
        } else {
            QMessageBox::warning(&window, "Input Error", "Please enter valid numbers.");
        }
    });

    QObject::connect(mulButton, &QPushButton::clicked, [&]() {
        bool ok1, ok2;
        double val1 = line1->text().toDouble(&ok1);
        double val2 = line2->text().toDouble(&ok2);
        if (ok1 && ok2) {
            double result = CalculatorCore::multiply(val1, val2);
            resultLabel->setText(QString("Result: %1").arg(result));
        } else {
            QMessageBox::warning(&window, "Input Error", "Please enter valid numbers.");
        }
    });

    QObject::connect(divButton, &QPushButton::clicked, [&]() {
        bool ok1, ok2;
        double val1 = line1->text().toDouble(&ok1);
        double val2 = line2->text().toDouble(&ok2);
        if (ok1 && ok2) {
            try {
                double result = CalculatorCore::divide(val1, val2);
                resultLabel->setText(QString("Result: %1").arg(result));
            } catch (const std::exception& e) {
                QMessageBox::critical(&window, "Runtime Error", e.what());
            }
        } else {
            QMessageBox::warning(&window, "Input Error", "Please enter valid numbers.");
        }
    });

    window.show();
    return app.exec();
}

// =========================================================================
// Main Entry Point
// This is where the decision is made to run either the CLI or the GUI.
// =========================================================================

int main(int argc, char *argv[]) {
    // If command-line arguments are provided, run the CLI
    if (argc > 1) {
        return runCLI(argc, argv);
    }
    // Otherwise, run the GUI
    else {
        return runGUI(argc, argv);
    }
}

