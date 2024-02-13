import requests
from bs4 import BeautifulSoup

def scrape_odds(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Function to check if the title starts with "Compare odds for"
    def has_compare_odds_title(tag):
        return tag.has_attr('title') and tag['title'].startswith("Compare odds for")

    # Find all <a> tags with the specified style and title
    odds_elements = soup.find_all(has_compare_odds_title, style="color: navy")

    odds_data = []

    # Loop through each element to extract the odds information
    for element in odds_elements:
        # Extract the text containing odds information
        odds_text = element.get_text(strip=True)
        
        # Split the text to separate the matchup from the odds
        _, odds = odds_text.split('\n')
        
        # Further split the odds to separate the individual odds and the percentage
        odds1, odds2, percentage = odds.split(' - ')[0], odds.split(' - ')[1].split(' ')[0], odds.split(' ')[1].strip('()')
        
        odds_data.append((odds1, odds2, percentage))

    return odds_data



# URL of the webpage to scrape
url = "https://www.sportspunter.com.au/sports-betting/"
odds_data = scrape_odds(url)