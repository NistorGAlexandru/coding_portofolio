

from cnp import este_valid
## TDD -> TEST DRIVEN DEVELOPMENT


def test_este_valid_cnp():
    # Lungimea - 13 caractere
    assert este_valid("123456789012") == False, "lungimea nu poate fi de 12 caractere"
    assert este_valid("12345678901234") == False, "lungimea nu poate fi de 14 caractere"

    ### Trebuie sa inceapa cu 1, 2... 7.8
    assert este_valid("9234567890123") == False, "prima cifra nu poate fi 9"
    assert este_valid("0234567890123") == False, "prima cifra nu poate fi 0"

    assert este_valid("A234567890123") == False, "trebuie sa fie numeric, nu poate contine litere"

    # 2073 - nu este valid (anul trebuie sa fie cel putin cel curent) 
    assert este_valid("6734567890123") == False, "anul trebuie sa fie cel mult 2024"

    ## luna trebuie sa fie intre 01 si 12
    assert este_valid("5000001234567") == False, "luna trebuie sa fie intre 01 si 12"
    assert este_valid("5001301234567") == False, "luna trebuie sa fie intre 01 si 12"
    assert este_valid("5002001234567") == False, "luna trebuie sa fie intre 01 si 12"
    assert este_valid("5003101234567") == False, "luna trebuie sa fie intre 01 si 12"

    ## zi trebuie sa fie in tre 01 si 31
    assert este_valid("5000100234567") == False, "ziua trebuie sa fie intre 01 si 31"
    assert este_valid("5000132234567") == False, "ziua trebuie sa fie intre 01 si 31"
    assert este_valid("5000142234567") == False, "ziua trebuie sa fie intre 01 si 31"


    ## zi si luna cu 30 de zile
    assert este_valid("5000431234567") == False, "ziua de 31 nu exista in luna aprilie"
    assert este_valid("5000631234567") == False, "ziua de 31 nu exista in luna iunie"
    assert este_valid("5000931234567") == False, "ziua de 31 nu exista in luna septembrie"
    assert este_valid("5001131234567") == False, "ziua de 31 nu exista in luna noiembrie"

    ## februarie si luna cu 28 sau 29 de zile
    assert este_valid("5000230234567") == False, "ziua de 30 nu exista in februarie"

    assert este_valid("5230229234567") == False, "ziua de 29 nu exista in februarie in an nebisect"

    assert este_valid("3000229234567") == False, "ziua de 29 nu exista in februarie in an nebisect"

    assert este_valid("1000229234567") == False, "ziua de 29 nu exista in februarie in an nebisect"

    # assert este_valid("5000229234567") == True, "ziua de 29 nu exista in februarie in an nebisect"


    assert este_valid("5000221494567") == False, "Componenta JJ trebuie sa fie intre 1 si 48 sau 51, 52"
    assert este_valid("5000221504567") == False, "Componenta JJ trebuie sa fie intre 1 si 48 sau 51, 52"
    assert este_valid("5000221534567") == False, "Componenta JJ trebuie sa fie intre 1 si 48 sau 51, 52"

    #"279146358279" - este corect
    assert este_valid("279146358279") == False, "Componenta JJ trebuie sa fie intre 1 si 48 sau 51, 52"

    ### aici introduceti cnp-ul vostru
    assert este_valid("2990219469000") == True, "Componenta C care trebuie validata"

    assert este_valid("2990219469001") == False, "Componenta C care trebuie validata"

if __name__ == "__main__":
    test_este_valid_cnp()

