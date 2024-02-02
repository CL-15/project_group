import csv
from cash_on_hand import analyze_cash_on_hand
from overheads import find_highest_overhead
from profits_loss import analyze_profit_loss

def read_csv(file_path):
    """
    Reads a CSV file from the given file path and converts it into a list of dictionaries where each row is a dictionary.
    
    Parameter:
    file_path: The path to the CSV file to read.

    Return: 
    A list of dictionaries where each dictionary represents a row in the CSV file.
    """
    data = []
    with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def format_summary_report(highest_overhead, cash_analysis, profit_loss_analysis):
    """
    Creates a formatted summary report string based on the analyzed data.
    
    Parameter:
    highest_overhead: Data about the highest overhead.
    cash_analysis: Analysis results of cash on hand data.
    profit_loss_analysis:  Analysis results of profit and loss data.

    Returns: 
    A formatted string representing the summary report.
    """
    summary_lines = [
        f"[HIGHEST OVERHEAD] {highest_overhead['category'].upper()}: {highest_overhead['amount']}%"
    ]
    
    # Handle cash analysis summary
    if cash_analysis['trend'] == 'fluctuating':
        # List all cash deficit days
        for deficit in cash_analysis['deficit_days']:
            summary_lines.append(f"[CASH DEFICIT] DAY: {deficit['day']}, AMOUNT: SGD{deficit['deficit']}")
        # List the top 3 cash deficits
        summary_lines.append("[HIGHEST CASH DEFICIT] " + 
        f"DAY: {cash_analysis['top_deficits'][0]['day']}, "
        f"AMOUNT: SGD{cash_analysis['top_deficits'][0]['deficit']}"
        )
        summary_lines.append("[2ND HIGHEST CASH DEFICIT] " + 
        f"DAY: {cash_analysis['top_deficits'][1]['day']}, "
        f"AMOUNT: SGD{cash_analysis['top_deficits'][1]['deficit']}"
        )
        summary_lines.append("[3RD HIGHEST CASH DEFICIT] " + 
        f"DAY: {cash_analysis['top_deficits'][2]['day']}, "
        f"AMOUNT: SGD{cash_analysis['top_deficits'][2]['deficit']}"
        )

        # Identify whether there is a cash surplus by matching it with the increasing trend
    elif cash_analysis['trend'] == 'increasing':
        summary_lines.append(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        # List down the day of the highest cash surplus and the amount.
        summary_lines.append(f"[HIGHEST CASH SURPLUS] DAY: {cash_analysis['highest_increment']['day']}, "
                             f"AMOUNT: SGD{abs(cash_analysis ['highest_increment']['amount'])}") # abs to ensure not negative signs

        # Identify whether there is a cash deficit by matching it with the decreasing trend 
    elif cash_analysis['trend'] == 'decreasing':
        summary_lines.append(f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")
        # List down the day of the highest cash deficit and the amount
        summary_lines.append(f"[HIGHEST CASH DEFICIT] DAY: {cash_analysis['highest_decrement']['day']}, "
                             f"AMOUNT: SGD{abs(cash_analysis['highest_decrement']['amount'])}") # abs to ensure not negative signs

    # Handle profit and loss analysis summary
    if profit_loss_analysis['trend'] == 'fluctuating':
        # List all net profit deficit days
        for deficit in profit_loss_analysis['deficit_days']:
            summary_lines.append(f"[NET PROFIT DEFICIT] DAY: {deficit['day']}, AMOUNT: SGD{deficit['deficit']}")
        # List the top 3 profit deficits
        summary_lines.append("[HIGHEST NET PROFIT DEFICIT] " + 
        f"DAY: {profit_loss_analysis['top_deficits'][0]['day']}, "
        f"AMOUNT: SGD{profit_loss_analysis['top_deficits'][0]['deficit']}"
        )
        summary_lines.append("[2ND HIGHEST NET PROFIT DEFICIT] " + 
        f"DAY: {profit_loss_analysis['top_deficits'][1]['day']}, "
        f"AMOUNT: SGD{profit_loss_analysis['top_deficits'][1]['deficit']}"
        )
        summary_lines.append("[3RD HIGHEST NET PROFIT DEFICIT] " + 
        f"DAY: {profit_loss_analysis['top_deficits'][2]['day']}, "
        f"AMOUNT: SGD{profit_loss_analysis['top_deficits'][2]['deficit']}"
        )

        # Identify whether there is a net profit surplus by matching it with the increasing trend
    elif profit_loss_analysis['trend'] == 'increasing':
        summary_lines.append(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
        # List down the day of the highest net profit surplus and the amount
        summary_lines.append(f"[HIGHEST NET PROFIT SURPLUS] DAY: {profit_loss_analysis['highest_increment']['day']}, "
                             f"AMOUNT: SGD{abs(profit_loss_analysis['highest_increment']['amount'])}") # abs to ensure not negative signs
        
        # Identify whether there is a net profit deficit by matching it with the decreasing trend
    elif profit_loss_analysis['trend'] == 'decreasing':
        summary_lines.append(f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY")
        # List Down the day of the highest net profit deficit and the amount
        summary_lines.append(f"[HIGHEST NET PROFIT DEFICIT] DAY: {profit_loss_analysis['highest_decrement']['day']}, "
                             f"AMOUNT: SGD{abs(profit_loss_analysis['highest_decrement']['amount'])}") # abs to ensure not negative signs

    return '\n'.join(summary_lines)

def write_to_summary_report(content, file_path='summary_report.txt'):
    """
    Writes the given content to the summary report text file.
    
    Parameter:
    content: The content to be written to the file
    file_path: The path to the file where the summary report will be written.
    """
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    """
    Main function to orchestrate the process of reading data from CSV files, 
    analyzing it, and writing the summary report
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

