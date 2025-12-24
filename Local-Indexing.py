"""
Local Web Indexing Script
==========================
This script crawls a given website and discovers all internal links.
It performs a breadth-first search through the website's pages.

Author: LocalWebIndex Project
Purpose: Web crawling and URL discovery for local/internal website indexing
"""

import requests  # Import the requests library for making HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing
from urllib.parse import urlparse, urljoin  # Import urlparse and urljoin for URL manipulation
import certifi  # Import certifi for SSL certificate handling
import warnings  # Import warnings module to suppress warnings
import urllib3  # Import urllib3 for HTTP connection pooling
from urllib3.exceptions import InsecureRequestWarning  # Import InsecureRequestWarning for SSL warnings suppression

def crawl_website(url):
    """
    Crawls a website starting from the given URL and discovers all internal links.
    
    Uses a breadth-first search algorithm to traverse the website:
    1. Starts with the initial URL in a queue
    2. Processes each URL from the queue
    3. Extracts all links from each page
    4. Adds internal links to the queue for further crawling
    
    Args:
        url (str): The starting URL to begin crawling from
        
    Returns:
        set: A set of all discovered and visited URLs
        
    Note:
        - SSL verification is disabled (verify=False) for crawling sites with self-signed certificates
        - Only internal links (same domain) are followed
        - Duplicate URLs are automatically skipped using a set
    """
    visited_urls = set()  # Initialize a set to store visited URLs (prevents duplicates)
    queue = [url]  # Initialize a queue with the starting URL (FIFO for breadth-first search)
    
    # Continue crawling while there are URLs in the queue
    while queue:
        current_url = queue.pop(0)  # Get the next URL from the queue (dequeue first item)
        
        # Skip if URL has already been visited (avoid infinite loops and redundant work)
        if current_url in visited_urls:
            continue
        
        try:            
            # Suppress InsecureRequestWarning to avoid cluttering output when verify=False
            urllib3.disable_warnings(InsecureRequestWarning)
            
            # Send a GET request to the current URL and retrieve the response
            # verify=False disables SSL certificate verification (use with caution)
            response = requests.get(current_url, verify=False)

            # Check if the response is successful (HTTP status code 200)
            if response.status_code == 200:
                visited_urls.add(current_url)  # Mark this URL as visited
                
                # Parse the HTML content of the response using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find all <a> (anchor) elements with href attribute
                for link in soup.find_all('a', href=True):
                    # Construct the absolute URL of the next page
                    # urljoin handles relative URLs and combines them with the base URL
                    next_url = urljoin(current_url, link['href'])
                    
                    # Check if the next URL is internal (same domain as starting URL)
                    if is_internal_url(url, next_url):
                        queue.append(next_url)  # Add the next URL to the queue for crawling
                        
        except Exception as e:
            # Catch any exceptions during crawling (network errors, parsing errors, etc.)
            print(f"Error crawling {current_url}: {str(e)}")

    return visited_urls  # Return the complete set of visited URLs

def is_internal_url(base_url, url):
    """
    Determines if a URL is internal (same domain) compared to the base URL.
    
    Internal URLs are those that belong to the same domain as the base URL.
    This ensures the crawler doesn't follow external links to other websites.
    
    Args:
        base_url (str): The original/starting URL of the website
        url (str): The URL to check if it's internal
        
    Returns:
        bool: True if the URL is internal (same domain), False otherwise
        
    Examples:
        >>> is_internal_url("https://example.com/page1", "https://example.com/page2")
        True
        >>> is_internal_url("https://example.com/page1", "https://other-site.com/page")
        False
    """
    base_domain = urlparse(base_url).netloc  # Extract the domain from the base URL
    next_domain = urlparse(url).netloc  # Extract the domain from the URL to check
    return base_domain == next_domain  # Return True if both URLs have the same domain

if __name__ == "__main__":
    """
    Main entry point of the script.
    
    Execution flow:
    1. Prompts user for a website URL
    2. Calls the crawl_website function to discover all internal links
    3. Prints all discovered URLs to the console
    """
    # Prompt the user to insert a URL
    website_url = input("Please enter the URL: ")
    
    # Call the crawl_website function with the provided URL
    discovered_urls = crawl_website(website_url)
    
    # Print all discovered URLs
    print(f"\nDiscovered {len(discovered_urls)} URLs:")
    print("-" * 50)
    for url in discovered_urls:
        print(url)
