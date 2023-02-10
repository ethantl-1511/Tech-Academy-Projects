function rideFunction() { // Height-for-riding function
	var height, canRide;
	height = document.getElementById("height").value;
	canRide = (height < 52) ? "You are too short":"You are tall enough";
	document.getElementById("ride").innerHTML = canRide + " to ride.";
}

function voteFunction() { // Voting ternary function
	var age, canVote;
	age = document.getElementById("age").value;
	canVote = (age < 17) ? "You are not old enough":"You are old enough";
	document.getElementById("vote").innerHTML = canVote + " to vote.";
}

function Vehicle(Make, Model, Year, Color) { // Function utilizing this and new.
	this.Vehicle_Make = Make;
	this.Vehicle_Model = Model;
	this.Vehicle_Year = Year;
	this.Vehicle_Color = Color;
}
var Jack = new Vehicle("Dodge", "Viper", 2020, "Red");
var Emily = new Vehicle("Jeep", "Trail Hawk", 2019, "White and Black");
var Erik = new Vehicle("Ford", "Pinto", 1971, "Mustard");
function myFunction() {
	document.getElementById("keywords_and_constructors").innerHTML = "Erik drives a " + Erik.Vehicle_Color + "-colored " + Erik.Vehicle_Model + " manufacured in " + Erik.Vehicle_Year;
}

function animal(type, age, color) { // My own function utilizing this and new.
    this.animal_type = type;
    this.animal_age = age;
    this.animal_color = color;
}
var Nick = new animal("Dog", "1", "Black");
var Remi = new animal("Cat", "3", "Calico");
function pet() {
    document.getElementById("new_and_this").innerHTML = "Remi has a " + Remi.animal_color + "-colored " + Remi.animal_type + ", age " + Remi.animal_age;
}

// Using a reserved word challenge. Used comments to kill it.
// function reserved(word, letter) {
//     this.reserved_word = word;
//     this.reserved_letter = letter;
// }
// var null = new reserved("Word", "W");
// function reservedFunction(){
//     document.getElementById("reserved").innerHTML = "Using the variable void: " + null.reserved_word + " " + null.reserved_letter;
// }

function countFunction(){ // Nested function
    document.getElementById("nested_function").innerHTML = count();
    function count(){
        var startingPoint = 9;
        function plusOne() {startingPoint += 1;}
        plusOne();
        return startingPoint;
    }
}