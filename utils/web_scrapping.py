import requests
from bs4 import BeautifulSoup

def get_content_from(url):
    try:
        # Making a GET request to the URL
        r = requests.get(url)

        # Check if the request was successful (status code 200)
        if r.status_code == 200:
            # Parsing the HTML content of the webpage
            soup = BeautifulSoup(r.content, 'html.parser')

            # Finding the div with class 'entry-content' that typically holds the main content
            content_div = soup.find('div', class_='entry-content')

            if content_div:
                # Extracting all paragraphs within the content_div
                paragraphs = content_div.find_all('p')

                # Joining paragraphs into a single string
                content_text = '\n'.join([p.get_text(strip=True) for p in paragraphs])

                return content_text
            else:
                return "Content not found on the webpage."

        else:
            return f"Failed to retrieve content. Status code: {r.status_code}"

    except Exception as e:
        return f"An error occurred: {str(e)}"