from bs4 import BeautifulSoup
import requests


# def check_broken_links(url):
#     response = requests.get(url)
#     response = requests.get(url)
#     print(f"Status Code: {response.status_code}")
#     print(f"Response Headers: {response.headers}")
#     soup = BeautifulSoup(response.text, 'html.parser')

#     links = [a["href"] for a in soup.find_all("a", href=True)]
    
#     for link in links:
#         try:
#             res = requests.get(link)
#             if res.status_code != 200:
#                 print(f"Broken link found: {link} (Status: {res.status_code})")
#         except requests.exceptions.RequestException:
#             print(f"Invalid link: {link}")

# # Example Usage
# check_broken_links("https://www.gabrielny.com/")



# import requests

# url = "https://allenplus.allen.ac.in/"

# response = requests.get(url)

# print(f"Status Code: {response.status_code}")
# print(f"Response Headers: {response.headers}")
# print(f"Response Content (First 500 chars):\n{response.text[:500]}")


import requests
from bs4 import BeautifulSoup

def count_links(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.find_all("a", href=True)  # Find all <a> tags with href attribute
        print(f"Total links found on {url}: {len(links)}")

        return len(links)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

# Example Usage
url = "https://www.gabrielny.com/"  # Replace with the target URL
count_links(url)



from bs4 import BeautifulSoup

def extract_api_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return [a["href"] for a in soup.find_all("a", href=True) if "api" in a["href"]]

url="https://www.gabrielny.com/"
extract_api_links(url)
print("last line")


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def extract_api_links(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract API links from <a> tags
        api_links = [urljoin(url, a["href"]) for a in soup.find_all("a", href=True) if "api" in a["href"].lower()]

        # Extract API links from JavaScript <script> tags
        scripts = soup.find_all("script")
        for script in scripts:
            if script.string:
                found_links = re.findall(r'https?://[^\s"\'<>]+', script.string)  # Regex to find URLs
                api_links.extend([link for link in found_links if "api" in link.lower()])

        # Remove duplicates
        api_links = list(set(api_links))

        # Print all extracted API URLs
        if api_links:
            print("\nExtracted API URLs:")
            for link in api_links:
                print(link)
        else:
            print("No API links found.")

        return api_links

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return []

# Example Usage
website_url = "https://allenplus.allen.ac.in/"  # Replace with actual site URL
extract_api_links(website_url)


