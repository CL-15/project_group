def get_deficit_amount(deficit):
    """
    Retrieves the deficit amount from a deficit record.

    Parameter:
    deficit (dict): A dictionary representing a deficit record.

    Returns:
    int: The amount of the deficit.
    """
    return deficit['deficit']
def analyze_profit_loss(data):
    """
    Analyzes profit and loss data to categorize trends (increasing, decreasing, or fluctuating)
    and to identify significant financial changes such as the highest increments or decrements
    in net profit, and the top three highest deficits in case of fluctuating trend.
    
    - If increasing, finds the day and amount of the highest net profit surplus(increment)
    - If decreasing, finds the day and amount of the highest net profit deficit(decrement)
    - If fluctuating, lists all days with a deficit and the top 3 highest deficits

    Parameters:
    data (list of dict): List of dictionaries containing 'Day' and 'Net Profit' data

    Returns:
    A dictionary containing the analysis results with the trend, highest increment/decrement,
    and top deficits if the trend is fluctuating.
    """
    # Initialize variables for tracking net profit changes
    highest_increment = 0
    day_of_highest_increment = 0
    highest_decrement = 0
    day_of_highest_decrement = 0
    deficits = []

    # Flags to identify the overall trend of net profit
    always_increasing = True
    always_decreasing = True

    # Analyzing each day's net profit to identify trend and significant changes
    previous_net_profit = int(data[0]['Net Profit'])
    for i in range(1, len(data)):
        current_net_profit = int(data[i]['Net Profit'])
        profit_difference = current_net_profit - previous_net_profit

        # Updating trend flags based on profit difference
        if profit_difference < 0:
            always_increasing = False
        elif profit_difference > 0:
            always_decreasing = False

        # Identifying the highest increment and decrement in net profit
        if profit_difference > highest_increment:
            highest_increment = profit_difference
            day_of_highest_increment = data[i]['Day']
        elif profit_difference < highest_decrement:
            highest_decrement = profit_difference
            day_of_highest_decrement = data[i]['Day']

        # Recording deficits for fluctuating trend scenario
        if profit_difference < 0:
            deficits.append({'day': data[i]['Day'], 'deficit': abs(profit_difference)})

        # Prepare for the next iteration
        previous_net_profit = current_net_profit

    # Determining top 3 deficits if the trend is fluctuating
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

    # Compiling and returning the analysis results
    analysis_result = {
        'trend': 'increasing' if always_increasing else 'decreasing' if always_decreasing else 'fluctuating',
        'highest_increment': {'day': day_of_highest_increment, 'amount': highest_increment} if always_increasing else None,
        'highest_decrement': {'day': day_of_highest_decrement, 'amount': highest_decrement} if always_decreasing else None,
        'deficit_days': deficits if not always_increasing and not always_decreasing else [],
        'top_deficits': top_deficits
    }

    return analysis_result




