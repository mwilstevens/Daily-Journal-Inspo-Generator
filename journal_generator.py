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
{{\\rtf1\\ansi\\deff0
{{\\fonttbl{{\\f0 Courier;}}}}
\\f0
\\b Date: {date} \\b0

\\b Morning Plan \\b0
\\ul Ritual \\ul0
\\"When you're ready, close your eyes and take 3 deep breaths. Ok... but now actually do it.\\"

\\b Dump \\b0
List all the tasks you have to do today:
\\line - [ ] 
\\line - [ ] 
\\line - [ ] 
\\line - [ ] 
\\line - [ ] 
\\line - [ ] 
\\line - [ ] 
\\line - [ ] 

\\b Prioritize \\b0
Choose the most important tasks for the day:
\\line - [ ] Top priority
\\line - [ ] Important/urgent
\\line - [ ] Important/urgent
\\line - [ ] Small task
\\line - [ ] Small task
\\line - [ ] Small task
\\line - [ ] Small task

\\ul Self-Care \\ul0
What is one small thing you're going to do for yourself today?

\\ul Closing \\ul0
What is your mantra or something to keep in mind today?

\\b Creative Writing Prompt \\b0
Write for at least 10 minutes about the following:
\\"{writing_prompt}\\" 

\\b Evening Reflection \\b0

\\ul Thoughts from the Day \\ul0
What stuck with you today? Any conversations, new ideas, or observations?

\\ul Mindfulness \\ul0
Share three things you're grateful for:

One thing you're proud of:

One thing you'd like to do differently in the future:


\\ul Inspiration \\ul0
What inspired you today? It can be a quote, a photo, an article, or anything else!
}}

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
    
    # Write the content to a .rtf file
    with open(file_name, 'w') as file:
        file.write(journal_content)

print("365 RTF journal files with unique writing prompts have been created successfully.")
