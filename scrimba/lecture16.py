import colorama
from colorama import Fore
print(f"{Fore.GREEN} ---selling lemonade---")
print()
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]

sale = int(input('week 2 sunday sale value: '))
sales_w2.append(sale)

sales = sales_w1 + sales_w2
sales_str = " ".join(f"{Fore.YELLOW}{i}" for i in sales)

best = max(sales)
best_profit = best * 1.5
worst = min(sales)
worst_profit = worst * 1.5
combined = best_profit + worst_profit
print(f"{Fore.GREEN}{'sales':<24}: {sales_str}")
print(f"{Fore.GREEN}{'best day and profit':<24}: {Fore.BLUE}{str(best)}, {str(best_profit)}$")
print(f"{Fore.GREEN}{'worst day':<24}: {Fore.RED}{str(worst)}, {str(worst_profit)}$")
print(f"{Fore.GREEN}{'combined profit':<24}: {str(combined)}$")

