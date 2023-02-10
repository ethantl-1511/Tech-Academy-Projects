// Form function
function validateForm() {
    let x = document.forms["formEx"]["fname"].value;
    let y = document.forms["formEx"]["lname"].value;
    if (x == ""){
        alert("First name must be filled out.");
    }
    if (y == ""){
        alert("Last name must be filled out.")
    }
}