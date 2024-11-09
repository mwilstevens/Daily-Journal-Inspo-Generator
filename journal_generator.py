from datetime import datetime, timedelta

# Set the starting date to the current date when the script is run
start_date = datetime.today()

# Load writing prompts from the file
with open('365_daily_prompts.txt', 'r') as file:
    writing_prompts = file.readlines()

# Ensure we have exactly 365 prompts for the year
if len(writing_prompts) < 365:
    raise ValueError("The '365_daily_prompts.txt' file should contain 365 unique writing prompts.")

# Define the journal template with a placeholder for the unique prompt
journal_template = """
\\rtf1\\ansi\\deff0
{{\\b Date:}} {date} \\line

\\b Morning Plan \\par
\\b Ritual \\par
"When you're ready, close your eyes and take 3 deep breaths. Ok... but now actually do it." \\par

\\b Dump \\par
List all the tasks you have to do today: \\line
- Task 1 \\line
- Task 2 \\line
- Task 3 \\line
- Task 4 \\line
- Task 5 \\line
- Task 6 \\line
- Task 7 \\line
- Task 8 \\line

\\b Prioritize \\par
Choose the most important tasks for the day: \\line
- Top priority \\line
- Important/urgent \\line
- Important/urgent \\line
- Small task \\line
- Small task \\line
- Small task \\line
- Small task \\line

\\b Time Box \\par
Take a minute to schedule the top priority task into your day.
Time boxing is a proven method of "making an appointment with your task." \\par

\\b Self-Care \\par
What is one small thing you're going to do for yourself today? \\par

\\b Closing \\par
What is your mantra or something to keep in mind today? \\par

Now Go Own Your Day. \\par

\\b Creative Writing Prompt \\par
Write for at least 10 minutes about the following: \\par
"{writing_prompt}" \\par

\\b Evening Reflection \\par

\\b Thoughts from the Day \\par
What stuck with you today? Any conversations, new ideas, or observations? \\par

\\b Mindfulness \\par
Share three things you're grateful for: \\line
- Example: A moment of peace \\line
- Example: A good laugh with a friend \\line
- Example: A productive meeting \\line

One thing you're proud of: \\par
Example: Completing a challenging task at work. \\par

One thing you'd like to do differently in the future: \\par
Example: Be more present during meals. \\par

\\b Inspiration \\par
What inspired you today? It can be a quote, a photo, an article, or anything else! \\par
Example: "Success is not final, failure is not fatal: It is the courage to continue that counts." – Winston Churchill \\par
"""

# Loop to create 365 daily journal files
for i in range(365):
    # Calculate the date for each entry
    current_date = start_date + timedelta(days=i)
    # Format date in MM.DD.YY for file naming
    file_name = current_date.strftime("%m.%d.%y") + " Journal.rtf"
    # Format date for inside the journal entry
    formatted_date = current_date.strftime("%B %d, %Y")
    # Get the unique writing prompt for the day, stripping newline characters
    writing_prompt = writing_prompts[i].strip()
    # Populate the template with the formatted date and unique prompt
    journal_content = journal_template.format(date=formatted_date, writing_prompt=writing_prompt)
    
    # Write the content to an RTF file
    with open(file_name, 'w') as file:
        file.write(journal_content)

print("365 RTF journal files with unique writing prompts have been created successfully.")
