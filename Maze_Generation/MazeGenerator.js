//const GRID_SIZE = 4600000; //square centimeters
const GRID_SIZE = 1600;
var CUSTOM_rows = null;
var CUSTOM_cols = null;

var GRID = [];

var RandomSequenceOfUnique = (function () {
    function RandomSequenceOfUnique(seedBase, seedOffset) {
        var prime = 4294967291,
            residue,
            permuteQPR = function (x) {
                if (x >= prime)
                    return x;
                residue = (x * x) % prime;
                return (x <= prime / 2) ? residue : prime - residue;
            }

        this.next = function () {
            return permuteQPR((permuteQPR(this.index++) + this.intermediateOffset) ^ 0x5bf03635);
        }

        this.index = permuteQPR(permuteQPR(seedBase) + 0x682f0161);
        this.intermediateOffset = permuteQPR(permuteQPR(seedOffset) + 0x46790905);
    }
    return RandomSequenceOfUnique;
}());


function generateDimensions() {
    var scale = Math.floor((Math.random() * 40) + 60); //GENERATES RANDOM # 60 - 100
    var rows = Math.floor(Math.sqrt(GRID_SIZE / (scale / 100)));
    var cols = Math.floor(GRID_SIZE / rows);
    var temp;
    if (Math.floor(Math.random() * 2) == 1) { //randomize length and width
        temp = rows;
        rows = cols;
        cols = temp;
    }

    return [rows, cols];
}

function customDimensions() {
    if (CUSTOM_rows === null || CUSTOM_cols === null) {
        return false;
    }
    return [CUSTOM_rows, CUSTOM_cols];
}

function generateObstacle(y, x) {
    //console.log("obstacle");
    //size of obstacle 
    rows = y + 20;
    cols = x + 15;
    
   /* for (var i = y; i < rows; i++) {
        for (var j = x; j < cols; j++) {
            GRID[i][j] = [1, 1, 1, 1];
        }
    } */

    for (var i = y; i < rows; i++) {
        GRID[i][x] = [0, 0, 1, 0]; //left wall
        GRID[i][cols - 1] = [0, 0, 0, 1] //right wall;
    }
    /*UP AND DOWN WALL*/
    for (var i = x; i < cols; i++) {
        GRID[y][i] = [1, 0, 0, 0]; //up wall
        GRID[rows - 1][i] = [0, 1, 0, 0]; //down wall
    }

    /* CORNER POINTS */
    GRID[y][x] = [1, 0, 1, 0]; //top left corner
    GRID[rows - 1][x] = [0, 1, 1, 0]; //bottom left corner
    GRID[y][cols - 1] = [1, 0, 0, 1]; //top right corner
    GRID[rows - 1][cols - 1] = [0, 1, 0, 1]; //bottom right corner
}


function generateOutline() {
    var dimensions = customDimensions() === false ? generateDimensions() : customDimensions();
    GRID.rows = dimensions[0];
    GRID.cols = dimensions[1];
    GRID.size = dimensions[0] * dimensions[1];

    var rows = dimensions[0];
    var cols = dimensions[1];

    /*EMPTY BOX*/
    for (var i = 0; i < rows; i++) {
        GRID[i] = new Array(1);
        for (var j = 0; j < cols; j++) {
            GRID[i][j] = [0, 0, 0, 0];
        }
    }
    /* scary algo
    for (var i = 0; i < rows; i++) {
        for (var j = 0; j < cols; j++) {
            if(Math.floor(Math.random() * 100) < 10 && j < rows - 80 && i < cols - 120 ) {
                generateObstacle(i, j);
            }
        }
    } */

    for (var i = 0; i < rows; i++) {
        var generator = new RandomSequenceOfUnique(Date.now(), parseInt(Math.random() * 10000));
        for (var j = 0; j < cols; j++) {
            if ( (generator.next() % 100000 < 10) && (i < rows - 20) && (j < cols - 15)) {
                generateObstacle(i, j);
               // i += 50;
                //j += 70;
                generator.next();
                generator.next();
            }
        }
    }
    /*LEFT AND RIGHT WALL*/
    for (var i = 0; i < rows; i++) {
        GRID[i][0] = [0, 0, 1, 0]; //left wall
        GRID[i][cols - 1] = [0, 0, 0, 1] //right wall;
    }
    /*UP AND DOWN WALL*/
    for (var i = 0; i < cols; i++) {
        GRID[0][i] = [1, 0, 0, 0]; //up wall
        GRID[rows - 1][i] = [0, 1, 0, 0]; //down wall
    }

    /* CORNER POINTS */
    GRID[0][0] = [1, 0, 1, 0]; //top left corner
    GRID[rows - 1][0] = [0, 1, 1, 0]; //bottom left corner
    GRID[0][cols - 1] = [1, 0, 0, 1]; //top right corner
    GRID[rows - 1][cols - 1] = [0, 1, 0, 1]; //bottom right corner
    return;
}


function removeWarningMessage() {
    document.getElementById('message').innerText = " ";
}

function drawMap() {
    var p = 5;
    removeWarningMessage();
    //document.getElementById("canvas").rows = GRID.rows;
    //document.getElementById("canvas").cols = GRID.cols;
    var bw = GRID.rows;
    // Box cols
    var bh = GRID.cols;
    // Padding
    var p = 10;

    var canvas = document.getElementById("canvas");
    var context = canvas.getContext("2d");

    for (var y = 0; y < bw; y++) {
        context.strokeStyle = "black";
        for (var x = 0; x < bh; x++) {
            context.beginPath();
            if (GRID[y][x][2] == 1) {
                context.moveTo(0.5 + x + p, y + p);
                context.lineTo(0.5 + x + p, y + 1 + p);
            }
            context.stroke();
            if (GRID[y][x][3] == 1) {
                context.moveTo(.5 + x + 1 + p, y + p);
                context.lineTo(.5 + x + 1 + p, y + 1 + p);
            }
            context.stroke();
            if (GRID[y][x][0] == 1) {
                context.moveTo(x + p, 0.5 + y + p);
                context.lineTo(x + 1 + p, 0.5 + y + p);

            }
            context.stroke();
            if (GRID[y][x][1] == 1) {
                context.moveTo(x + p, 0.5 + y + 1 + p);
                context.lineTo(x + 1 + p, 0.5 + y + 1 + p);
            }
            context.stroke();
        }
    }



}

function promptUser() {
    return true;
}



function printMap(filename) {
    var fs = require('fs');
    var room = "";
    var rows = GRID.rows;
    var cols = GRID.cols;
    for(var i = 0; i < rows; i++) {
        var lineString = "";
        for(var j = 0; j < cols; j++) {
            for(var k = 0; k < 4; k++) {
                lineString += String(GRID[i][j][k]);
            }
           // console.log(lineString);
        }
        room += lineString + '\n';
    }
    fs.writeFile(filename + '.txt', room, function (err) {
        console.log('Saved!');
      });
}

function mapGenerator(numMaps) {
    promptUser();
    
    
    //drawMap(); comment this out for txt file
    for(var i = 1; i <= numMaps; i++) {
        generateOutline();
        num = i + 0; //for file naming generate file by blocks to not overwork procssor
        currentFilename = FILE_PREFIX + num;
        printMap(currentFilename); //comment printMap() to visualize in html
        GRID = [];
    }
    console.log("done");
}

const NUM_MAPS = 1; //number of maps to generate
const FILE_PREFIX = "tinymaze" + GRID_SIZE + "_";

mapGenerator(NUM_MAPS)



