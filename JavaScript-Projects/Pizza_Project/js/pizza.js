function getReceipt() {
    // This initializes our string so it can get passed from
    // function to function, gorwing line by line into a full receipt
    var text1 = "<h3>You Ordered:</h3>"; 
    var runningTotal = 0; // Variable for keeping track of the total price
    var sizeTotal = 0; // Variable for keeping track of the size 
    var sizeArray = document.getElementsByClassName("size");  // Array variable that will be used to add what is selected under "size" class
    for (var i = 0; i < sizeArray.length; i++) { // This [for loop/if/else if] checks what 'size' is selected, adds it to text1, and sets number to variable runningTotal
        if (sizeArray[i].checked) { // If sizeArray[i] is checked,
            var selectedSize = sizeArray[i].value; // selectedSize = the value of sizeArray[i]
            text1 = text1 + selectedSize + "<br>"; // text1 = itself + selectedSiz
        }
    } // Below will set sizeTotal to the appropriate price IF the selectedSize === which size.
    if (selectedSize === "Personal Pizza") {
        sizeTotal = 6;
    } else if (selectedSize === "Small Pizza") {
        sizeTotal = 8;
    } else if (selectedSize === "Medium Pizza") {
        sizeTotal = 10;
    } else if (selectedSize === "Large Pizza") {
        sizeTotal = 14;
    } else if (selectedSize === "Extra Large Pizza") {
        sizeTotal = 16;
    }
    runningTotal = sizeTotal;
    console.log(selectedSize + " = $" + sizeTotal + ".00"); // Outputs a console message with the selected size, and size total.
    console.log("size text1: " + text1); // Outputs a console message for text1
    console.log("subtotal: $" + runningTotal + ".00"); // Outputs a console message for subtotal price 
    // These variables will get passed on to each function
    getTopping(runningTotal,text1);
};

function getTopping(runningTotal,text1){
    var toppingTotal = 0; // Variable for tracking toppings
    var selectedTopping = []; // Variable for tracking the selected topping(s)
    var toppingArray = document.getElementsByClassName("toppings"); // Array variable that will be used for what is selected under "toppings" class.
    for (var j = 0; j < toppingArray.length; j++) { // This [for loop/if/else if] checks what 'topping' is selected, adds it to text1
        if (toppingArray[j].checked) {
            selectedTopping.push(toppingArray[j].value); // Pushes selectedToppings to toppingArray
            console.log("selected topping item: ("+ toppingArray[j] +")"); // Console message telling us what topping was selected
            text1 = text1 + toppingArray[j].value + "<br>";
        }
    }
    var toppingCount = selectedTopping.length; // Whatever the number is in the selectedTopping array, that is now set to toppingCount
    if (toppingCount > 1) { // If toppingCount is greater than 1
        toppingTotal = (toppingCount - 1); // toppingTotal = toppingCount - 1
    } else { // Otherwise,
        toppingTotal = 0; // toppingTotal = 0
    }
    runningTotal = (runningTotal + toppingTotal); // The running total equal itself + totalTopping
    console.log("total selected topping items: " + toppingCount); // Console message for topping count
    console.log(toppingCount + " topping - 1 free topping = " + "$" + toppingTotal + ".00"); // Console message for topping count and total
    console.log("topping text1: " + text1); // Console message telling us text1
    console.log("Purchase Total: " + "$" + runningTotal + ".00"); // Console message giving us the runningTotal
    document.getElementById("showText").innerHTML = text1; // Displays text1 output in HTML div id="showText"
    document.getElementById("totalPrice").innerHTML = "<h3>Total: <strong>$" + runningTotal + ".00" + "</strong></h3>"; // Displays totalPrice output in div HTML id="totalPrice"
};