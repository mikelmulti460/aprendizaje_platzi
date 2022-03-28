var dibujo = document.getElementById("midibujito");
var lienzo = dibujo.getContext("2d");
var i=0;

function dibujarLinea(color, x_inicial, y_inicial, x_final, y_final) {
   lienzo.beginPath();
   lienzo.strokeStyle = color;
   lienzo.moveTo(x_inicial, y_inicial);
   lienzo.lineTo(x_final, y_final);
   lienzo.stroke();
   lienzo.closePath();
}

while (i<=300) {
    dibujarLinea('blue', 0+300, i, i+300, 300);
    dibujarLinea('green', 300, 300+i, i, 300+0);
    dibujarLinea('violet',  300+i, 300, 300, 600-i);
    dibujarLinea('brown', i, 300, 300, 300-i);
    i+=10;
}