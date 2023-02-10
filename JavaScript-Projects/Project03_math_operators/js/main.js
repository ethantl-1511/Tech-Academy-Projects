function addition_function() {  // This function will do addition.
	var addition = 2 + 2;
	document.getElementById("add").innerHTML = "2 + 2 = " + addition;
}

function subtraction_function() {  // This function will do subtraction.
    var subtraction = 5 - 2;
    document.getElementById("subtract").innerHTML = "5 - 2 = " + subtraction;
}

function multiply() {  // This function will do multiplication.
    var multiply = 6 * 8;
    document.getElementById("multiply").innerHTML = "6 * 8 = " + multiply;
}

function division() {  // This function will do division.
    var divide = 48 / 6;
    document.getElementById("divide").innerHTML = "48 / 6 = " + divide;
}

function equation() {   // This function will do long math.
    var math = (1 + 2) * 10 / 2 - 5;
    document.getElementById("Math").innerHTML = "1 + 2, times 10, divided by 2, minus 5 equals " + math;
}

function remainder() {   // This function will give the remainder.
    var remainder =  25 % 6;
    document.getElementById("mod").innerHTML = "25 divided by 6 gives remainder of: " + remainder;
}

function negation() {  // This function will use the negation operator.
	var x = 10;
	document.getElementById("negative").innerHTML = "x = " + -x;
}

function increment() {    // This function will increment the value.
    var X = 5;
    X++;
    document.getElementById("increment").innerHTML = X
}

function decrement() {    // This function will decrement the value.
    var Y = 5.25;
    Y--;
    document.getElementById("decrement").innerHTML = Y
}

function random() {    // This function will give a random number between 0 and 100.
    var random = Math.random() * 100;
    document.getElementById("random").innerHTML = random
}

function pi() {    // This function will give us Pi.
    var pi = Math.PI;
    document.getElementById("pi").innerHTML = pi;
}