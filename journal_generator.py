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
Date: {date}

Morning Plan
Ritual
"When you're ready, close your eyes and take 3 deep breaths. Ok... but now actually do it."

Dump
List all the tasks you have to do today:
- Task 1
- Task 2
- Task 3
- Task 4
- Task 5
- Task 6
- Task 7
- Task 8

Prioritize
Choose the most important tasks for the day:
- Top priority
- Important/urgent
- Important/urgent
- Small task
- Small task
- Small task
- Small task

Time Box
Take a minute to schedule the top priority task into your day.
Time boxing is a proven method of "making an appointment with your task."

Self-Care
What is one small thing you're going to do for yourself today?

Closing
What is your mantra or something to keep in mind today?

Now Go Own Your Day.

Creative Writing Prompt
Write for at least 10 minutes about the following:
"{writing_prompt}"

Evening Reflection

Thoughts from the Day
What stuck with you today? Any conversations, new ideas, or observations?

Mindfulness
Share three things you're grateful for:
- Example: A moment of peace
- Example: A good laugh with a friend
- Example: A productive meeting

One thing you're proud of:
Example: Completing a challenging task at work.

One thing you'd like to do differently in the future:
Example: Be more present during meals.

Inspiration
What inspired you today? It can be a quote, a photo, an article, or anything else!
Example: "Success is not final, failure is not fatal: It is the courage to continue that counts." – Winston Churchill
"""

# Loop to create 365 daily journal files
for i in range(365):
    # Calculate the date for each entry
    current_date = start_date + timedelta(days=i)
    # Format date in MM.DD.YY for file naming
    file_name = current_date.strftime("%m.%d.%y") + " Journal.txt"
    # Format date for inside the journal entry
    formatted_date = current_date.strftime("%B %d, %Y")
    # Get the unique writing prompt for the day, stripping newline characters
    writing_prompt = writing_prompts[i].strip()
    # Populate the template with the formatted date and unique prompt
    journal_content = journal_template.format(date=formatted_date, writing_prompt=writing_prompt)
    
    # Write the content to a .txt file
    with open(file_name, 'w') as file:
        file.write(journal_content)

print("365 TXT journal files with unique writing prompts have been created successfully.")
