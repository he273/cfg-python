import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def read_data():

    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            print(dict(row))
            data.append(row)
    return data


def write_data(data):

    field_names = data[0].keys()
    with open('updated sales.csv', 'w+') as new_sales:
        spreadsheet = csv.DictWriter(new_sales, field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(data)


def collect_sales(data):

    sales_list = []

    for row in data:
        sales_list.append(int(row['sales']))

    return sales_list


def collect_expenditure(data):

    expend_list = []

    for row in data:
        expend_list.append(int(row['expenditure']))

    return expend_list


def main():
    data = read_data()

    # sales calculations

    sales_list = collect_sales(data)
    # print('List of sales: {}'.format(sales_list))

    total_sales = sum(sales_list)
    print('Total sales: {}'.format(total_sales))

    avg_sales = sum(sales_list)/len(sales_list)
    print('Average monthly sales: {}'.format(round(avg_sales, 2)))

    monthly_changes = [round(sales_list[x+1]*100/sales_list[x], 2) for x in range(len(sales_list)-1)]
    print('Percentage monthly changes in sales: {}'.format(monthly_changes))

    highest_sales = max(sales_list)
    best_sales_month = data[sales_list.index(highest_sales)]['month']
    print('The best month for sales was: {} with sales of {}'.format(best_sales_month, highest_sales))

    lowest_sales = min(sales_list)
    worst_sales_month = data[sales_list.index(lowest_sales)]['month']
    print('The worst month for sales was: {} with sales of {}'.format(worst_sales_month, lowest_sales))

    # expenditure calculations

    expend_list = collect_expenditure(data)
    # print('List of expenditures: {}'.format(expend_list))

    total_expenditure = sum(expend_list)
    print('Total expenditure: {}'.format(total_expenditure))

    avg_expenditure = sum(expend_list)/len(expend_list)
    print('Average monthly expenditure: {}'.format(avg_expenditure))

    # profit calculations

    profit_list = [a - b for a, b in zip(sales_list, expend_list)]
    print('List of monthly profit margins: {}'.format(profit_list))

    total_profit = total_sales - total_expenditure
    print('Total profit: {}'.format(total_profit))

    avg_profit = total_profit/len(profit_list)
    print('Average monthly profit: {}'.format(round(avg_profit, 2)))

    # adds a column with the profits to the data and writes it into a new csv file

    for row, month in zip(data, range(len(profit_list))):
        row['profit'] = profit_list[month]
        # print(dict(row))

    write_data(data)

    # writes a file with a summary of some of the calculation results

    with open('sales results.txt', 'w+') as results:
        results.write('2018 Sales Summary\n')
        results.write('\nTotal sales: {}'.format(total_sales))
        results.write('\nTotal expenditure: {}'.format(total_expenditure))
        results.write('\nTotal profit: {}'.format(total_profit))
        results.write('\nThe best month for sales was {} with sales of {}'.format(best_sales_month, highest_sales))
        results.write('\nThe worst month for sales was {} with sales of {}'.format(worst_sales_month, lowest_sales))

    # plots a graph of the monthly sales, expenditure and profits

    sns.set_theme()
    df = pd.read_csv('updated sales.csv')
    df2 = pd.melt(df, id_vars=['year', 'month'])
    # print(df2)
    ax = sns.lineplot(x='month', y='value', hue='variable', style='year', data=df2)
    plt.title('2018 sales')
    plt.show()


main()

