ShipList = [
  ["N2 Bomber", "Heavy Fighter", "Limited", 21],
  ["J-Type 327", "Light Combat", "Unlimited", 1],
  ["NX Cruiser", "Medium Fighter", "Limited", 18],
  ["N1 Starfighter", "Medium Fighter", "Unlimited", 25],
  ["Royal Cruiser", "Light Combat", "Limited", 4],
]

print("{:<15} {:<15} {:<11} {:<10}".format('SHIP NAME', 'CLASS', 'DEPLOYMENT', 'IN SERVICE'))

for i in ShipList:
  ShipName, Class, Deployment, InService = i
  print("{:<15} {:<15} {:<11} {:<10}".format(ShipName, Class, Deployment, InService))