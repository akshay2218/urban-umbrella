import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Add a <div> tag around all paragraphs (<p> tags)
    for paragraph in soup.find_all('p'):
        new_div_tag = soup.new_tag('div')
        paragraph.wrap(new_div_tag)

    # Get the modified HTML content
    modified_html = str(soup)

    # Print or use the modified HTML content as needed
    print(modified_html)

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
