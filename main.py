import csv
from typing import List

def read_csv(filename:str)->List[List[str]]:
    pop = None
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        pop = [row for row in csv_reader]
    return pop

def col_to_int(myList:list) -> List[List[str]]:
    #Skipping 0 as it is headers
    for row in range(1,len(myList)):
        for column in range(1,len(myList[row])):
          myList[row][column] = int(myList[row][column])
    return myList

def highestLowestProjPop(pop:list):
    pop_exp_dev = []

    for row in range(0, len(pop)):
        pop_exp_dev.append([])
        pop_exp_dev[row].append(pop[row][0])

    

    col_names = ['country', 'lowest_pop', 'lowest_pop_year', 'highest_pop', 'highest_pop_year', 'rel_change_2020-2100']
    pop_exp_dev[0] = col_names

    for row in range(4,5):
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
        dev = round((pop[row][-1]-pop[row][1])/pop[row][1]*100, 2)

        pop_exp_dev[row].append(dev)
    return pop_exp_dev

def main():
    pop = read_csv('pop_subset.csv')
    pop = col_to_int(pop)
    print(pop[0])
    print(pop[4])
    x = highestLowestProjPop(pop)
    print(type(x))
    print(x[0])
    print(x[4])

    



    
if __name__ == "__main__":
    main()