let inputSideOne = document.getElementById('sideOne');
let inputSideTwo = document.getElementById('sideTwo');
let inputSideThree = document.getElementById('sideThree');
let buttonCalculate = document.getElementById('buttonCalculate');
let spanTrianguleType = document.getElementById('trianguleType');
let spanResultArea = document.getElementById('resultArea');

function areaTrianguloEquilatero(sideOne, sideTwo, sideThree){
    let area = (Math.sqrt(3) / 4) * Math.pow(sideOne, 2);
    return area;
}

function areaTrianguloEscaleno(sideOne, sideTwo, sideThree){
    let base = 0;
    let altura = 0;
    let area = 0;

    if(sideOne > sideTwo && sideOne > inputSideThree) {
        base = sideOne;
        altura = (sideTwo * sideThree) / base;
    }else if(sideTwo > sideThree){
        base = sideTwo;
        altura = (sideOne * sideThree) / base;
    }else{
        base = sideThree;
        altura = (sideTwo * sideOne) / base;
    }

    area = (base * altura) / 2;
    return area;

}

function areaTrianguloIsosceles(sideOne, sideTwo, sideThree){
    let base = 0;
    let area = 0;
    let ladosIguales = 0;
    if( sideOne == sideTwo){
        base = sideThree;
        ladosIguales = sideOne;
    }else if(sideTwo == sideThree){
        base = sideTwo;
        ladosIguales = sideOne;
    }else{
        base = sideOne;
        ladosIguales =  sideThree;
    }

    area = (base * (Math.sqrt(Math.pow(ladosIguales, 2))) - (Math.pow(base, 2) / 4)) / 2;
    return area;
}

buttonCalculate.addEventListener('click', () => {
    let resultado = 0;
    let tipoTriangulo = ''
    sideOne = parseFloat(inputSideOne.value);
    sideTwo = parseFloat(inputSideTwo.value);
    sideThree = parseFloat(inputSideThree.value);

    if (sideOne === sideTwo && sideTwo === sideThree && sideThree === sideOne) {
        resultado = areaTrianguloEquilatero(sideOne, sideTwo, sideThree);
        tipoTriangulo = 'Equilatero';
    }else if((sideOne === sideTwo && sideThree != sideOne) || (sideTwo === sideThree && sideTwo != sideOne) || (sideOne === sideThree && sideOne != sideTwo)){
        resultado = areaTrianguloIsosceles(sideOne, sideTwo, sideThree);
        tipoTriangulo = 'Isosceles';
    }else {
        resultado = areaTrianguloEscaleno(sideOne, sideTwo, sideThree);
        tipoTriangulo = 'Escaleno';
    }

    spanResultArea.innerHTML = resultado;
    spanTrianguleType.innerHTML = tipoTriangulo;
});