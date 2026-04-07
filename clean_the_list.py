def clean_list(shopping_list):
    if not shopping_list:
        return []

    cleaned = shopping_list.copy()

    if 'milk' not in cleaned:
        cleaned.append('milk')

    final_list = []
    
    for index, item in enumerate(cleaned, start=1):
        formatted_item = item.strip().capitalize()
        final_list.append(f"{index}/ {formatted_item}")

    return final_list
