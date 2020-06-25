import os

no_of_rooms = int(input())
sp_price, nor_price = input().split(" ")
target_revenue = int(input())
sp_price = int(sp_price)
nor_price = int(nor_price)
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_patients = 0


def price_calculator(rooms, count_of_month, no_of_days):
    patients = 0
    for i in range(1, no_of_days + 1):
        patients_on_day = (6 - count_of_month) ** 2 + abs(i - 15)
        if patients_on_day >= rooms:
            patients_on_day = rooms
        patients = patients + patients_on_day
    return patients


def calulator(no_of_rooms, sp_price, nor_price, target_revenue, month, days, total_patients):
    for i in range(0, len(month)):
        patient_per_month = price_calculator(no_of_rooms, month[i], days[i])
        total_patients = total_patients + patient_per_month

    for i in range(0, no_of_rooms + 1):
        nor_rooms = no_of_rooms - i
        sp_rooms = i
        income = (nor_rooms * nor_price) + (sp_rooms * sp_price)
        avg_income = income / no_of_rooms
        total_revenue = avg_income * total_patients
        if total_revenue > target_revenue:
            print(sp_rooms)
            exit()

    print(no_of_rooms)
    os.system("Pause")

if 5 <= no_of_rooms <= 100:
    if 0 <= sp_price <= 5000 or 0 <= nor_price <= 5000:
        if 0 <= target_revenue < 90000000:
            calulator(no_of_rooms, sp_price, nor_price, target_revenue, month, days, total_patients)
        else:
            exit()
    else:
        exit()
else:
    exit()
