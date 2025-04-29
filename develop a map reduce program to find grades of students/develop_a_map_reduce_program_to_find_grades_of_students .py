# ===========================
# Simulated MapReduce Program
# ===========================

# Holds the student data as (name, marks)
student_records = []

# -----------------------
# Mapper: Assign a grade
# -----------------------
def mapper(record):
    name, marks = record
    marks = int(marks)

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"
    
    return (grade, name)

# -----------------------------------------
# Shuffle and Sort: Group names by grades
# -----------------------------------------
def shuffle_and_sort(mapped_data):
    shuffle_dict = {}
    for grade, name in mapped_data:
        if grade not in shuffle_dict:
            shuffle_dict[grade] = []
        shuffle_dict[grade].append(name)
    return shuffle_dict

# -----------------------
# Reducer: Just return it
# -----------------------
def reducer(shuffled_data):
    return shuffled_data

# -----------------------------------
# Full MapReduce Flow (Driver Logic)
# -----------------------------------
def run_mapreduce(data):
    mapped = [mapper(record) for record in data]
    shuffled = shuffle_and_sort(mapped)
    reduced = reducer(shuffled)
    return reduced

# -------------------------
# Interactive Menu System
# -------------------------
def menu():
    while True:
        print("\n==== Student Grading System (Simulated MapReduce) ====")
        print("1. Add Student")
        print("2. View Grade of a Student")
        print("3. List Students by Grade")
        print("4. Show All Grade-wise Records")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter student name: ").strip()
            marks = input("Enter student marks: ").strip()
            if not marks.isdigit():
                print("❌ Invalid marks. Please enter a number.")
                continue
            student_records.append((name, marks))
            print("✅ Student added successfully.")

        elif choice == '2':
            name = input("Enter student name to check grade: ").strip()
            found = False
            for record in student_records:
                if record[0].lower() == name.lower():
                    grade, _ = mapper(record)
                    print(f"🎓 {record[0]} has grade: {grade}")
                    found = True
                    break
            if not found:
                print("❌ Student not found.")

        elif choice == '3':
            grade_query = input("Enter grade to search (A+, A, B, C, D, F): ").strip().upper()
            reduced = run_mapreduce(student_records)
            students = reduced.get(grade_query, [])
            if students:
                print(f"📋 Students with grade {grade_query}: {', '.join(students)}")
            else:
                print(f"⚠️ No students found with grade {grade_query}.")

        elif choice == '4':
            if not student_records:
                print("⚠️ No student records available.")
            else:
                reduced = run_mapreduce(student_records)
                print("📊 Grade-wise student list:")
                for grade in sorted(reduced.keys(), reverse=True):
                    print(f"{grade}: {', '.join(reduced[grade])}")

        elif choice == '5':
            print("👋 Exiting. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

# -----------------------
# Start the program
# -----------------------
if __name__ == "__main__":
    menu()
