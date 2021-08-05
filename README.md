# AO3 Scraper 
Simple web scraper to scrape info on works off Archive Of Our Own. 

## How to use
Run `python3 get-fics.py [number of pages] [fandom/primary tag] [sorting method]`

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

Run `python3 analyse-fics.py`

This will generate a graph based on the data saved in `results.csv` which can be accessed at `fig.png` or loaded with `index.html`

## To-do
Allow more options in graph generation - right now I hard-code that it generates the top 10 fandoms in the primary tag.

Create an interface so that fan statisticians can easily use this to generate what graphs they'd like instead of relying on hardcoding.

## Example usage

Run `python3 get-fics.py 5 "Alternate Universe - College" kudos_count`

Run `python3 analyse-fics.py`

This produces the frequency of the top 10 fandoms in "Alternate Universe - College", from the top 100 fics sorted by kudos. 
![Example graph](examples/example.png)

## Note

If you know how many pages of results there are you can put that in in order to scrape all possible search results of your query (or put in an impossibly high number - the script will detect if no fics are left), which will produce more accurate results. Note that this will take a while to scrape though due to the delay per page.