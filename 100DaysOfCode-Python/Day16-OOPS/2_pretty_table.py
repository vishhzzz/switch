from prettytable import PrettyTable, ALL

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# to add horizontal lines 
table.hrules = ALL

print(table.align)

table.align = 'l'
print(table.align)
print(table)