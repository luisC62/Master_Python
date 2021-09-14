// alert('Hola mundo!!')
window.onload=inicio;
var nombre = "Luis Cárceles";
var edad = 58;

var concatenacion = nombre + ". " + "Tu edad es: " + edad + " años";
function inicio(){
    var dato = document.getElementById("datos");
    var info = document.getElementById("info");
    dato.innerHTML = concatenacion;
    info.innerHTML = `<h3>Ficha de datos completa</h3>
                      <p>Mi nombre es: ${nombre}</p>
                      <p>Mi edad es: ${edad} años</p>`;
    if (edad >= 30){
        info.innerHTML +='<p>Eres un profesional senior</p>';
    }else{
        info.innerHTML +='<p>Eres un profesional junior</p>';
    }
    printyears(dato);
    var nombres = ['Luis', 'Marta', 'David'];
    printarrays(nombres, dato)
}

function  printyears(x){
    for(var i=1962; i<=2020; i++){
        x.innerHTML += "Estamos en el año: " + i + "</br>"
    }
}
function printarrays(a, x){
    for(var k=0; k<a.length; k++){
        x.innerHTML += `<p>El miembre ${k + 1} del grupo es ${a[k]} </p>>`;
    }
}
