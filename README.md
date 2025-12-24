# Local Web Indexing

A Python web crawler script that discovers and indexes all internal links within a target website. This tool performs a breadth-first search traversal of web pages, making it useful for site mapping, link discovery, and content auditing.

## Overview

This script crawls a website starting from a given URL and discovers all internal pages by following links. It respects domain boundaries, only following links that belong to the same domain as the starting URL.

## Features

- **Breadth-First Crawling**: Systematically explores the website level by level
- **Internal Link Detection**: Only follows links within the same domain
- **Duplicate Prevention**: Automatically skips already-visited URLs
- **SSL Support**: Handles SSL certificates (including self-signed certificates)
- **Error Handling**: Gracefully handles network errors and parsing issues
- **Simple Output**: Lists all discovered URLs to the console

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

### For Windows, macOS, and Linux:

Install the required Python packages using pip:

```bash
pip install requests
pip install beautifulsoup4
pip install certifi
```

Or install all dependencies at once:

```bash
pip install requests beautifulsoup4 certifi
```

## Usage

1. Run the script:
   ```bash
   python Local-Indexing.py
   ```

2. When prompted, enter the URL of the website you want to crawl:
   ```
   Please enter the URL: https://example.com
   ```

3. The script will crawl the website and display all discovered URLs:
   ```
   Discovered 15 URLs:
   --------------------------------------------------
   https://example.com
   https://example.com/about
   https://example.com/contact
   ...
   ```

## How It Works

1. **Initialization**: The script starts with the URL you provide
2. **Queue Processing**: URLs are processed in a first-in-first-out (FIFO) order
3. **Page Fetching**: Each page is fetched using HTTP GET requests
4. **Link Extraction**: All links (`<a>` tags) are extracted from the HTML
5. **Domain Filtering**: Only links with the same domain are added to the queue
6. **Deduplication**: Already-visited URLs are skipped automatically
7. **Output**: All discovered URLs are printed at the end

## Technical Details

### Dependencies

- **requests**: For making HTTP requests to web pages
- **beautifulsoup4**: For parsing HTML and extracting links
- **certifi**: For SSL certificate verification
- **urllib3**: For HTTP connection pooling and SSL warning suppression

### Algorithm

The script uses a breadth-first search (BFS) algorithm:
- Maintains a queue of URLs to visit
- Maintains a set of visited URLs to prevent duplicates
- Processes URLs level by level across the website hierarchy

### Security Note

⚠️ **WARNING**: The script disables SSL certificate verification (`verify=False`) to allow crawling of websites with self-signed certificates. 

**Important Security Considerations:**
- This makes the connection vulnerable to man-in-the-middle (MITM) attacks
- Only use this feature on trusted networks and websites you control
- For production use, enable SSL verification by setting `verify=True` in the code
- This feature is primarily intended for local development and testing environments

**Recommended Usage:**
- ✅ Local development websites with self-signed certificates
- ✅ Internal company websites on trusted networks
- ❌ Public websites or untrusted sources
- ❌ Production environments without proper SSL certificates

## Limitations

- Only follows internal links (same domain as starting URL)
- Does not handle JavaScript-rendered content
- Does not respect robots.txt
- No rate limiting (may generate many requests quickly)
- Does not save crawled content, only lists URLs

## Use Cases

- **Site Mapping**: Create a complete map of all pages on a website
- **Link Discovery**: Find all accessible pages within a domain
- **Content Auditing**: Identify all pages for content review
- **Testing**: Verify internal link structure
- **Documentation**: Generate a list of all pages for documentation

## Example Output

```
Please enter the URL: https://example.com

Discovered 10 URLs:
--------------------------------------------------
https://example.com
https://example.com/about
https://example.com/services
https://example.com/products
https://example.com/contact
https://example.com/blog
https://example.com/blog/post-1
https://example.com/blog/post-2
https://example.com/privacy
https://example.com/terms
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is open source and available for educational and personal use.

## Troubleshooting

### Common Issues

1. **SSL Certificate Errors**: The script disables SSL verification by default to handle self-signed certificates
2. **Network Timeouts**: Some websites may be slow to respond; the script will print error messages and continue
3. **Too Many URLs**: For large websites, the crawler may discover many URLs; consider adding a limit if needed

## Future Enhancements

Potential improvements for future versions:
- Add depth limit for crawling
- Implement rate limiting
- Add support for robots.txt
- Save results to a file
- Add progress indicator
- Support for JavaScript-rendered content
- Configurable filters for URL patterns
