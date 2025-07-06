import csv

def load_csv(file_path):
    print(f"📂 Attempting to load: {file_path}")  # NEW DEBUG LINE
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        print(f"✅ Loaded {len(data)} rows.")
        return data
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return []

def filter_data(data, column_name, condition, value):
    if not data or column_name not in data[0]:
        return []

    filtered = []
    for row in data:
        cell = row[column_name]

        try:
            cell_val = float(cell)
            target_val = float(value)
        except ValueError:
            cell_val = cell
            target_val = value

        if condition == 'equals' and cell_val == target_val:
            filtered.append(row)
        elif condition == 'greater_than' and isinstance(cell_val, (int, float)) and cell_val > target_val:
            filtered.append(row)
        elif condition == 'less_than' and isinstance(cell_val, (int, float)) and cell_val < target_val:
            filtered.append(row)

    return filtered

def display_data(data):
    if not data:
        print("No data to display.")
        return

    headers = data[0].keys()
    print("\n".join([", ".join(headers)]))
    for row in data:
        print(", ".join(row.values()))

if __name__ == "__main__":
    file_path = r"C:\Users\ioan1\Desktop\CSV_Analyzer_FIXED\employees.csv"

    data = load_csv(file_path)

    if data:
        print("Filter: Salary > 50000")
        filtered = filter_data(data, "Salary", "greater_than", "50000")
        display_data(filtered)

def save_to_csv(data, output_path):
    if not data:
        print("No data to save.")
        return
    with open(output_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ Saved {len(data)} rows to {output_path}")


save_to_csv(filtered, "test_output.csv")

