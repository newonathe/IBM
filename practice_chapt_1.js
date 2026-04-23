// In JavaScript, use let, const, or var

let name = "Ethan"; //can be reassigned
const PI = 3.14529; //constant, cannot be reassigned
var age = 21; // old way of declaring variables, can be reassigned and has function scope, avoid

// Types in JS (loosely typed like Python)
let name = "Ethan" // string
let age = 22 //number
let GPA = 3.8 //number
let isStudent = true; //boolean
let emptyValue = null; //null
let undefinedValue; //undefined

// Check Type
console.log(typeof name); // string
console.log(typeof age);

// Type Conversion
let numStr = "123";
let parsed = parseInt(numStr);
let parsedF = parsedFloat(numStr);
let backToStr = String(99);

