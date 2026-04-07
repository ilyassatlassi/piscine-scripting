def remember_the_apple(shopping_list):
    if not shopping_list:
        return shopping_list
    if not "apple" in shopping_list:
        shopping_list.append("apple")
    return shopping_list    
        
