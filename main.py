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
        f"[HIGHEST OVERHEAD] {highest_overhead['category']} EXPENSE: {highest_overhead['amount']}%"
    ]
    
    # Handle cash analysis summary
    if cash_analysis['trend'] == 'fluctuating':
        # List all cash deficit days
        for deficit in cash_analysis['deficit_days']:
            summary_lines.append(f"[CASH DEFICIT] DAY: {deficit['day']}, AMOUNT: SGD{deficit['deficit']}")
        # List the top 3 cash deficits
        summary_lines.append("[HIGHEST CASH DEFICIT] " + 
        f"DAY: {cash_analysis['top_deficits'][0]['day']}, AMOUNT: SGD{cash_analysis['top_deficits'][0]['deficit']}"
        )
        summary_lines.append("[2ND HIGHEST CASH DEFICIT] " + 
        f"DAY: {cash_analysis['top_deficits'][1]['day']}, AMOUNT: SGD{cash_analysis['top_deficits'][1]['deficit']}"
        )
        summary_lines.append("[3RD HIGHEST CASH DEFICIT] " + 
        f"DAY: {cash_analysis['top_deficits'][2]['day']}, AMOUNT: SGD{cash_analysis['top_deficits'][2]['deficit']}"
        )
    elif cash_analysis['trend'] == 'increasing':
        summary_lines.append(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        summary_lines.append(f"[HIGHEST CASH SURPLUS] DAY: {cash_analysis['highest_increment']['day']}, AMOUNT: SGD{cash_analysis['highest_increment']['amount']}")
    elif cash_analysis['trend'] == 'decreasing':
        summary_lines.append(f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")
        summary_lines.append(f"[HIGHEST CASH DEFICIT] DAY: {cash_analysis['highest_decrement']['day']}, AMOUNT: SGD{cash_analysis['highest_decrement']['amount']}")

    # Handle profit and loss analysis summary
    if profit_loss_analysis['trend'] == 'fluctuating':
        # List all net profit deficit days
        for deficit in profit_loss_analysis['deficit_days']:
            summary_lines.append(f"[NET PROFIT DEFICIT] DAY: {deficit['day']}, AMOUNT: SGD{deficit['deficit']}")
        # List the top 3 profit deficits
        summary_lines.append("[HIGHEST NET PROFIT DEFICIT] " + 
        f"DAY: {profit_loss_analysis['top_deficits'][0]['day']}, AMOUNT: SGD{profit_loss_analysis['top_deficits'][0]['deficit']}"
        )
        summary_lines.append("[2ND HIGHEST NET PROFIT DEFICIT] " + 
        f"DAY: {profit_loss_analysis['top_deficits'][1]['day']}, AMOUNT: SGD{profit_loss_analysis['top_deficits'][1]['deficit']}"
        )
        summary_lines.append("[3RD HIGHEST NET PROFIT DEFICIT] " + 
        f"DAY: {profit_loss_analysis['top_deficits'][2]['day']}, AMOUNT: SGD{profit_loss_analysis['top_deficits'][2]['deficit']}"
        )
    elif profit_loss_analysis['trend'] == 'increasing':
        summary_lines.append(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        summary_lines.append(f"[HIGHEST NET PROFIT SURPLUS] DAY: {profit_loss_analysis['highest_increment']['day']}, AMOUNT: SGD{profit_loss_analysis['highest_increment']['amount']}")
    elif profit_loss_analysis['trend'] == 'decreasing':
        summary_lines.append(f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY")
        summary_lines.append(f"[HIGHEST NET PROFIT DEFICIT] DAY: {profit_loss_analysis['highest_decrement']['day']}, AMOUNT: SGD{profit_loss_analysis['highest_decrement']['amount']}")

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
    # Read the data from CSV files and analyze
    cash_data = read_csv('csv_reports/Cash_on_Hand.csv')
    profit_loss_data = read_csv('csv_reports/Profits_and_Loss.csv')
    overheads_data = read_csv('csv_reports/Overheads.csv')

    cash_analysis = analyze_cash_on_hand(cash_data)
    profit_loss_analysis = analyze_profit_loss(profit_loss_data)
    highest_overhead = find_highest_overhead(overheads_data)

    # Format and write the summary report
    summary_content = format_summary_report(highest_overhead, cash_analysis, profit_loss_analysis)
    write_to_summary_report(summary_content)

if __name__ == "__main__":
    main()

