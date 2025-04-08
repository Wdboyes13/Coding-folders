import requests
from bs4 import BeautifulSoup

# URL of the CBC Poll Tracker
url = "https://newsinteractives.cbc.ca/elections/poll-tracker/canada/"
headers = {"User-Agent": "Mozilla/5.0"}

# Get the HTML response
response = requests.get(url, headers=headers)

# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Print the first part of the page to understand the structure (debugging step)
print(soup.prettify()[:1000])  # Preview the first 1000 characters

# Find the parent div (which is correct, according to your example)
parent_div = soup.find("div", class_="MuiBox-root css-52sq9")

if parent_div:
    # Now find the child div(s) containing the poll data
    poll_data = parent_div.find_all("div", class_="css-10avd87")  # Update class as necessary

    if poll_data:
        # Write the children content (poll data) to a file
        with open("output.html", "w", encoding="utf-8") as file:
            for child in poll_data:
                file.write(str(child))  # Write each child element to the file
        print("Poll data saved to output.html")
    else:
        print("No poll data found within the parent div.")
else:
    print("Parent div not found.")
