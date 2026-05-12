const prompt = require('prompt-sync')();
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

// let contador = 25;

// do {
//     console.log(`Vuelta N° ${contador}`);
//     contador ++;    
// } while (contador <10)


// for (let i = 0; i <= 9; i++){
//     console.log(i);
// }

// let pregunta = confirm("Aceptar|Cancelar");

const fecha = new Date();
const dia = fecha.getDay();
const mes = fecha.getMonth();
const año = fecha.getFullYear();

console.log(diaMes);

if (dia == 0){console.log(`${año}/${mes+1}/lunes`);}
if (dia == 1){console.log(`${año}/${mes+1}/martes`);}
if (dia == 2){console.log(`${año}/${mes+1}/miercoles`);}
if (dia == 3){console.log(`${año}/${mes+1}/jueves`);}
if (dia == 4){console.log(`${año}/${mes+1}/viernes`);}
if (dia == 5){console.log(`${año}/${mes+1}/sabado`);}
if (dia == 6){console.log(`${año}/${mes+1}/domingo`);}

// console.log(año + "/" + (mes+1) + "/" + dia);
// console.log(`${año}/${mes+1}/${dia}`);