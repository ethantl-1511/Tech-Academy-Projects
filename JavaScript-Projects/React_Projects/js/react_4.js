function validateForm(){
    let x = document.forms["formExample"]["first"].value;
    if (x == "") {
        alert("Name must be filled out");
        return false;
    }
    let y = document.forms["formExample"]["last"].value;
    if (y == "") {
        alert("Name must be filled out");
        return false;
    }
    let z = document.forms["formExample"]["phone"].value;
    if (z == "") {
        alert("Phone number must be filled out");
        return false;
    }
}

function openForm(){
    document.getElementById("popupForm").style.display = "block";
}

function closeForm(){
    document.getElementById("popupForm").style.display = "none";
}

// Automatic slideshow
$("#slideshow > div:gt(0)").hide();

setInterval(function() {
  $('#slideshow > div:first')
    .fadeOut(1000)
    .next()
    .fadeIn(1000)
    .end()
    .appendTo('#slideshow');
}, 3000);

