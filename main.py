def main():
    print('Witaj w programie do obsługi wysyłek paczek!')
    parcels = int(input('Ile paczek chcesz wysłać? '))

    max_weight = 20
    parcel_weight = 0
    empty_kg = 20
    sent_kg = 0
    parcel_number = 1
    gap_weight = 0
    parcel_gap_weight = None
    empty_kg = parcels * 20 - sent_kg
    max_empty_kg = gap_weight

    stop_program = False
    while not stop_program:
        element = float(input("Podaj wagę elementu lub wpisz '0' aby zakończyć: "))
        if element == 0:
            stop_program = True
        elif 10 < element < 1:
            stop_program = True
        else:
            if parcel_weight + element > 20:
                if 20 - parcel_weight > gap_weight:
                    gap_weight = 20 - parcel_weight
                    parcel_gap_weight = parcel_number
                if parcel_number == int(parcels):
                    break
                parcel_weight = 0
                parcel_weight += element
                parcel_number += 1
                sent_kg += element
            else:
                parcel_weight += element
                sent_kg += element




    print("\nPodsumowanie:")
    print(f"Liczba paczek wysłanych: {parcels}")
    print(f"Liczba kilogramów wysłanych: {sent_kg :.2f} kg")
    print(f"Suma 'pustych' kilogramów: {empty_kg - sent_kg :.2f} kg")
    print(f"Paczka o numerze {parcel_number} miała najwięcej 'pustych' kilogramów: {gap_weight :.2f} kg")


if __name__ == "__main__":
    main()