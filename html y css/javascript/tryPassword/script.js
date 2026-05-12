const prompt = require('prompt-sync')();

const MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const MINUSCULAS = "abcdefghijklmnopqrstuvwxyz";
const NUMEROS    = "0123456789";
const SIMBOLOS   = "!@#$%^&*()-_=+[]{}|;:,.<>?";

// let generatorPassword = document.getElementById ("generatorPassword");
// const btnGenerator = document.getElementById ("btn-generator");

// let contraseña = "";

function actualizarLongitud() {
    const longitud = document.getElementById("lengthPassword").value;
    document.getElementById("longitudValor").textContent = longitud;
    }

// checkbox 
function generarContraseña(){
    const mayuscula = document.getElementById ("mayuscula").checked;
    const minuscula = document.getElementById ("minuscula").checked;
    const numeros = document.getElementById ("numeros").checked;
    const simbolos = document.getElementById ("simbolos").checked;
    
    const mayusculasD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const minusculasD = "abcdefghijklmnopqrstuvwxyz";
    const numerosD    = "0123456789";
    const simbolosD   = "!@#$%^&*";

    // Se hace el pool
    let pool = "";

    if (mayuscula) {pool += mayusculasD};
    if (minuscula) {pool += minusculasD};
    if (numeros)   {pool += numerosD};
    if (simbolos)  {pool += simbolosD};

    const longitud = document.getElementById("lengthPassword").value;
    let contraseña ="";

    for (let i = 0; i < longitud; i++){
        const indice = Math.floor(Math.random()* pool.length);
        contrasena += pool[indice];
    }
    
    // let contraseñaFinal = document.getElementById("passwordFinal");
    // contraseñaFinal.textContent = contraseña;

    }