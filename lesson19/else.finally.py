def safe_divide():
    try:
        nom = int(input("Give nominator: "))
        denom = int(input("Give denominator: "))
        res = nom/denom
    except ZeroDivisionError:
        print("Error! Denom is 0")
    except Exception as e:
        print("Something went really wrong: " + str(e))
    else:
        return res
    finally:
        return None

safe_divide()


