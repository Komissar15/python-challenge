import os
import csv


budget_csv = os.path.join('PyBank','Resources', 'budget_data.csv')
output_file = "financial_analysis.txt"


total_months = 0
total_amount = 0
changes = []
greatest_increase = {"date": None, "amount": float('-inf')}
greatest_decrease = {"date": None, "amount": float('inf')}

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    previous_value = None

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        total_months += 1
        total_amount += profit_loss

        if previous_value is not None:
            change = profit_loss - previous_value
            changes.append(change)

            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        previous_value = profit_loss

# Calculate the average change
average_change = round(sum(changes) / len(changes), 2)

# Generate the financial analysis report
financial_analysis = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_amount}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the analysis to the terminal
print(financial_analysis)

# Export the analysis to a text file
with open(output_file, "w") as textfile:
    textfile.write(financial_analysis)

print("Financial analysis saved to 'financial_analysis.txt'.")





election_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')
election_output_file = "election_analysis.txt"


total_votes = 0
candidates = {}  # A dictionary to store candidate names as keys and their vote count as values

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)  # Read the CSV header

    for row in csvreader:
        # Assuming candidate names are in the third column (adjust the index if needed)
        candidate_name = row[2]
        total_votes += 1

        # Update the vote count for the candidate
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Determine the winner
winner = max(candidates, key=candidates.get)

# Calculate the percentage of votes each candidate won
percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Generate the election analysis report
election_analysis = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate, votes in candidates.items():
    election_analysis += f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})\n"

election_analysis += "-------------------------\n"
election_analysis += f"Winner: {winner}\n"
election_analysis += "-------------------------\n"

# Print the analysis to the terminal
print(election_analysis)

# Export the analysis to a text file
with open(election_output_file, "w") as textfile:
    textfile.write(election_analysis)

print("Election analysis saved to 'election_analysis.txt'.")
