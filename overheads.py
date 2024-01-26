def find_highest_overhead(data):
    """
    Identifies the category with the highest overhead expense.

    This function iterates through a list of overhead data, each represented as a dictionary,
    and finds the category with the maximum overhead expense.

    Parameters:
    - data (list of dict): A list where each dictionary contains 'Category' and 'Overheads' keys.

    Returns:
    A dictionary with two keys:
    - 'category': The category with the highest overhead.
    - 'amount': The amount of overhead in this category.
    """

    # Initialize variables to track the highest overhead
    highest_overhead_category = ''
    highest_overhead_amount = 0

    # Loop through each entry in the data list
    for entry in data:
        # Convert the overhead amount from string to float for comparison
        overhead_amount = float(entry['Overheads'])
        # Update the highest overhead and its corresponding category if a new highest is found
        if overhead_amount > highest_overhead_amount:
            highest_overhead_amount = overhead_amount
            highest_overhead_category = entry['Category']

    # Return the category and amount of the highest overhead
    return {
        'category': highest_overhead_category,
        'amount': highest_overhead_amount
    }
