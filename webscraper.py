import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.sportspunter.com.au/sports-betting/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Function to check if the title starts with "Compare odds for"
def has_compare_odds_title(tag):
    return tag.has_attr('title') and tag['title'].startswith("Compare odds for")

# Find all <a> tags with the specified style and title
odds_elements = soup.find_all(has_compare_odds_title, style="color: navy")

# Loop through each element to extract the odds information
for element in odds_elements:
    # Extract the text containing odds information
    odds_text = element.get_text(strip=True)
    
    # Split the text to separate the matchup from the odds
    _, odds = odds_text.split('\n')
    
    # Further split the odds to separate the individual odds and the percentage
    odds1, odds2, percentage = odds.split(' - ')[0], odds.split(' - ')[1].split(' ')[0], odds.split(' ')[1].strip('()')
    
    # Print the individual odds and the percentage
    print("Odds 1:", odds1)
    print("Odds 2:", odds2)
    print("Percentage:", percentage)
