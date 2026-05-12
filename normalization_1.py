employees = [
    {
        "id": 1,
        "name": "Amit Sharma",
        "details": {"salary": 55000, "city": "Pune", "department": "HR"}
    },
    {
        "id": 2,
        "name": "Neha Verma",
        "details": {"salary": 72000, "city": "Mumbai", "department": "IT"}
    },
    {
        "id": 3,
        "name": "Rajesh Kumar",
        "details": {"salary": 48000, "city": "Delhi", "department": "Finance"}
    },
    {
        "id": 4,
        "name": "Sneha Patil",
        "details": {"salary": 65000, "city": "Pune", "department": "Marketing"}
    },
    {
        "id": 5,
        "name": "Arjun Singh",
        "details": {"salary": 80000, "city": "Bangalore", "department": "IT"}
    },
    {
        "id": 6,
        "name": "Kavita Joshi",
        "details": {"salary": 53000, "city": "Ahmedabad", "department": "HR"}
    },
    {
        "id": 7,
        "name": "Rahul Mehta",
        "details": {"salary": 90000, "city": "Mumbai", "department": "Finance"}
    },
    {
        "id": 8,
        "name": "Priya Nair",
        "details": {"salary": 67000, "city": "Kochi", "department": "Marketing"}
    },
    {
        "id": 9,
        "name": "Vikram Desai",
        "details": {"salary": 75000, "city": "Surat", "department": "IT"}
    },
    {
        "id": 10,
        "name": "Anjali Gupta",
        "details": {"salary": 60000, "city": "Delhi", "department": "HR"}
    }
]


def normalized_data(emp_list):
    result = []

    for emp in emp_list:
        emp_id = emp["id"]
        name = emp["name"]
        salary = emp["details"]["salary"]
        city = emp["details"]["city"]
        department = emp["details"]["department"]

        result.append((emp_id, name, salary, city, department))

    return result
output = normalized_data(employees)
print(output)
