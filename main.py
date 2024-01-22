import csv
from cash_on_hand import analyze_cash_on_hand
from overheads import find_highest_overhead
from profits_loss import analyze_profit_loss

def read_csv(file_path):
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    Each row is represented by a dictionary with keys as the column headers.
    """
    data = []
    with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def write_to_summary_report(content, file_path='summary_report.txt'):
    """
    Writes content to the summary report text file.
    """
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    # Read the data from CSV files
    cash_data = read_csv('csv_reports/Cash_on_Hand.csv')
    profit_loss_data = read_csv('csv_reports/Profits_and_Loss.csv')
    overheads_data = read_csv('csv_reports/Overheads.csv')

    # Analyze the data
    cash_analysis = analyze_cash_on_hand(cash_data)
    profit_loss_analysis = analyze_profit_loss(profit_loss_data)
    highest_overhead = find_highest_overhead(overheads_data)

    # Prepare the summary report content
    summary_content = f"Highest Overhead: {highest_overhead}\n"
    summary_content += f"Cash On Hand Analysis:\n{cash_analysis}\n"
    summary_content += f"Profit & Loss Analysis:\n{profit_loss_analysis}\n"

    # Write the summary report
    write_to_summary_report(summary_content)

if __name__ == "__main__":
    main()
