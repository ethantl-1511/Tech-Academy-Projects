function fullSentence() {   // Concatenate sentence function
	var part1 = "This is "; 
	var part2 = "a sentence ";
	var part3 = "using the ";
	var part4 = "concat() method.";
	var wholeSentence = part1.concat(part2, part3, part4);
	document.getElementById("concat").innerHTML = wholeSentence;
}

function sliceMethod(){ // Slice sentence function
	var sentence = "All work and no play makes Johnny a dull boy.";
	var section = sentence.slice(27,33);
	document.getElementById("slice").innerHTML = section;
}

function upperCase(){ // Function to create uppercase words.
    var sentence = "i'm too lazy to use capslock.";
    var letters = sentence.toUpperCase();
    document.getElementById("upper").innerHTML = letters;
}

function searching(){ // Function that searches for index position of a given value.
    var sentence = "This is a sentence about a girl named Remi.";
    var word = sentence.search("Remi");
    document.getElementById("search").innerHTML = word; // Note: Remi is at 38
}

function stringMethod(){ // Function that turns numbers into a string data type.
	var x = 182;
	document.getElementById("numberToString").innerHTML = x.toString();
}

function precisionMethod(){ // Function that will format a number to a specific length.
	var x = 13245.1409571353;
	document.getElementById("precision").innerHTML = x.toPrecision(7);
}

function fixing(){ // toFixed() function, can round up a specific number of decimals.
    var x = 12.6567;
    document.getElementById("fixing").innerHTML = x.toFixed();
}

function value1(){ // The valueOf() method returns the primitive value of a string.
    var x = "This is a string.";
    document.getElementById("value1").innerHTML = x.valueOf();
}