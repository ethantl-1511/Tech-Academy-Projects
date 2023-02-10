var x = 10 // global variable
function addNumbers_1() {
    document.getElementById("global").innerHTML = 20 + x;
}
addNumbers_1();

function addNumbers_2() {
    var y = 20; // local variable
    document.getElementById("local").innerHTML = 50 + y;
}
addNumbers_2();

function addNumbers_3() {
    document.getElementById("local_broke").innerHTML = 30 + y; // uses the local variable in addnumbers_2, which will not work
    console.log(30 + y); // uses console.log to debug, check developer tools!
}
addNumbers_3();

function getDate(){ // An if statement based on time-of-day.
    if (new Date().getHours() < 18) {
        document.getElementById("time").innerHTML = "Adventure Time!";
    }
}

function numbers(){ // Another if statement, determined by numbers.
    var x = 10
    if (x < 20){
        document.getElementById("ifstatement").innerHTML = "x is indeed less than 20.";
    }
}

function ageFunction() { // AN if/else statement to determine voting eligibility.
	age = document.getElementById("age").value;
	if (age >= 18) {
		vote = "You are old enough to vote!";
	}
	else {
		vote = "You are not old enough to vote!";
	}
	document.getElementById("howOldAreYou").innerHTML = vote;
}

function timeFunction(){ // Time_function() = timeFunction(), an if/elseif/else function to determine what period of day it is.
    var time = new Date().getHours();
    var reply;
    if (time < 12 == time > 0) {
        reply = "It is morning time!"
    }
    else if (time >= 12 == time < 18) {
        reply = "It is afternoon.";
    }
    else {
        reply = "It is evening time.";
    }
    document.getElementById("timeOfDay").innerHTML = reply;
}