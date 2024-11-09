# Daily Journal Generator

This project creates 365 RTF journal files, each with a unique writing prompt for daily reflection and creativity. The script begins generating files from a specified start date (currently set to November 8, 2024) and provides a structured format for planning, reflection, and creative writing prompts for each day.

## Files

- **`journal_generator.py`**: The main script that generates the RTF files with daily prompts.
- **`365_daily_prompts.txt`**: A text file containing 365 unique writing prompts, one for each day of the year.

## Features

- **Daily Journal Structure**: Each RTF file includes sections for planning, prioritizing tasks, self-care, and evening reflections.
- **Unique Writing Prompt**: Each day has a creative writing prompt to inspire at least 10 minutes of writing.
- **Automatic Naming**: Files are saved with the format `MM.DD.YY Journal.rtf`, starting from the specified date.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/daily-journal-generator.git
    cd daily-journal-generator
    ```

2. **Ensure the Prompts File is Available**  
   Make sure `365_daily_prompts.txt` is in the same directory as `journal_generator.py`.

## Usage

1. Run the Python script:
    ```bash
    python journal_generator.py
    ```

2. The script will generate 365 `.rtf` files, each with a unique prompt and formatted journal entry.

### Example Output

Each RTF file includes:
- **Morning Planning**: Sections to list tasks, prioritize, schedule, and set intentions for the day.
- **Evening Reflection**: Sections to note gratitude, moments of pride, and insights for personal growth.
- **Creative Writing Prompt**: A unique prompt for daily writing practice.

## Customization

- **Start Date**: Update the `start_date` variable in `journal_generator.py` to change the first date for file generation.
- **Prompts**: Modify `365_daily_prompts.txt` to add your own prompts or replace existing ones.

## License

This project is licensed under the MIT License. See `LICENSE` for more information.

---

Happy journaling!
