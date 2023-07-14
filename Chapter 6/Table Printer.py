import pandas as pd

def printTable(list):
    colWidths = [0] * len(list)
    justifiedList = []
    # Finding max length of each column
    for index,sublist in enumerate(list):
        colWidths[index] = len(sorted(sublist,reverse=True,key=len)[0])
    
    # Justifying each word and putting it back into list of lists
    for indexSub,sublist in enumerate(list):
        justifiedList.append([])
        for i in range(len(sublist)):
            justifiedList[indexSub].append(str(sublist[i]).rjust(colWidths[indexSub]))

    # Creating a table using pandas.. but honestly that removes the need to justify in the first place! 
    # So it's probably not what the author meant.
    df = pd.DataFrame(justifiedList)
    df = df.transpose().to_string(index=False,header=False)
    return(df)


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print(printTable(tableData))