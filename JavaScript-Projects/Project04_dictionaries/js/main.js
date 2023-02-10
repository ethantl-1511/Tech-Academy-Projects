function myDictionary() {   // Defining the function.
	var animal = {  // The variable, animal, followed by KVPs
		Species:"Cat",
		Color:"Black and White",
		Breed:"American Shorthair",
		Age:2,
		Sound:"Meow!"
	};
    delete animal.Breed;    // Deletes the Breed key.
	document.getElementById("Dictionary").innerHTML = animal.Breed; // Will output as "undefined"
}