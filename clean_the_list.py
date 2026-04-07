def clean_list(shopping_list):
    if not shopping_list:
        return []
    normalized = [item.strip().lower() for item in shopping_list]

    if 'milk' not in normalized:
        shopping_list.append('milk')

    final_list = []
    
    for index, item in enumerate(shopping_list, start=1):
        formatted_item = item.strip().capitalize()
        final_list.append(f"{index}/ {formatted_item}")

    return final_list
