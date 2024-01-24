def get_deficit_amount(deficit):
    return deficit['deficit']
def analyze_profit_loss(data):
    """
    Analyzes profit and loss data to categorize trends and identify significant changes.
    
    - If increasing, finds the day and amount of the highest increment.
    - If decreasing, finds the day and amount of the highest decrement.
    - If fluctuating, lists all days with a deficit and the top 3 highest deficits.
    """
    # Initialize variables to track the net profit increments and decrements
    highest_increment = 0
    day_of_highest_increment = 0
    highest_decrement = 0
    day_of_highest_decrement = 0
    deficits = []

    # Initialize flags for net profit trend
    always_increasing = True
    always_decreasing = True

    # Loop through each day to calculate the difference in net profit
    previous_net_profit = int(data[0]['Net Profit'])
    for i in range(1, len(data)):
        current_net_profit = int(data[i]['Net Profit'])
        profit_difference = current_net_profit - previous_net_profit

        # Check for always increasing or decreasing
        if profit_difference < 0:
            always_increasing = False
        elif profit_difference > 0:
            always_decreasing = False

        # Update highest increment and decrement
        if profit_difference > highest_increment:
            highest_increment = profit_difference
            day_of_highest_increment = data[i]['Day']
        elif profit_difference < highest_decrement:
            highest_decrement = profit_difference
            day_of_highest_decrement = data[i]['Day']

        # Accumulate deficits
        if profit_difference < 0:
            deficits.append({'day': data[i]['Day'], 'deficit': abs(profit_difference)})

        previous_net_profit = current_net_profit

    # If cash on hand is fluctuating, sort deficits to find the top 3 highest deficits
    if not always_increasing and not always_decreasing:
        top_deficits = sorted(deficits, key=get_deficit_amount, reverse=True)[:3]
    else:
        top_deficits = []


    # Prepare the analysis result
    analysis_result = {
        'trend': 'increasing' if always_increasing else 'decreasing' if always_decreasing else 'fluctuating',
        'highest_increment': {'day': day_of_highest_increment, 'amount': highest_increment} if always_increasing else None,
        'highest_decrement': {'day': day_of_highest_decrement, 'amount': highest_decrement} if always_decreasing else None,
        'deficit_days': deficits if not always_increasing and not always_decreasing else [],
        'top_deficits': top_deficits
    }

    return analysis_result




