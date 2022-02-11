function factorial(a){
    if (a % 1){
        return 'Error. Solo valores enteros se permiten';
    }else if (a < 0){
        return 'Error. Solo valores positivos permitidos';
    }else{
        if (a === 0 || a === 1){
            return 1;
        }else{
            return a * factorial(a-1);
        }
    }
}

function combinatoria(a,b){
    if (a % 1 || b % 1){
        return 'Error. Solo números enteros son permitidos.';
    }else if (a < 0 || b < 0){
        return 'Error. Solo números positivos son permitidos.';
    }else if (a < b){
        return 'Error. El primer número debe ser mayor o igual que el segundo número.';
    }else{
        return factorial(a)/(factorial(b)*factorial(a-b));
    }
}
