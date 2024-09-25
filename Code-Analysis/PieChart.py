import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# Load the data from Excel file
excel_file = r"C:\Users\SukmaAI\Downloads\Trial_survey.xlsx"  # Replace with your actual file path
df = pd.read_excel(excel_file, sheet_name='Sheet1')  # Make sure you specify the correct sheet name

# Assume the column containing the data is named 'Greenery'
df['Greenery'] = df['Greenery'].str.split(';') #Make sure the Column name is similar with excel file

# Split and normalize the data
greenery_types = df['Greenery'].explode()

# Count occurrences of each greenery type
greenery_counts = greenery_types.value_counts()

# Plot the pie chart
plt.figure(figsize=(8, 6))
plt.pie(greenery_counts, labels=greenery_counts.index, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99','#ffcc99','#ff9999'])
plt.title('Preferred Greenery')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular


# Save the plot to an HTML file
html_str = mpld3.fig_to_html(plt.gcf())
with open("/mnt/data/preferred_greenery_chart.html", "w") as f:
    f.write(html_str)

plt.show()
