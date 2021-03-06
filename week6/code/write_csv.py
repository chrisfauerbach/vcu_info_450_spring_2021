import csv
cars = []
cars.append({"id": 1, "color":"blue", "make": "ford", "model":"flex"})
cars.append({"id": 2, "color":"orange", "make": "hyundai", "model":"santa fe sport"})
cars.append({"id": 3, "color":"green", "make": "honda", "model":"accord"})
cars.append({"id": 4, "color":"white", "make": "kia", "model":"sorento"})
cars.append({"id": 5, "color":"black", "make": "jeep", "model":"wrangler"})
cars.append({"id": 6, "color":"red", "make": "jaguar", "model":"f-type"})

with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'color','make','model']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader() # Up to you
    # for car in cars:
        # writer.writerow(car)
    writer.writerows(cars)
