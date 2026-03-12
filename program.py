list_of_rooms = []

# Funktion zur Berechnung der Fläche
def calculate_area(length, width):
    return length * width

numberOfRooms = int(input("Bitte geben Sie an wieviele Räume die Wohnung hat:"))
for i in range(numberOfRooms):

    roomName = input("\nBezeichnung des Raumes: ")
    length = float(input("Länge des Raumes in Meter: "))
    width = float(input("Breite des Raumes in Meter: "))

    roomArea = calculate_area(length, width)

    rectangular = input("Ist der Raum ein Rechteck? (j/n): ").lower()

    if rectangular == "n":
        print("Geben Sie die Maße des ausgeschnittenen Rechtecks an:")
        smallLength = float(input("Länge des kleineren Rechtecks: "))
        smallWidth = float(input("Breite des kleineren Rechtecks: "))

        roomArea -= calculate_area(smallLength, smallWidth)

    print(f"Fläche des Raumes: {roomArea} m²")

    list_of_rooms.append((roomName, roomArea))


print("\n---> Maßheft der Wohnung <---")

for room, area in list_of_rooms:
    print(f"{room}: {area} Quadratmeter")

total_area = sum(area for _, area in list_of_rooms)

print(f"\nDie Wohnung hat insgesamt {total_area} Quadratmeter.")
