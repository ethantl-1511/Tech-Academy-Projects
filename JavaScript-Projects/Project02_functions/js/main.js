function my_first_function() {  // Defining first function, "my_first_function"
    var Family = "The Arezzinis"    // Creating variable "Family" and giving it a string value.
    var Dad = "Jermiah"             // Creating second variable "Dad" and giving it a string value.
	document.getElementById("button_text").innerHTML = Family + ", " + Dad; // Setting up call to give us the value of 'Family + ", " + Dad' via "button_text"
}

function myFunction() {             // Defining second function "myFunction"
    var sentence = "I am learning";         // Variable sentence with string
    sentence += " a lot from this book!";   // Using += operator to concatenate
    document.getElementById("Concatenate").innerHTML = sentence;    // Setting up call to give us the value of 'sentence' via "Concatenate"
}