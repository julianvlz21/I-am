let generatorPassword = document.getElementById ("generatorPassword");
const lengthPassword = document.getElementById ("lengthPassword");

const btnGenerator = document.getElementById ("btn-generator");

let contraseña = "";

function actualizarLongitud() {
    const longitud = document.getElementById("longitud").value;
    document.getElementById("longitudValor").textContent = longitud;
    }

function generarContraseña(){
    const mayuscula = document.getElementById ("mayuscula").checked;
    const minuscula = document.getElementById ("minuscula").checked;
    const numeros = document.getElementById ("numeros").checked;
    const simbolos = document.getElementById ("simbolos").checked;

    }