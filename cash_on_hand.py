def get_deficit_amount(deficit):
    """
    Retrieves the deficit amount from a deficit record.

    Parameter:
    deficit (dict): A dictionary representing a deficit record.

    Returns:
    The amount of the deficit.
    """
    return deficit['deficit']
def analyze_cash_on_hand(data):
    """
    Analyzes cash on hand data to determine trends and identify significant changes.
    It categorizes the data into increasing, decreasing, or fluctuating trends and 
    finds the highest increment/decrement in cash or the top deficits.
    
    - If increasing, finds the day and amount of the highest cash surplus(increments)
    - If decreasing, finds the day and amount of the highest cash deficit(decrements)
    - If fluctuating, lists all days with a deficit and the top 3 highest deficits

    Parameter:
    data (list of dict): List of dictionaries containing 'Day' and 'Cash On Hand' data.

    Returns:
    A dictionary containing analysis results such as trend, highest increment/decrement, 
    and top deficits.
    """
    # Initialize variables for tracking increments, decrements, and deficits
    highest_increment = 0
    day_of_highest_increment = 0
    highest_decrement = 0
    day_of_highest_decrement = 0
    deficits = []

    # Flags to identify if cash on hand is always increasing or decreasing
    always_increasing = True
    always_decreasing = True

    # Analyze the trend by calculating daily differences
    previous_day_cash = int(data[0]['Cash On Hand'])
    for i in range(1, len(data)):
        current_day_cash = int(data[i]['Cash On Hand'])
        difference = current_day_cash - previous_day_cash

        # Update flags based on the difference
        if difference < 0:
            always_increasing = False
        elif difference > 0:
            always_decreasing = False

        # Identifying the highest increment and decrement in Cash on hand
        if difference > highest_increment:
            highest_increment = difference
            day_of_highest_increment = data[i]['Day']
        elif difference < highest_decrement:
            highest_decrement = difference
            day_of_highest_decrement = data[i]['Day']


        # Accumulate all deficits for fluctuating trend analysis
        if difference < 0:
            deficits.append({'day': data[i]['Day'], 'deficit': abs(difference)})

        # Set up for next iteration comparison
        previous_day_cash = current_day_cash

    # Identify the top 3 highest deficits if the trend is fluctuating
    if not always_increasing and not always_decreasing:
        # Make a copy of the deficits list for finding top 3 deficits
        deficits_copy = deficits[:]
        top_deficits = []
        for _ in range(3):
            # Initialize with the first element of the list or a default value
            highest_current_deficit = deficits_copy[0] if deficits_copy else {'day': None, 'deficit': 0}
            highest_deficit_index = 0 if deficits_copy else None

            # Searching for the highest deficit in the copied list
            for index, deficit in enumerate(deficits_copy[1:], start=1):  # Start from the second element
                if deficit['deficit'] > highest_current_deficit['deficit']:
                    highest_current_deficit = deficit
                    highest_deficit_index = index

            # Adding the found deficit to top deficits and removing it from the copy list
            if highest_deficit_index is not None:
                top_deficits.append(highest_current_deficit)
                deficits_copy.pop(highest_deficit_index)
    else:
        top_deficits = []

    # Compile and return the analysis results
    results = {
        'trend': 'increasing' if always_increasing else 'decreasing' if always_decreasing else 'fluctuating',
        'highest_increment': {'day': day_of_highest_increment, 'amount': highest_increment} if always_increasing else None,
        'highest_decrement': {'day': day_of_highest_decrement, 'amount': highest_decrement} if always_decreasing else None,
        'deficit_days': deficits if not always_increasing and not always_decreasing else [],
        'top_deficits': top_deficits
    }

    return results


    








