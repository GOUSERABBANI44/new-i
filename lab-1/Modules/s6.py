# Importing the datetime module
from datetime import datetime

# Retrieving the current date and time
current_datetime = datetime.now()

# Formatting the date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Displaying the result
print(f"Current date and time: {formatted_datetime}")
