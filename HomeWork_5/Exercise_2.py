names = ['Max', 'Stiv', 'Ben']
salaries = [60000, 80000, 100000]
premium_rate = ["16.5%", "10.25%", "7.4%"]

premium = {name: salary * premium / 100 for name, salary, premium in
           zip(names, salaries, map(lambda x: float(x[:-1:]), premium_rate))}

print(premium)