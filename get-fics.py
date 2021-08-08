import requests
import argparse 
from bs4 import BeautifulSoup
from time import sleep
import csv

# Let user input parameters of search
parser = argparse.ArgumentParser(description="List the filters of your AO3 search")
parser.add_argument("--num_pages", default="-1", type=int, help="The number of pages") # defaults to all search results
parser.add_argument("fandom", type=str, help="The fandom (please use a valid AO3 fandom tag)")
parser.add_argument("--sort", default="revised_at", type=str, help="How do you wish to sort your results?") # defaults to date updated

valid_sort = ["authors_to_sort_on", "title_to_sort_on", "created_at", "revised_at", "word_count", "hits", 
    "kudos_count", "comments_count", "bookmarks_count"]

args = parser.parse_args()

num_pages = args.num_pages
fandom = args.fandom
sort = args.sort

if sort not in valid_sort:
    print("Please enter a valid sorting method.")
    exit(1)
if num_pages < 0 and num_pages != -1:
    print("Please enter a valid number of pages of works to scrape.")
    exit(1)

with open("results.csv", "w", encoding="utf-8") as f:

    writer = csv.writer(f)

    header = ["Title", "Author", "Fandoms", "Content Rating", "Relationship Type", "Content Warning", "Work Status",
        "Date Updated", "Relationship Tags", "Character Tags", "Freeform Tags", "Summary", "Language", "Word Count",
        "Chapters", "Comments", "Kudos", "Bookmarks", "Hits"]
    writer.writerow(header)

    # For the number of pages we want to look at
    pages_so_far = 0
    while True:
        if num_pages != -1 and pages_so_far == num_pages:
            print(num_pages)
            print(pages_so_far)
            break

        page = pages_so_far + 1

        # this ugly ass url lets me make more specific searches
        url = ("https://archiveofourown.org/tags/"+ fandom + "/works?commit=Sort+and+Filter&page="
        + str(page) + "&utf8=%E2%9C%93&work_search%5Bcomplete%5D=&work_search" +
        "%5Bcrossover%5D=&work_search%5Bdate_from%5D=&work_search%5Bdate_to%5D=&work_search%5B"+
        "excluded_tag_names%5D=&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D"+
        "=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D="+ sort + 
        "&work_search%5Bwords_from%5D=&work_search%5Bwords_to%5D=")
        
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser') # r.content gives us html of the webpage
        
        works = soup.select("li.work.blurb.group") # creates list of all works on the page

        # check if we've input too many pages and there's no more fic
        if len(works) == 0:
            break
        
        # iterate through the list of works and print to terminal (maybe make this a webpage in future)
        for work in works:

            row = []

            title = work.select_one(".heading a").text.strip()
            row.append(title) 
            
            author = work.select_one(".heading a[rel=author]").text.strip() # i'm just taking the first author - rip multiple authors but it's not important for my analysis yet
            row.append(author) 
            
            fandoms = work.select(".fandoms.heading a") # multiple fandoms
            fandoms_list = []
            for f in fandoms:
                fandoms_list.append(f.text.strip())
            fandoms_str = "$".join(fandoms_list) # $ is unlikely to show up in an ao3 tag so using it as separator
            row.append(fandoms_str)
            
            reqd_tags = work.select(".required-tags span span")
            reqd_tags_list = []
            for r in reqd_tags:
                reqd_tags_list.append(r.text.strip())

            row.append(reqd_tags_list[0]) # content rating

            rel_type = reqd_tags_list[1].split(", ") # relationship type
            rel_type_str = "$".join(rel_type)
            row.append(rel_type_str)

            cw = reqd_tags_list[2].split(", ") # content warnings
            cw_str = "$".join(cw)
            row.append(cw_str)

            row.append(reqd_tags_list[3]) # work status
            
            date_updated = work.select_one(".datetime").text.strip()
            row.append(date_updated)
            
            relationships = work.select(".relationships")
            rel_list = []
            for rel in relationships:
                rel_list.append(rel.text.strip())
            rel_str = "$".join(rel_list)
            row.append(rel_str)
            
            characters = work.select(".characters")
            char_list = []
            for char in characters:
                char_list.append(char.text.strip())
            char_str = "$".join(char_list)
            row.append(char_str)

            freeforms = work.select(".freeforms")
            free_list = []
            for free in freeforms:
                free_list.append(free.text.strip())
            free_str = "$".join(free_list)
            row.append(free_str)

            summary = work.select_one(".userstuff.summary")
            if summary is None:
                summary = ""
            else:
                summary = summary.text.strip()
            row.append(summary)

            lang = work.select_one("dd.language").text.strip()
            row.append(lang) 
            
            word_count = work.select_one("dd.words").text.strip()
            row.append(word_count)

            chapters = work.select_one("dd.chapters a") # if this doesn't exist, it's dd.chapters and a one shot
            if chapters is None:
                chapters = 1
            else:
                chapters = chapters.text.strip()
            row.append(chapters)

            # possible to have zero comments/kudos/bookmarks/hits
            comments = work.select_one("dd.comments a")
            if comments is None:
                comments = 0
            else:
                comments = comments.text.strip()
            row.append(comments)

            kudos = work.select_one("dd.kudos a")
            if kudos is None:
                kudos = 0
            else:
                kudos = kudos.text.strip()
            row.append(kudos)

            bookmarks = work.select_one("dd.bookmarks a")
            if bookmarks is None:
                bookmarks = 0
            else:
                bookmarks = bookmarks.text.strip()
            row.append(bookmarks)

            hits = work.select_one("dd.hits")
            if hits is None:
                hits = 0
            else:
                hits = hits.text.strip()
            row.append(hits)

            writer.writerow(row)

        sleep(5) # to fit with ao3 guidelines

        pages_so_far += 1
