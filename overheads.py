def find_highest_overhead(data):
    """
    Finds the highest overhead category from the overheads data.
    :param data: A list of dictionaries, each containing 'Category' and 'Overheads' keys.
    :return: A dictionary with the highest overhead category and its amount.
    """
    highest_overhead_category = ''
    highest_overhead_amount = 0

    # Assuming the data is a list of dictionaries with 'Category' and 'Overheads' keys
    for entry in data:
        # Convert the overhead amount to float and compare
        overhead_amount = float(entry['Overheads'])
        if overhead_amount > highest_overhead_amount:
            highest_overhead_amount = overhead_amount
            highest_overhead_category = entry['Category']

    return {
        'category': highest_overhead_category,
        'amount': highest_overhead_amount
    }
