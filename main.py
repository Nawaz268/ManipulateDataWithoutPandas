import csv
from typing import List
import matplotlib.pyplot as plt


def read_csv(filename: str) -> List[List[str]]:
    pop = None
    with open(filename, "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        pop = [row for row in csv_reader]
    return pop


def col_to_int(myList: list) -> List[List[str]]:
    # Skipping 0 as it is headers
    for row in range(1, len(myList)):
        for column in range(1, len(myList[row])):
            myList[row][column] = int(myList[row][column])
    return myList


def highestLowestProjPop(pop: list) -> List[List[str]]:
    pop_exp_dev = []

    for row in range(0, len(pop)):
        pop_exp_dev.append([])
        pop_exp_dev[row].append(pop[row][0])

    for row in range(1, len(pop)):
        lowest = min(pop[row][1:])
        lowest_index = pop[row].index(lowest)
        lowest_year = pop[0][lowest_index]

        highest = max(pop[row][1:])
        highest_index = pop[row].index(highest)
        highest_year = pop[0][highest_index]

        pop_exp_dev[row].append(lowest)
        pop_exp_dev[row].append(lowest_year)
        pop_exp_dev[row].append(highest)
        pop_exp_dev[row].append(highest_year)

        # add relative change in population 2020-2100
        dev = round((pop[row][-1] - pop[row][1]) / pop[row][1] * 100, 2)

        pop_exp_dev[row].append(dev)

    col_names = [
        "country",
        "lowest_pop",
        "lowest_pop_year",
        "highest_pop",
        "highest_pop_year",
        "rel_change_2020-2100",
    ]
    pop_exp_dev[0] = col_names

    return pop_exp_dev

def sorted_list(pop: list, index: int) -> List[List[str]]:
    pop_dev_sorted = sorted(pop[1:], reverse=True, key=lambda x:x[index])
    return pop_dev_sorted

def insert_rows_ranged(pop:list, output:list, start:int = None, end:int = None) -> List[List[str]]:
    for row in pop[start:end]:
        output.append(row)
    return output

def drawPlot(pop:list, xaxis_index:int, yaxis_index:int):
    countries = []
    rel_change = []
    for row in range(1, len(pop)):
        countries.append(pop[row][xaxis_index])
        rel_change.append(pop[row][yaxis_index])
    plt.grid()
    plt.barh(countries, rel_change)
    plt.title('World Population Projection 2019 - 2100.\nCountries with Largest Growth and Decline Respectively')
    plt.xlabel('Change factor in percent')
    plt.show()  



def main():
    pop = read_csv("pop_subset.csv")
    pop = col_to_int(pop)
    new_pop = highestLowestProjPop(pop)
    sorted_pop = sorted_list(new_pop,5)

    growth_list = []
    growth_list = insert_rows_ranged(sorted_pop, growth_list, start= None, end = 11)
    growth_list = insert_rows_ranged(sorted_pop, growth_list, start= -10, end =None)
    #drawPlot(pop=growth_list, xaxis_index=0, yaxis_index=-1)

    #draw only for european nations
    europe = ['Russia', 'Germany', 'United Kingdom', 'France', 'Italy', 'Spain', 'Ukraine', 'Poland', 'Romania', 'Netherlands', 
          'Belgium', 'Czech Republic', 'Greece', 'Portugal', 'Sweden', 'Hungary', 'Belarus', 'Austria', 'Serbia', 
          'Switzerland', 'Bulgaria', 'Denmark', 'Finland', 'Slovak Republic','Norway', 'Ireland', 'Croatia', 'Moldova', 
          'Bosnia and Herzegovina', 'Albania',	'Lithuania','Macedonia, FYR', 'Slovenia', 'Latvia', 'Kosovo', 'Estonia', 
          'Montenegro', 'Luxembourg', 'Malta', 'Iceland', 'Andorra', 'Monaco', 'Liechtenstein', 'San Marino', 'Holy See']
    
    europe_list = []
    for row in range(1, len(sorted_pop)):
        if sorted_pop[row][0] in europe:
            europe_list.append(sorted_pop[row])
    
    europe_list_srt = sorted_list(europe_list,5)
    print(europe_list)
    #drawPlot(pop=europe_list_srt, xaxis_index=0, yaxis_index=-1)

    # standardize the pop list, use 2020 as index year

    # create new empty list to store new values
    pop_norm = []

    # add country
    for row in range(len(europe_list_srt)):
        pop_norm.append([])
        pop_norm[row].append(europe_list_srt[row][0])
        print(pop_norm)

    # add normalized values for each year, use 2020 as index year
    for row in range(1,len(europe_list_srt)):
        for column in range(1, len(europe_list_srt[row])):
            """print(type(europe_list_srt[row][column]))
            print(europe_list_srt[row][column])
            print("\n")
            print(type(europe_list_srt[row][1]*100))
            print(europe_list_srt[row][1]*100)"""
            #pop_norm[row].append(round(europe_list_srt[row][column]/europe_list_srt[row][1]*100, 2))

    # add column names
    cols = ['COUNTRIES', '2019', '2020', '2025', '2030', '2035', '2040', '2045', '2050', '2055', '2060', '2065', '2070', '2075', '2080', '2085', '2090', '2095', '2100']
    pop_norm.insert(0, cols)

    # print first 5 rows
    for row in pop_norm[:5]:
        print(row)




if __name__ == "__main__":
    main()
    # Prints in 2D prettified
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))