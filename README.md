# AO3 Scraper 
Simple web scraper to scrape info on works off Archive Of Our Own. 

## How to use
Run `python2 get-fics.py [number of pages] [fandom/primary tag] [sorting method]`

(For sorting method please use one of the following: 
- authors_to_sort_on
- title_to_sort_on
- created_at
- revised_at
- word_count
- hits
- kudos_count
- comments_count
- bookmarks_count)

For fandom/primary tag please use a valid AO3 tag for best results.

Note that there's a 5 second delay for each page that you access to comply with AO3 guidelines.

The results will automatically be saved to `results.csv`

For example, run `python3 get-fics.py 3 Glee kudos_count` to get the first 3 pages of fics in the Glee fandom, sorted by kudos.