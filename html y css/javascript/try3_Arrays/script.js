const prompt = require('prompt-sync')();

// const matriz = [[1,2],[3,4],[5,6]];

// console.log(matriz[2][1]);

//////
// CREAR LISTA/ARRAYS VACIOS 
let matriz1 = new Array(3);

for (let i = 0; i <= 2; i++){
    matriz1[i] = new Array(3);
}

const vector1 = [1,2,3,4];
const vector2 = [5,6,7];

matriz1[0] = vector1;
matriz1[2] = vector2;

// console.log(matriz1);
//////
// RECORRER ARRAY (vector)

// for (let i = 0; i < matriz1.length; i++){
//     console.log(matriz1[i]);

// }

// RECORRER ARRAY (matriz)

let matriz2 = [ ["Hola", "cómo", "estas"],
                ["yo", "bien", "y tú"],
                ["ultimo"]
]

// for (let m = 0; m < matriz2.length; m++){
//     for (let v = 0; v < matriz2[m].length; v++){
        
//         console.log(matriz2[m][v]);
//     }
// }
//////

let matriz3 = ["Hola", "cómo", "estas"]

let letraA = matriz3.filter(buscaA => buscaA.includes("a"));
console.log(letraA);
    