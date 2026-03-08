def password_criteria(password) :
    if len(password) < 8 :
        return False
    elif len(password) >= 8 :   
        return True
