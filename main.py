import csv
from cash_on_hand import analyze_cash_on_hand
from overheads import find_highest_overhead
from profits_loss import analyze_profit_loss

def read_csv(file_path):
    """
    Reads a CSV file from the given file path and converts it into a list of dictionaries.
    
    :param file_path: The path to the CSV file to read.
    :return: A list of dictionaries where each dictionary represents a row from the CSV.
    """
    data = []
    with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def format_summary_report(highest_overhead, cash_analysis, profit_loss_analysis):
    """
    Formats the summary report content from the analyzed data.
    
    :param highest_overhead: Dictionary containing the highest overhead data.
    :param cash_analysis: Dictionary containing cash analysis data.
    :param profit_loss_analysis: Dictionary containing profit/loss analysis data.
    :return: A string that represents the formatted summary report.
    """
    summary_lines = [
        f"HIGHEST OVERHEAD: {highest_overhead['category']} EXPENSE: {highest_overhead['amount']}"
    ]
    
    # Add the highest cash increment and decrement information to the summary lines
    summary_lines.append(
        f"HIGHEST CASH INCREMENT: DAY: {cash_analysis['day_of_highest_increment']}, "
        f"AMOUNT: SGD{cash_analysis['highest_increment']}"
    )
    summary_lines.append(
        f"HIGHEST CASH DECREMENT: DAY: {cash_analysis['day_of_highest_decrement']}, "
        f"AMOUNT: SGD{-cash_analysis['highest_decrement']}"  # Assuming the decrement is a negative number
    )
    
    # Add the highest profit surplus and deficit information to the summary lines
    summary_lines.append(
        f"HIGHEST PROFIT SURPLUS: DAY: {profit_loss_analysis['day_of_highest_surplus']}, "
        f"AMOUNT: SGD{profit_loss_analysis['highest_surplus']}"
    )
    summary_lines.append(
        f"HIGHEST PROFIT DEFICIT: DAY: {profit_loss_analysis['day_of_highest_deficit']}, "
        f"AMOUNT: SGD{-profit_loss_analysis['highest_deficit']}"  # Assuming the deficit is a negative number
    )
    
    # Add information about the trend of net profit
    if profit_loss_analysis['always_increasing']:
        summary_lines.append("NET PROFIT TREND: ALWAYS INCREASING")
    elif profit_loss_analysis['always_decreasing']:
        summary_lines.append("NET PROFIT TREND: ALWAYS DECREASING")
    else:
        summary_lines.append("NET PROFIT TREND: FLUCTUATING")

    # Combine all lines into a single string separated by newlines
    return '\n'.join(summary_lines)

def write_to_summary_report(content, file_path='summary_report.txt'):
    """
    Writes the given content to the summary report text file.
    
    :param content: The content to write to the file.
    :param file_path: The path to the file where the summary report will be written.
    """
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    """
    Main function that orchestrates the reading, analyzing, formatting, and writing of the summary report.
    """
    # Read the data from CSV files
    cash_data = read_csv('csv_reports/Cash_on_Hand.csv')
    profit_loss_data = read_csv('csv_reports/Profits_and_Loss.csv')
    overheads_data = read_csv('csv_reports/Overheads.csv')

    # Analyze the data
    cash_analysis = analyze_cash_on_hand(cash_data)
    profit_loss_analysis = analyze_profit_loss(profit_loss_data)
    highest_overhead = find_highest_overhead(overheads_data)

    # Format the summary report content
    summary_content = format_summary_report(highest_overhead, cash_analysis, profit_loss_analysis)

    # Write the formatted summary report content to the file
    write_to_summary_report(summary_content)

# Entry point of the script
if __name__ == "__main__":
    main()

