import matplotlib.pyplot as plt 
import csv 

FANDOM_COL = 2

with open("results.csv", "r") as f:
    plots = csv.reader(f, delimiter=",")
    
    # Get most popular fandoms
    fandoms = {}
    for row in plots: 
        fandom_list = row[FANDOM_COL].split("$")
        for fandom in fandom_list:
            if fandom not in fandoms:
                fandoms[fandom] = 1
            else:
                fandoms[fandom] += 1

    fandoms = dict(sorted(fandoms.items(), key=lambda item: item[1], reverse=True))
    
    # can't have too many fandoms otherwise the graph is unreadable
    if len(fandoms) > 10:
        fandoms = dict(list(fandoms.items())[:10]) 

    print(fandoms)

    x = []
    for i in range(len(fandoms)):
        x.append(i+1)
    print(x)

    values = [int(v) for v in fandoms.values()]

    # the fandom names can be quite long
    keys = list(fandoms.keys())
    for k in range(len(keys)):
        c = ""
        for char in range(len(keys[k])):
            if char % 10 == 0 and char is not 0:
                # print(char)
                c += "\n"
            c += keys[k][char]

        keys[k] = c 
    print(keys)

    plt.bar(x, values, tick_label = keys)
    plt.xticks(fontsize=8, rotation=90)
    plt.xlabel('Fandom')
    plt.ylabel('Frequency')
    plt.title("Top 10 Fandoms in 'Alternate Universe - College'")
    plt.show()

    plt.tight_layout()

    plt.savefig("fig.png")

    # Get most popular relationships

    # Get most popular characters

    # Get most popular freeform tags (e.g. AUs, tropes)