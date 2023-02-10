document.write(typeof 3); // Determing the type of the value "3" - will return "number"
document.write("10" + 5); // Type coercion - will return "105"

function nan_function1() {  // Function to show example of NaN
	document.getElementById("nan").innerHTML = 0/0;
}

function nan_function2() {  // Function to show example of a isNaN check
	document.getElementById("true").innerHTML = isNaN("A sentence");
}

function nan_function3() {  // Function to show example of a isNaN check
	document.getElementById("false").innerHTML = isNaN("123");
}

function infinity() {  // Function to show example of infinity
    var infinity = document.write(2E310);
	document.getElementById("infinity").innerHTML = infinity;
}

function neg_infinity() {  // Function to show example of negative infinity
    var neg_infinity = document.write(-3E310);
	document.getElementById("neg_infinity").innerHTML = neg_infinity;
}

document.write(22 < 50); // Boolean will output true
document.write(10 > 20); // Boolean will output false

console.log(5 + 7); // Check console to see result.
console.log(5 > 7); // Check console to see result of boolean.

document.write(5 == 5);  // Is 5 equal to 5?
document.write(5 == 6); // Is 5 equal to 6?


a = 10;
b = 10;
document.write(a === b);    // Checks if a is the same as b. True.
	
c = 5;
d = "ten";
document.write(c === d);    // Checks if c is the same as d. False.
	
e = 5;
f = "5";
document.write(e === f);    // Checks if e is the same as f. False.

g = 5;
h = 10;
document.write(g === h);    // Checks if g is the same as h. False.

document.write(1 < 2 && 3 < 4); // Is 1<2 AND 3<4? True.
document.write(1 > 2 && 3 < 4); // Is 1>2 AND 3<4? False.

document.write(1 > 2 || 3 < 4); // Is 1>2 OR 3<4? True.
document.write(1 > 2 || 3 > 4); // Is 1<2 OR 3<4? False.

function notFunction1(){
	document.getElementById("not1").innerHTML = !(20 > 10); // Not operator to display true or false. False.
}

function notFunction2(){
	document.getElementById("not2").innerHTML = !(5 > 10); // Not operator to display true or false. True.
}