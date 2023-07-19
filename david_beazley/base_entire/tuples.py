

# Кортежы
stock = ('GOOG', 100, 490.10)
adress = 'www.python.org', 80
# person = first_name, last_name, phone

filename = "portfolio.csv"
portfolio = []

for line in open(filename):
	fields = line.split(",")
	name = fields[0]
	shares = int(fields[1])
	price = float(fields[2])
	stock = (name, shares, price)
	portfolio.append(stock)

