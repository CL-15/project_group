def analyze_cash_on_hand(data):
    """
    Analyzes cash on hand data to:
    - Determine if the cash on hand is always increasing or decreasing.
    - Find the day with the highest increment if always increasing.
    - Find the day with the highest decrement if always decreasing.
    - If fluctuating, list all days with a deficit and identify the top 3 highest deficits.
    """
    # Initialize variables to track the cash on hand increments and decrements
    highest_increment = 0
    day_of_highest_increment = None
    highest_decrement = 0
    day_of_highest_decrement = None
    deficits = []
    differences = []  # List to keep track of daily differences

    # Initialize flags for determining if cash on hand is always increasing or decreasing
    always_increasing = True
    always_decreasing = True

    # Starting with the second entry, compare each day's cash on hand to the previous day
    previous_amount = int(data[0]['Cash On Hand'])
    for i in range(1, len(data)):
        current_amount = int(data[i]['Cash On Hand'])
        difference = current_amount - previous_amount
        differences.append(difference)  # Store the difference for each day

        # Identify the highest increment and decrement
        if difference > highest_increment:
            highest_increment = difference
            day_of_highest_increment = data[i]['Day']
        if difference < highest_decrement:
            highest_decrement = difference
            day_of_highest_decrement = data[i]['Day']

        # If there is any day where the cash on hand did not increase, it is not always increasing
        if difference < 0:
            always_increasing = False
            deficits.append({'day': data[i]['Day'], 'deficit': difference})

        # If there is any day where the cash on hand did not decrease, it is not always decreasing
        if difference > 0:
            always_decreasing = False

        # Update the previous cash on hand amount for the next iteration
        previous_amount = current_amount

    # List to keep all deficit days
    all_deficits = [{'day': data[i]['Day'], 'deficit': difference} for i, difference in enumerate(differences) if difference < 0]

    # Construct the results dictionary
    result = {
        'always_increasing': always_increasing,
        'day_of_highest_increment': day_of_highest_increment if always_increasing else None,
        'amount_highest_increment': highest_increment if always_increasing else None,
        'always_decreasing': always_decreasing,
        'day_of_highest_decrement': day_of_highest_decrement if always_decreasing else None,
        'amount_highest_decrement': highest_decrement if always_decreasing else None,
        'fluctuating': not always_increasing and not always_decreasing,
        'deficits': deficits,  # This includes all deficit days
        'top_deficits': sorted(deficits, key=lambda x: x['deficit'])[:3],  # Top 3 deficits
        'all_deficits': all_deficits,  # This is the new line, including all deficits
        'deficit_days': all_deficits
    }

    return result



