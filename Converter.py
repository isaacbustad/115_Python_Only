farengeighttest = 55.6
celtest = 10.0
kelvintest = 0


def convertFarenheightToCelsius(aFarVal = 20.00):
    retCelVal = 0.0

    # one line execution
    #retCelVal = (aFarVal - 32)*(5/9)

    # multi step calculation
    # subtraction that occours in par
    parsub = aFarVal - 32
    #fraction the par is multiplied by
    fract = 5/9
    # final calculation and assignment of value
    retCelVal = fract * parsub


    return retCelVal



print(convertFarenheightToCelsius(farengeighttest))