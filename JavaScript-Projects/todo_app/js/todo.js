// Function gets task from input
function get_todos() {
    var todos = new Array; // Create an array of tasks
    var todos_str = localStorage.getItem('todo'); // Pulls task that was saved in browser memory
    if (todos_str !== null) {   // If the input is NOT null, parse and make JS object
        todos = JSON.parse(todos_str);
    }
    return todos;
}

// Function adds inputed task to get_todos array
function add() {
    var task = document.getElementById('task').value; // Takes inputed task and creates a variable
    var todos = get_todos();
    todos.push(task); // Adds new task to the end of the array
    localStorage.setItem("todo", JSON.stringify(todos)); // Converts task to JSON string
    document.getElementById("task").value = "";
    show();

    return false;
}

// Function that removes task when clicking "X" button
function remove() {
    var ID = this.getAttribute('id');
    var todos = get_todos();
    todos.splice(ID, 1);
    localStorage.setItem("todo", JSON.stringify(todos));
    show();
}

// Function keeps the task permanently displayed on screen
function show() {
    var todos = get_todos(); // Sets task that was retrieved as a variable
    var html = '<ul>'; // Sets up each task as an unordered list
    for (var i = 0; i < todos.length; i++) {    // Displays a task to the list in the order that it is inputted, and displays the task as a list and created the button "X"
        html += '<li>' + todos[i] + '<button class="remove" id="' + i + '">x</button></li>';
    };
    html += '</ul>'; // Ends unordered list
    document.getElementById('todos').innerHTML = html; // Displays the task as a list

    for (var i = 0; i < todos.length; i++) {
        document.getElementById(`${i}`).addEventListener('click', remove);
    }

}

document.getElementById('add').addEventListener('click', add); // Displays the inputed task when the 'Add Item' button is clicked
show(); // Keeps the inputs displayed on the screen