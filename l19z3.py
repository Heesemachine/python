'''
 розклад руху маршрутних таксі: номер маршруту, кінцева зупинка, марка автобуса, час поїздки'''
def schedule():
    taxi = {}
    taxi["Number of race"] = input("Number of race : ") # Робимо ключі
    taxi["Finish"] = input("Finish : ").split("  ")
    taxi["Car variability"] = input("Car Variability : ")
    taxi["Time of drive"] = input("Time of drive : ")
    return taxi
def input_taxi():
    n = int(input("Numbers of free taxis : "))
    return [schedule() for i in range(n)]
def search_taxi(taxi_l, taxi_title):
    return list(filter(lambda taxi: taxi['Number race'] == taxi_title, taxi_l))

taxi_l = input_taxi()

while True:
    drive_accept = input('Do you want to take taxi {y/n} ? : ' )
    if drive_accept == 'n':
        break
    taxi_title = input('Taxi for search: ')
    taxi_res = search_taxi(taxi_l, taxi_title)
    if len(taxi_res) > 0:
        print(taxi_res)
    else:
        print('No taxis near')