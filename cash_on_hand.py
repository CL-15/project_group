def analyze_cash_on_hand(data):
    """
    Analyzes cash on hand data to find:
    - The day with the highest cash increment
    - The day with the highest cash decrement
    """
    highest_increment = 0
    day_of_highest_increment = None
    highest_decrement = 0
    day_of_highest_decrement = None

    # Assuming the data is a list of dictionaries with 'Day' and 'Cash on Hand' keys
    for i in range(1, len(data)):
        # Calculate the difference from the previous day
        difference = int(data[i]['Cash On Hand']) - int(data[i - 1]['Cash On Hand'])
        if difference > highest_increment:
            highest_increment = difference
            day_of_highest_increment = data[i]['Day']
        elif difference < highest_decrement:
            highest_decrement = difference
            day_of_highest_decrement = data[i]['Day']

    return {
        'highest_increment': highest_increment,
        'day_of_highest_increment': day_of_highest_increment,
        'highest_decrement': highest_decrement,
        'day_of_highest_decrement': day_of_highest_decrement
    }
