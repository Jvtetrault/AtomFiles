def interpret(string):
    if string.lower() == "daily":
        return 1
    elif string.lower() == "weekly":
        return 7
    elif string.lower() == "bi-weekly":
        return 14
    elif string.lower() == "monthly":
        return 31
    elif string.lower() == "semi-Annually":
        return 183
    elif string.lower() == "yearly":
        return 365
    elif string.lower() == "1 years":
        return 365
    elif string.lower() == "2 years":
        return 730
    elif string.lower() == "3 years":
        return 1095
    elif string.lower() == "4 years":
