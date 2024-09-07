from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('mobile.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with the specified class and data-tkid
divs = soup.find_all('div', class_='tUxRFH', attrs={'data-tkid': 'en_DpZ-b-GB4PGkozr5CmmsyLzWdxeKTtV0gGe2KMYIYbqN9ZXHLP3qN6C0Y8W47UzYFaq5Tzib0zLV4t4M08SzMw=='})

# Prepare a list to hold the extracted data
data = []

for div in divs:
    # Initialize variables
    product_name = ""
    price = ""
    rating = ""
    details = ""

    # Extract product_name
    product_div = div.find('div', class_='KzDlHZ')
    if product_div:
        product_name = product_div.text.strip()

    # Extract price
    price_div = div.find('div', class_='Nx9bqj _4b5DiR')
    if price_div:
        price = price_div.text.strip()

    # Extract rating
    rating_div = div.find('div', class_='XQDdHH')
    if rating_div:
        rating = rating_div.text.strip()

    # Extract details
    details_div = div.find('div', class_='_6NESgJ')
    if details_div:
        details = details_div.text.strip()

    # Append the extracted data to the list
    data.append([product_name, price, rating, details])

# Write the data to a CSV file
with open('mobile_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Product Name', 'Price', 'Rating', 'Details'])
    csvwriter.writerows(data)

