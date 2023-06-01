lives = 3
print(type(lives))
age = 12
budget = 500

temperature = 15.2
print(type(temperature))

budget_jan = 600
budget_feb = 400
budget_mar = 700
avg_budget = ((budget_jan+budget_feb+budget_mar)/3)
print("El presupuesto promedio para el trimestre enero-marzo es", avg_budget)

budget_january = input("¿Cuál es tu presupuesto para enero? ")
budget_february = input("¿Cuál es tu presupuesto para febrero? ")
budget_march = input("¿Cuál es tu presupuesto para marzo? ")

budget_january = int(budget_january)
budget_february = int(budget_february)
budget_march = int(budget_march)

avg_budget2 = ((budget_january+budget_february+budget_march)/3)
print("El presupuesto promedio para el trimestre enero-marzo es", avg_budget2)