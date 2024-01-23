def analyze_profit_loss(data):
    """
    Analyzes profit and loss data to handle three scenarios:
    - If net profit is always increasing, find the day and amount of the highest increment.
    - If net profit is always decreasing, find the day and amount of the highest decrement.
    - If net profit fluctuates, list all days when a deficit occurs and the top 3 highest deficits.
    """
    # Initialize variables for tracking net profit trends and amounts
    highest_increment = 0
    day_of_highest_increment = None
    highest_decrement = 0
    day_of_highest_decrement = None
    deficits = []

    # Initialize flags for always increasing or decreasing
    always_increasing = True
    always_decreasing = True

    # Start with the first day's net profit as the previous value to compare against
    previous_net_profit = float(data[0]['Net Profit'])

    # Iterate over each day's data
    for i in range(1, len(data)):
        current_net_profit = float(data[i]['Net Profit'])
        profit_difference = current_net_profit - previous_net_profit

        # Check for always increasing/decreasing trends
        if profit_difference < 0:
            always_increasing = False
        if profit_difference > 0:
            always_decreasing = False

        # Check for highest increment/decrement
        if profit_difference > highest_increment:
            highest_increment = profit_difference
            day_of_highest_increment = data[i]['Day']
        elif profit_difference < highest_decrement:
            highest_decrement = profit_difference
            day_of_highest_decrement = data[i]['Day']

        # Track all deficit days and amounts
        if profit_difference < 0:
            deficits.append({'day': data[i]['Day'], 'deficit': profit_difference})

        # Update the previous net profit for the next day's comparison
        previous_net_profit = current_net_profit

    # Sort the deficits to find the top 3. Note that since these are deficits, they will be negative numbers, 
    # so we sort them in descending order to get the 3 largest (most negative) values.
    top_deficits = sorted(deficits, key=lambda x: x['deficit'], reverse=True)[:3]

    # Prepare the analysis result
    analysis_result = {
        'always_increasing': always_increasing,
        'day_of_highest_increment': day_of_highest_increment if always_increasing else None,
        'amount_highest_increment': highest_increment if always_increasing else None,
        'always_decreasing': always_decreasing,
        'day_of_highest_decrement': day_of_highest_decrement if always_decreasing else None,
        'amount_highest_decrement': highest_decrement if always_decreasing else None,
        'deficit_days': deficits if not always_increasing and not always_decreasing else [],
        'top_3_deficits': top_deficits  # Now this line ensures that top_3_deficits is always present
    }

    return analysis_result


