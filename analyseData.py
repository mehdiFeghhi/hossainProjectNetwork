def main(**kwargs):
    good_ping = get_good()
    bad_ping  = get_bad()
    if kwargs_1 == 1 :
        if (kwargs_2 > 0 and kwargs_2 < good_ping and kwargs_3 < 35):   
                return 1
        elif (kwargs_2.value > good_ping and kwargs_3.value < bad_ping and kwargs_3.value < 35):
                return 2
        else :
            return 3
    else :
        return 0 

def get_good():
    number1 = int(input('enter the best ping : '))
    return number1
def get_bad():
    number2 = int(input('enter bad ping = '))
    return number2
