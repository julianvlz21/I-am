//  let color = prompt("Enter a color: ");

//  switch(color) {
    
//     case "red":
//         console.log("Your color is red");
//         break;

//     default:
//         console.log("choose the color");
//         break;
//  }

// let list = prompt("open calculatore y | n");

// while (list === "y"){
//     const options = prompt("Escoge 1 si quieres restar,Escoge 2 si quieres sumar, Escoge 3 si quieres multiplicar")
//     let number1 = Number(prompt("Enter the first number: "));
//     let number2 = Number(prompt("Enter the second number: "));
    
//     if (options == "1"){
//         const total = (number1 - number2);
//         console.log(`the subtract of ${number1} - ${number2} = ${total}`);
//         break

//     } else if (options == "2") {
//         const total = (number1 + number2);
//         console.log(`the sum of ${number1} + ${number2} = ${total}`);
//         break;

//     } else if (options == "3") {
//         const total = (number1 * number2);
//         console.log(`the multiplication of ${number1} * ${number2} = ${total}`);
//         break;

//     } else {
//         alert("choose a correct option");
 
//     }
//     break
 
// };

// Do while //

let contador = 25;

do {
    console.log(`Vuelta N° ${contador}`);
    contador ++;    
} while (contador <10)