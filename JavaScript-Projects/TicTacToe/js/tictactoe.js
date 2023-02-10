let activePlayer = 'X'; // Keeps track of whose turn it is
let selectedSquares = []; // Stores an array of moves, used to determine win conditions.

function placeXorO(squareNumber){ //Function for placing an X or O in a square.
    if (!selectedSquares.some(element => element.includes(squareNumber))){ // Ensures a square hasn't be selected
        let select = document.getElementById(squareNumber); // Retrieves the HTML element id that was clicked
        if (activePlayer === 'X') { // Condition checks who's turn it is
            select.style.backgroundImage = 'url("images/x.png")'; // If activePlayer is equal to 'X', x.png is placed.
        } else {
            select.style.backgroundImage = 'url("images/o.png")'; // if activePlayer is equal to 'O', o.png is placed.
        }
        selectedSquares.push(squareNumber + activePlayer); // squareNumber and activePlayer are concatenated together and added to array.
        checkWinConditions(); // Calls a function to check for any win conditions.
        if (activePlayer === 'X') { // Condition for changing active player
            activePlayer = 'O'; // If active player is 'X', change to 'O'
        } else { // If active player is anything other than 'X', change to 'X'
            activePlayer = 'X';
        }
        function checkWinConditions(){ // This function parses the selectedSquares array to search for win conditions. drawLine() function is called to draw a line on the screen if the condition is met
            // Start of X win conditions
            if (arrayIncludes('0X', '1X', '2X')) { drawWinLine(50,100,558,100) } // If X is on 0, 1, 2 - win condition.
            else if (arrayIncludes('3X', '4X', '5X')) { drawWinLine(50,304,558,304) } // If X is on 3, 4, 5 - win condition ... and so on.
            else if (arrayIncludes('6X', '7X', '8X')) { drawWinLine(50,508,558,508) } // End of horizontal X win conditions
            else if (arrayIncludes('0X', '3X', '6X')) { drawWinLine(100,50,100,558) }
            else if (arrayIncludes('1X', '4X', '7X')) { drawWinLine(304,50,304,558) }
            else if (arrayIncludes('2X', '5X', '8X')) { drawWinLine(508,50,508,558) } // End of vertical X win conditions
            else if (arrayIncludes('0X', '4X', '8X')) { drawWinLine(100,100,520,520) } // Top-left-buttom-right diagonal win
            else if (arrayIncludes('6X', '4X', '2X')) { drawWinLine(100,508,510,90) } // Bottom-left-top-right diagonal win, END OF X WINS
            // Start of O win conditions
            else if (arrayIncludes('0O', '1O', '2O')) { drawWinLine(50,100,558,100) } // If O is on 0, 1, 2 - win condition.
            else if (arrayIncludes('3O', '4O', '5O')) { drawWinLine(50,304,558,304) } 
            else if (arrayIncludes('6O', '7O', '8O')) { drawWinLine(50,508,558,508) } // End of horizontal O win conditions
            else if (arrayIncludes('0O', '3O', '6O')) { drawWinLine(100,50,100,558) }
            else if (arrayIncludes('1O', '4O', '7O')) { drawWinLine(304,50,304,558) }
            else if (arrayIncludes('2O', '5O', '8O')) { drawWinLine(508,50,508,558) } // End of vertical O win conditions
            else if (arrayIncludes('0O', '4O', '8O')) { drawWinLine(100,100,520,520) } // Top-left-buttom-right diagonal win
            else if (arrayIncludes('6O', '4O', '2O')) { drawWinLine(100,508,510,90) } // Bottom-left-top-right diagonal win, END OF O WINS
            // Condition for tie. If none of the above are met, and 9 squares are selected the code executes.
            else if (selectedSquares.length >= 9) {
                audio('./media/tie.mp3'); // Plays tie sound
                setTimeout(function() { resetGame(); }, 1000); // After 1s, resetGame function is called.
            }

            function arrayIncludes(squareA, squareB, squareC){ // Function checks if an array includes 3 strings. Used to check for win conditions.
                // Variables to be used to check for 3 in a row:
                const a = selectedSquares.includes(squareA);
                const b = selectedSquares.includes(squareB);
                const c = selectedSquares.includes(squareC);
                if (a === true && b === true && c === true) { return true; } // If the 3 variables we pass are all included in our array, then true is returned and else if executes drawLine() function.
            }
        }

        function disableClick(){
            body.style.pointerEvents = 'none'; // Makes our body unclickable
            setTimeout(function () { body.style.pointerEvents = 'auto'; }, 1000) // Makes body clickable after 1 second
        }
        
        function audio(audioURL) { // Function takes a string parameter fromn earlier for placement sound('./media/place.mp3')
            let audio = new Audio(audioURL); // Create new audio object and pass the path as parameter
            audio.play(); // Play method plays sound
        }
        
        function drawWinLine(coordX1, coordY1, coordX2, coordY2) { // Function utilizes HTML canvas to draw win lines.
            const canvas = document.getElementById('win-lines');
            const c = canvas.getContext('2d');
            let x1 = coordX1, // Start of a lines x axis
                y1 = coordY1, // Start of a lines y axis
                x2 = coordX2, // End of a lines x axis
                y2 = coordY2, // End of a lines y axis
                x = x1, // Stores temporary x axis data we update in our animation loop
                y = y1; // Stores temporary y axis data we update in our animation loop
        
        
            function animateLineDrawing(){ // Function interacts with the canvas.
                const animationLoop = requestAnimationFrame(animateLineDrawing); // Creates a loop
                c.clearRect(0,0,608,608); // Clears content from last loop iteration
                c.beginPath(); // Starts a new path
                c.moveTo(x1,y1); // Incidates starting point in the line
                c.lineTo(x,y); // Indicates end point in the line
                c.lineWidth = 10; // Width of line
                c.strokeStyle = 'rgba(70,255,33,.8)'; // Color of line
                c.stroke(); // Draws everything we laid out above
                if (x1 <= x2 && y1 <= y2) { // Condition checks if we've reached endpoints
                    if (x < x2) { x += 10; } // Condition adds 10 to the previous end x endpoint.
                    if (y < y2) { y += 10; } // Condition adds 10 to the previous end y endpoint.
                    if (x >= x2 && y >= y2 ) { cancelAnimationFrame(animationLoop); } // Condition similar to the above, necessary for 6/4/2 win conditions.
                }
                // Another condition necessary for 6/4/2 win condition
                if (x1 <= x2 && y1 >= y2) {
                    if (x < x2) { x += 10; }
                    if (y > y2) { y -= 10; }
                    if (x >= x2 && y <= y2 ) { cancelAnimationFrame(animationLoop); }
                }
            }
        
            function clear(){ // Function clears canvas after win line is drawn.
                const animationLoop = requestAnimationFrame(clear); // Starts our animation loop
                c.clearRect(0,0,608,608); // Clears canvas
                cancelAnimationFrame(animationLoop);
            }
        
            disableClick(); // This line disallows clicking while win sound is playing
            audio('./media/winGame.mp3'); // This line plays the win sound
            animateLineDrawing(); // This calls out main animation
            setTimeout(function () { clear(); resetGame(); }, 1000); // This line waits 1 second and then clears canvas, resets game, and allows clicking.
        }

        function resetGame() { // Function that resets the game in the event of a tie or a win.
            for (let i = 0; i < 9; i++){ // Loop iterates through each HTML square element.
                let square = document.getElementById(String(i)); // Variable gets the HTML element i.
                square.style.backgroundImage = ''; // Removes our elements backgroundImage
            }
            selectedSquares = []; // Resets our array so it is empty and we can start over
        }

        audio('./media/place.mp3'); // Function plays placement sound.
        if (activePlayer === 'O'){ // Condition checks to see if it is the computers turn.
            disableClick(); // This disables clicking for computers turn.
            setTimeout(function () { computersTurn(); }, 1000); // Function waits 1 second before the computer places an image and enables click.
        }
        return true; // Returning true needed for computersTurn() function to work.
    }

    
    function computersTurn(){ // Function results a random square being selected by the computer.
        let success = false; // Boolean needed for while loop
        let pickASquare; // Variable stores a random number 0-8.
        while (!success){ // Condition allows for while loop to keep trying if a square is selected already.
            pickASquare = String(Math.floor(Math.random() * 9)); // Random number between 0 and 8 is selected.
            if (placeXorO(pickASquare)) { // If the random number evaluated returns true, the square hasn't been selected yet.
                placeXorO(pickASquare); // Call the function.
                success = true; // Change boolean to true, end the loop.
            };
        }
    }
    
}
