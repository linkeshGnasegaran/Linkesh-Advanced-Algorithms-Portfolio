import time


# Medicine entity class
class Medicine:
    def __init__(self, medicine_id, name, category, price, quantity):
        self.medicine_id = medicine_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (f"{self.medicine_id} | {self.name} | {self.category} | "
                f"RM {self.price:.2f} | Stock: {self.quantity}")


# Hash Table using Open Addressing and Linear Probing
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # Same hashing style as Practical 6
        return sum(ord(char) for char in key) % self.size

    def insert(self, medicine, show_message=True):
        index = self.hash_function(medicine.medicine_id)
        start_index = index

        # Linear probing
        while self.table[index] is not None:
            # Update medicine if same ID already exists
            if self.table[index].medicine_id == medicine.medicine_id:
                self.table[index] = medicine
                print("Medicine record updated successfully.")
                return

            index = (index + 1) % self.size

            if index == start_index:
                print("Hash table is full.")
                return

        self.table[index] = medicine
        if show_message:
            print(f"Medicine inserted at index {index}.")

    def search(self, medicine_id):
        index = self.hash_function(medicine_id)
        start_index = index

        while self.table[index] is not None:
            if self.table[index].medicine_id == medicine_id:
                return self.table[index]

            index = (index + 1) % self.size

            if index == start_index:
                break

        return None

    def display(self):
        print("\n=== PHARMACY HASH TABLE ===")

        for i, medicine in enumerate(self.table):
            print(f"Index {i}: {medicine}")


def array_search(medicine_list, medicine_id):
    for medicine in medicine_list:
        if medicine.medicine_id == medicine_id:
            return medicine

    return None


def performance_experiment():
    print("\n=== HASH TABLE VS ARRAY PERFORMANCE EXPERIMENT ===")

    # Same 1,000 medicine records stored in both structures
    experiment_table = HashTable(2003)
    experiment_array = []

    for i in range(1000):
        medicine = Medicine(
            f"MED{i:04d}",
            f"Medicine {i}",
            "General",
            10.00,
            50
        )

        experiment_table.insert(medicine, False)
        experiment_array.append(medicine)

    target_id = "MED0999"
    repetitions = 1000

    # Hash-table timing
    start_time = time.perf_counter_ns()

    for i in range(repetitions):
        experiment_table.search(target_id)

    hash_time = time.perf_counter_ns() - start_time

    # Array timing
    start_time = time.perf_counter_ns()

    for i in range(repetitions):
        array_search(experiment_array, target_id)

    array_time = time.perf_counter_ns() - start_time

    print(f"\nRecords inserted: {len(experiment_array)}")
    print(f"Target medicine ID: {target_id}")
    print(f"Number of searches: {repetitions}")
    print(f"\nHash table search time: {hash_time:,} ns")
    print(f"Array search time:      {array_time:,} ns")

    if hash_time < array_time:
        print("\nResult: Hash table was faster.")
    else:
        print("\nResult: Array was faster in this run.")


def main():
    pharmacy_table = HashTable(11)

    medicine_list = [
        Medicine("MED101", "Paracetamol", "Pain Relief", 5.50, 100),
        Medicine("MED102", "Cetirizine", "Allergy", 9.90, 50),
        Medicine("MED103", "Vitamin C", "Supplement", 18.50, 40),
        Medicine("MED104", "Cough Syrup", "Cold and Flu", 12.00, 30),
        Medicine("MED105", "Antacid", "Digestive", 7.80, 90)
    ]

    # Insert predefined medicine records
    for medicine in medicine_list:
        pharmacy_table.insert(medicine)

    while True:
        print("\n=== PHARMACY INVENTORY SYSTEM ===")
        print("1. Insert Medicine")
        print("2. Search Medicine")
        print("3. Display Hash Table")
        print("4. Run Performance Experiment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            medicine_id = input("Enter medicine ID: ").upper()
            name = input("Enter medicine name: ")
            category = input("Enter category: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            new_medicine = Medicine(
                medicine_id,
                name,
                category,
                price,
                quantity
            )

            pharmacy_table.insert(new_medicine)

        elif choice == "2":
            medicine_id = input("Enter medicine ID to search: ").upper()
            result = pharmacy_table.search(medicine_id)

            if result is not None:
                print("\nMedicine found:")
                print(result)
            else:
                print("\nMedicine not found.")

        elif choice == "3":
            pharmacy_table.display()

        elif choice == "4":
            performance_experiment()

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please enter 1 to 5.")


main()