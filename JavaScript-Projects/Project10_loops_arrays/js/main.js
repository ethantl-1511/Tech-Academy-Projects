// Function for counting to ten While Loop
function countToTen() {
    var digit = "";
    var x = 1;
    while (x < 11) {
        digit += "<br>" + x;
        x++;
    }
    document.getElementById("countToTen").innerHTML = digit;
}

// Function for string length 
function howManyLetters(){ // 
    var word = "supercalifragilisticexpialidocious";
    document.getElementById("howManyLetters").innerHTML = word.length;
}

//Function for instrument list For Loop
//First, list global variables
var instruments = ["Guitar", "Drums", "Piano", "Bass", "Violin", "Trumpet", "Flute"];
var content = "";
var y;
//Second, create for loop function
function forLoop(){
	for (y = 0; y < instruments.length; y++) {
	content += instruments[y] + "<br>";
	}
	document.getElementById("listOfInstruments").innerHTML = content;
}

// Function to create an array of cats.
function catPics(){
    var catPictures = [];
    catPictures[0] = "sleeping";
    catPictures[1] = "playinging";
    catPictures[2] = "eating";
    catPictures[3] = "purring";
    document.getElementById("cat").innerHTML = "In this picture, the cat is " + catPictures[2] + ".";
}

// Function to give an example of a const.
function constantFunction(){
    const musicInstrument = {type:"guitar", brand:"Fender", color:"black"};
    musicInstrument.color = "red";
    musicInstrument.price = "$900";
    musicInstrument.hand = "right-handed";
    document.getElementById("constant").innerHTML = 
    "The cost of the " 
    + musicInstrument.color 
    + " " 
    + musicInstrument.hand 
    + " " 
    + musicInstrument.brand
    + "-" 
    + musicInstrument.type 
    + " was " 
    + musicInstrument.price;
}

// Function to show example of let variable
function letExample(){
    let x = 20; // A local variable, note that we've used x in the script before.
    document.getElementById("let").innerHTML = x;
}

// Example of using RETURN
function returnExample(){
    let x = 10;
    let y = 20;
    if (x < y){
        return document.getElementById("return").innerHTML = "It is greater.";
    }
    else document.getElementById("return").innerHTML = "It is not.";
}

// Car object creation
let car = {
    make: "Dodge ",
    model: "Viper ",
    year: "2021 ",
    color: "red ",
    description : function(){
        return "The car is a " + this.year + this.color + this.make + this.model;
    }
};
document.getElementById("carObject").innerHTML = car.description();

// Break example
function breakExample(){
    for (let i = 0; i < 10; i++){ // This says to add 1 to i if = to 0, and < 10.
        if (i === 3) {break;} // This will "break" / stop the count at 3
        document.getElementById("break").innerHTML += "The number is " + i + "<br>";
    }
}

// Continue example
function contExample(){
    for (let i = 0; i < 10; i++){
        if (i === 3) {continue;} // This will "continue" / jump over 3.
        document.getElementById("continue").innerHTML += "The number is " + i + "<br>";
    }
}