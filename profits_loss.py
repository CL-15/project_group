def analyze_profit_loss(data):
    """
    Analyzes profit and loss data to find:
    - Days with the highest net profit surplus
    - Days with the highest net profit deficit
    """
    highest_surplus = 0
    day_of_highest_surplus = None
    highest_deficit = 0
    day_of_highest_deficit = None

    # Tracks if net profit is always increasing or decreasing
    always_increasing = True
    always_decreasing = True

    # Assuming the data is a list of dictionaries with 'Day' and 'Net Profit' keys
    previous_net_profit = float(data[0]['Net Profit'])  # Initialize with the first day's net profit

    for entry in data:
        current_net_profit = float(entry['Net Profit'])
        # Check for surplus/deficit
        if current_net_profit > highest_surplus:
            highest_surplus = current_net_profit
            day_of_highest_surplus = entry['Day']
        if current_net_profit < highest_deficit:
            highest_deficit = current_net_profit
            day_of_highest_deficit = entry['Day']

        # Check if net profit is always increasing or decreasing
        if current_net_profit < previous_net_profit:
            always_increasing = False
        elif current_net_profit > previous_net_profit:
            always_decreasing = False

        previous_net_profit = current_net_profit

    return {
        'always_increasing': always_increasing,
        'always_decreasing': always_decreasing,
        'highest_surplus': highest_surplus,
        'day_of_highest_surplus': day_of_highest_surplus,
        'highest_deficit': highest_deficit,
        'day_of_highest_deficit': day_of_highest_deficit
    }
