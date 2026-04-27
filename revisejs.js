// Variables
var a = 10;
let b = 20;
const c = 30;

console.log(a, b, c);

// Hoisting
console.log(x);
var x = 5;

let y = 10;

// Function Hoisting
sayHi();

function sayHi() {
    console.log("Hi, this is Shashi");
}

// Scope
let userName = "Shashi";

function showUser() {
    let msg = "Welcome " + userName;
    console.log(msg);
}

showUser();

// Block Scope
if (true) {
    let blockVar = "Inside block";
    var outsideVar = "Accessible outside";
    console.log(blockVar);
}

console.log(outsideVar);

// Functions
function add(a, b) {
    return a + b;
}

console.log(add(5, 3));

// Function Expression
const multiply = function(a, b) {
    return a * b;
};

console.log(multiply(2, 6));

// Arrow Function
const subtract = (a, b) => a - b;

console.log(subtract(10, 4));

// Default Parameters
function greetUser(name = "Shashi") {
    console.log("Hello " + name);
}

greetUser();
greetUser("Rahul");

// Callback Function
function processUser(name, callback) {
    callback(name);
}

processUser("Shashi", function(name) {
    console.log("Processing data for " + name);
});