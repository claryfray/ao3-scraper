import matplotlib.pyplot as plt 
import csv 
import argparse

parser = argparse.ArgumentParser(description="Type of graph to generate")
parser.add_argument("graph_type", type=str, help="Graph of most popular: fandom, relationship, character, freeform")
args = parser.parse_args()

graph_type = args.graph_type

if graph_type == "fandom":
    FANDOM_COL = 2
elif graph_type == "relationship":
    FANDOM_COL = 5
elif graph_type == "character":
    FANDOM_COL = 6
elif graph_type == "freeform":
    FANDOM_COL = 7
else:
    print("Please input a valid graph type")
    exit(1)

with open("results.csv", "r") as f:
    plots = csv.reader(f, delimiter=",")
    
    # Get most popular of whatever type user wants
    fandoms = {}
    for row in plots: 
        fandom_list = row[FANDOM_COL].split("$")
        for fandom in fandom_list:
            if fandom == "": # Not sure why this is happening but eh
                continue
            if fandom not in fandoms:
                fandoms[fandom] = 1
            else:
                fandoms[fandom] += 1

    fandoms = dict(sorted(fandoms.items(), key=lambda item: item[1], reverse=True))
    
    # can't have too many fandoms/characters/etc otherwise the graph is unreadable
    if len(fandoms) > 10:
        fandoms = dict(list(fandoms.items())[:10]) 
    print(fandoms)

    x = []
    for i in range(len(fandoms)):
        x.append(i+1)

    values = [int(v) for v in fandoms.values()]

    # the names can be quite long
    keys = list(fandoms.keys())
    for k in range(len(keys)):
        c = ""
        for char in range(len(keys[k])):
            if char % 10 == 0 and char != 0:
                c += "\n"
            c += keys[k][char]

        keys[k] = c 

    plt.bar(x, values, tick_label = keys)
    plt.xticks(fontsize=8, rotation=90)
    plt.xlabel(f"{graph_type}")
    plt.ylabel('Frequency')
    plt.show()

    plt.tight_layout()

    plt.savefig("fig.png")
