money=int(input("Money:"))
price=int(input("Price:"))
wrap=int(input("Wrap:"))
chocolates=0
temp_wrap=0
remaining_wrap=0

def wrappers(chocolates,choc,wrap,temp_wrap,remaining_wrap):
    while(temp_wrap>=wrap):
        temp_wrap = int(choc/wrap)
        remaining_wrap += choc%wrap
        choc=temp_wrap
        chocolates = chocolates + temp_wrap
    if(temp_wrap+remaining_wrap==wrap):
        chocolates += 1
    return chocolates

chocolates += int(money/price)
temp_wrap = chocolates
chocolates = wrappers(chocolates,temp_wrap,wrap,temp_wrap,remaining_wrap)
print(chocolates)
# print(5%3)