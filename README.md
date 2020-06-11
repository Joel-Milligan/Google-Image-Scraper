# Google-Image-Scraper
Scrapes and saves a certain number of google images returned from a specific search term.

## Instructions:
Call the script with: 
1. $ python scraper.py search_term1 search_term2 #_results
2. $ python scraper.py search_term1 search_term2 (default number = 10)
3. $ python scraper.py

Default arguments if missing values:
- search_term = "cat"
- #_results = 10

Saves the image results in a file called "#-images-of-search_term-v1"

Version number changes if there is already a folder called "#-images-of-search_term-v1"