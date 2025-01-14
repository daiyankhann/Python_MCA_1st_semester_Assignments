def minimum_life(cost, earnings, salvage, rate):
    n = 1 
    while True:
        
        pv_earnings = earnings * (1 - (1 + rate) ** -n) / rate
        pv_salvage = salvage / (1 + rate) ** n
        pv_total = pv_earnings + pv_salvage
        
  
        if pv_total > cost:
            return n
        n += 1

cost = 6000
earnings = 1000
salvage = 2000
rate = 0.12
min_life = minimum_life(cost, earnings, salvage, rate)
print(f"The minimum life of the machine to make it a more attractive investment is: {min_life} years.")