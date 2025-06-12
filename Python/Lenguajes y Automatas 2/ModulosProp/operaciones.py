def calculadora(num1,num2,op):
    sumar = num1+num2
    restar = num1-num2
    multi = num1*num2
    divi = num1/num2
    if op == "suma":
        return sumar
    if op == "resta":
        return restar
    if op == "multiplicacion":
        return multi
    if op == "division":
        return divi