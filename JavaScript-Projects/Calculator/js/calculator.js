// Create an object to keep track of values
const Calculator = {
    displayValue: '0', // Display 0 on the calculator screen
    firstOperand: null, // Hold the first operand for any expressions, set to null for now
    waitSecondOperand: false, // Checks whether or not second operand has been inputted
    operator: null // Holds the operator, set to null for now
};

// Modify values each time a button is clicked on
function inputDigit(digit){
    const {displayValue,waitSecondOperand} = Calculator;
    if (waitSecondOperand === true) { // Checks if waitSecondOperand is true and sets displayValue to the key that was clicked.
        Calculator.displayValue = digit;
        Calculator.waitSecondOperand = false;
    } else { // Overwrites displayValue if the current value is 0, otherwise it adds onto it.
        Calculator.displayValue = displayValue === '0' ? digit : displayValue + digit;
    }
}

// Handles decimal points.
function inputDecimal(dot) {
    if (Calculator.waitSecondOperand === true) return; // This ensure that accidental clicking of decimal point doesn't cause bugs in the operation.
    if (!Calculator.displayValue.includes(dot)){
        Calculator.displayValue += dot; // We are saying if the displayValue does not contain a decimal point, we want to add a decimal point.
    }
}

// Handles operators
function handleOperator(nextOperator){
    const {firstOperand, displayValue, operator} = Calculator;
    const valueOfInput = parseFloat(displayValue); // When an operator key is pressed we convert the current number displayed on the screen to a number, and then store in calculator.firstOperand
    if (operator && Calculator.waitSecondOperand) { // Checks if operator already exists, and if waitSecondOperand is true, updates operator and exits from function.
        Calculator.operator = nextOperator;
        return;
    }
    if (firstOperand == null) {
        Calculator.firstOperand = valueOfInput;
    } else if (operator) { // Checks if an operator already exists
        const valueNow = firstOperand || 0;
        let result = performCalculation[operator](valueNow, valueOfInput); // If operator exists, property lookup is performed for the operator and the function that matches is executed.
        result = Number(result).toFixed (9); // We add a fixed amount of numbers after the decimal
        result = (result * 1).toString(); // This will remove any trailing 0's
        Calculator.displayValue = parseFloat(result);
        Calculator.firstOperand = parseFloat(result);

    }
    Calculator.waitSecondOperand = true;
    Calculator.operator = nextOperator;
}

// Calculation object
const performCalculation = {
    '/': (firstOperand, secondOperand) => firstOperand / secondOperand,
    '*': (firstOperand, secondOperand) => firstOperand * secondOperand,
    '+': (firstOperand, secondOperand) => firstOperand + secondOperand,
    '-': (firstOperand, secondOperand) => firstOperand - secondOperand,
    '=': (firstOperand, secondOperand) => secondOperand
};
function CalculatorReset() {
    Calculator.displayValue = '0';
    Calculator.firstOperand = null;
    Calculator.waitSecondOperand = false;
    Calculator.operator = null;
}
// Function that updates the calculator screen with the contents of displayValue
function updateDisplay(){
    const display = document.querySelector('.calculator-screen'); // Makes use of the calculator-screen class to target the input tag in the HTML document
    display.value = Calculator.displayValue;
}
updateDisplay();

// Monitors button clicks
const keys = document.querySelector('.calculator-keys');
keys.addEventListener('click', (event) => {
    const { target } = event; // The target variable is an object that represents the element that was clicked
    if (!target.matches('button')) { // If the element clicked on is not a button, exit function.
        return;
    }
    if (target.classList.contains('operator')) {
        handleOperator(target.value);
        updateDisplay();
        return;
    }
    if (target.classList.contains('decimal')) {
        inputDecimal(target.value);
        updateDisplay();
        return;
    }
    if (target.classList.contains('all-clear')) { // Ensures AC clears all inputs from the Calculator screen.
        CalculatorReset();
        updateDisplay();
        return;
    }
    inputDigit(target.value);
    updateDisplay();
})