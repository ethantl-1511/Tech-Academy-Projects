// Switch function for choosing a color
function colorFunction(){
    var colorOutput;
    var colors = document.getElementById("colorInput").value;
    var colorString = " is a great color!";
    switch(colors) {
        case "Red":
            colorOutput = "Red" + colorString;
        break;
        case "Orange":
            colorOutput = "Orange" + colorString;
        break;
        case "Yellow":
            colorOutput = "Yellow" + colorString;
        break;
        case "Green":
            colorOutput = "Green" + colorString;
        break;
        case "Blue":
            colorOutput = "Blue" + colorString;
        break;
        case "Purple":
            colorOutput = "Purple" + colorString;
        break;
        default:
        colorOutput = "Please enter a color exactly as written on the above list.";
    }
    document.getElementById("output").innerHTML = colorOutput;
}
// Example use of getElementsByClassName()
function helloWorldFunction() {
	var a = document.getElementsByClassName("click");
	a[0].innerHTML = "The text has changed!";
}

// Example of adding a graphic to the HTML canvas
function circleCanvas(){
    var c = document.getElementById("canvas");
    var ctx = c.getContext("2d");
    ctx.beginPath();
    ctx.arc(250,125,40,0,2 * Math.PI);
    ctx.stroke();
}

// Example of adding a gradient to the HTML canvas
function gradientFunc(){
    var c = document.getElementById("grad");
    var ctx = c.getContext("2d");

    var grd = ctx.createLinearGradient(0,0,170,0);
    grd.addColorStop(0, "black");
    grd.addColorStop(1, "white");

    ctx.fillStyle = grd;
    ctx.fillRect(20,20,150,100);
}