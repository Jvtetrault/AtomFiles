# Simple Interpreter object definition for varying text to number conversion

def interpret(string):
    a = ((string.lower()).replace(" ", "")).strip()
    if a == "daily":
        return 1
    elif a == "weekly":
        return 7
    elif a == "bi-weekly":
        return 14
    elif a == "monthly":
        return 31
    elif a == "semi-Annually":
        return 183
    elif a == "yearly":
        return 365
    elif a == "1years":
        return 365
    elif a == "2years":
        return 730
    elif a == "3years":
        return 1095
    elif a == "4years":
        return 1460
    elif a == "5years":
        return 1825
    elif a == "6years":
        return 2190
    elif a == "-":
        return 0
    elif a == "7Days":
        return 7
    elif a == "firstmonth":
        return 31
    elif a == "6months":
        return 186
    elif a == "9months":
        return 279
    elif a == "1year":
        return 365
    else:
        print('"'+ string + '" please view documentation of Interpreter: Passed string is outside library of defined passable arguments')
