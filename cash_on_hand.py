def get_deficit_amount(deficit):
    return deficit['deficit']
def analyze_cash_on_hand(data):
    """
    Analyzes cash on hand data to categorize trends and identify significant changes.
    
    - If increasing, finds the day and amount of the highest increment.
    - If decreasing, finds the day and amount of the highest decrement.
    - If fluctuating, lists all days with a deficit and the top 3 highest deficits.
    """
    # Initialize variables for increment/decrement tracking
    highest_increment = 0
    day_of_highest_increment = 0
    highest_decrement = 0
    day_of_highest_decrement = 0
    deficits = []

    # Initialize flags for cash trend
    always_increasing = True
    always_decreasing = True

    # Calculate the difference from the previous day and analyze the trend
    previous_day_cash = int(data[0]['Cash On Hand'])
    for i in range(1, len(data)):
        current_day_cash = int(data[i]['Cash On Hand'])
        difference = current_day_cash - previous_day_cash

        # Check for always increasing or decreasing
        if difference < 0:
            always_increasing = False
        elif difference > 0:
            always_decreasing = False

        # Update highest increment and decrement
        if difference > highest_increment:
            highest_increment = difference
            day_of_highest_increment = data[i]['Day']
        elif difference < highest_decrement:
            highest_decrement = difference
            day_of_highest_decrement = data[i]['Day']

        # Accumulate deficits
        if difference < 0:
            deficits.append({'day': data[i]['Day'], 'deficit': abs(difference)})

        # Update for the next iteration
        previous_day_cash = current_day_cash

    # If cash on hand is fluctuating, sort deficits to find the top 3 highest deficits
    if not always_increasing and not always_decreasing:
        top_deficits = sorted(deficits, key=get_deficit_amount, reverse=True)[:3]
    else:
        top_deficits = []

    # Construct the results dictionary
    results = {
        'trend': 'increasing' if always_increasing else 'decreasing' if always_decreasing else 'fluctuating',
        'highest_increment': {'day': day_of_highest_increment, 'amount': highest_increment} if always_increasing else None,
        'highest_decrement': {'day': day_of_highest_decrement, 'amount': highest_decrement} if always_decreasing else None,
        'deficit_days': deficits if not always_increasing and not always_decreasing else [],
        'top_deficits': top_deficits
    }

    return results


    








