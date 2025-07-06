#https://dontpad.com/cnptestare3

def este_bisect(an):
    ## Version 1
    return an % 400 == 0 or (an % 4 == 0  and an % 100 != 0) 

    ## Version 2
    if an % 400 == 0:
        return True
    elif an % 100 != 0 and an % 4 == 0:
        return True
    else:
        return False
    
    ## Version 3
    return not (an % 4 or (an % 100 == 0 and an % 400))


def test_an_bisect():
    assert  este_bisect(2024) == True, "Anul 2024 este bisect"
    assert  este_bisect(2023) == False, "Anul 2023 nu este bisect"

    assert  este_bisect(2000) == True, "Anul 2000 este bisect"
    assert  este_bisect(2100) == False, "Anul 2100 nu este bisect"


if __name__ == "__main__":
    test_an_bisect()