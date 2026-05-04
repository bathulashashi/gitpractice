
let numbers = [300, 123, 783, 576, 231];


let sum = numbers.reduce((total, num) => total + num, 0);
console.log(sum); 


let evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); 


let sortedNumbers = [...numbers].sort((a, b) => a - b);
console.log(sortedNumbers); 


let largest = Math.max(...numbers);
console.log(largest); // 783


let evenCount = numbers.filter(num => num % 2 === 0).length;
console.log(evenCount); // 2


numbers.forEach(num => console.log(num));

