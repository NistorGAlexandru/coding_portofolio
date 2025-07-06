# https://dontpad.com/cnptestare2

from datetime import datetime, date
from an_bisect import este_bisect

## TDD -> TEST DRIVEN DEVELOPMENT
def este_valid(cnp:str) -> bool:
    if len(cnp) != 13:
        return False
    if cnp[0] == '9' or cnp[0] == '0':
        return False
    if not cnp.isnumeric():
        return False
    today = datetime.now()
    
    ## anul este cel mult cel curent
    if (cnp[0] in '56') and (cnp[1:3] > str(today.year)[2:]):
        return False

    if cnp[0] in '56' : start_an = '20'
    elif cnp[0] in '12' : start_an = '19'
    elif cnp[0] in '34' : start_an = '18'
    elif cnp[0] in '78' : start_an = '20' 

    an =  start_an + cnp[1:3]
    an = int(an)


    luna = int(cnp[3:5])
    if luna not in range(1, 13):
        return False 

    ziua = int(cnp[5:7])
    if ziua not in range(1, 32):
        return False 

    if luna in [4, 6, 9, 11] and ziua == 31:
        return False

    if luna == 2 and ziua > (28 + este_bisect(an)):
        print("an", an)
        return False
    
    jj = int(cnp[7:9])
    if jj not in (list(range(1, 49)) + [51, 52]) :
        return False 

    """

    Calcularea componentei C se face folosind constanta "279146358279", după cum urmează:

    fiecare cifră din primele 12 cifre ale C.N.P. este înmulțită cu corespondentul său din constantă
    rezultatele sunt însumate și totalul se împarte la 11
    dacă restul împărțirii este mai mic de 10, acela reprezintă valoarea componentei C
    dacă restul împărțirii este 10, valoarea componentei C este 1
    

    """
    # return True

    c = int(cnp[-1])
    VALIDATOR = "279146358279"
    cifre = cnp[:12]

    rezultat = sum([ int(VALIDATOR[i]) * int(cifre[i])   for i in range(12) ])
    rezultat = rezultat % 11

    if rezultat < 10:
        if c != rezultat:
            return False
    else:
        if c != 1:
            return False

    return True



def extract_birthday(cnp):
    if cnp[0] in '56' : start_an = '20'
    elif cnp[0] in '12' : start_an = '19'
    elif cnp[0] in '34' : start_an = '18'
    elif cnp[0] in '78' : start_an = '20' 

    an = int(start_an + cnp[1:3])
    luna = int(cnp[3:5])
    ziua = int(cnp[5:7])

    return datetime(an, luna, ziua)


def is_male(cnp):
    return cnp[0] in "1357"


def is_under(birth, min_age = 18):
    now = date.today()
    return (
        now.year - birth.year < min_age
        or now.year - birth.year == min_age and (
            now.month < birth.month 
            or now.month == birth.month and now.day <= birth.day
        )
    )

def is_over(birth, min_age = 18):
    return not is_under(birth, min_age)

def are_acces(cnp) -> bool:
    if not este_valid(cnp): return False
    bday = extract_birthday(cnp)
    print('bday:', bday)
    male = is_male(cnp)
    print('male:', male)

    return is_under(bday, 70) and ((male and not is_under(bday, 18))  or (not male and not is_under(bday, 16)))






