# Grade Calculator System
# Day 6 Practice Project - Conditional Statements

def get_letter_grade(score):
    """
    Convert numerical score to letter grade with +/- modifiers
    """
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 97:
        return "A+"
    elif score >= 93:
        return "A"
    elif score >= 90:
        return "A-"
    elif score >= 87:
        return "B+"
    elif score >= 83:
        return "B"
    elif score >= 80:
        return "B-"
    elif score >= 77:
        return "C+"
    elif score >= 73:
        return "C"
    elif score >= 70:
        return "C-"
    elif score >= 67:
        return "D+"
    elif score >= 63:
        return "D"
    elif score >= 60:
        return "D-"
    else:
        return "F"

def get_gpa(letter_grade):
    """
    Convert letter grade to GPA (4.0 scale)
    """
    gpa_scale = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "D-": 0.7,
        "F": 0.0
    }
    return gpa_scale.get(letter_grade, 0.0)

def get_status(score):
    """
    Determine pass/fail status
    """
    if score >= 60:
        return "PASS"
    else:
        return "FAIL"

def get_performance_comment(score):
    """
    Provide personalized feedback based on score
    """
    if score >= 90:
        return "Excellent! Outstanding performance!"
    elif score >= 80:
        return "Great job! Keep up the good work!"
    elif score >= 70:
        return "✓ Good work! You're doing well!"
    elif score >= 60:
        return "Satisfactory, but there's room for improvement."
    else:
        return "Needs improvement. Consider additional study."

def display_menu():
    """Display main menu"""
    print("\n" + "=" * 60)
    print("              GRADE CALCULATOR SYSTEM")
    print("=" * 60)
    print("1. Calculate single student grade")
    print("2. Calculate multiple students grades")
    print("3. View grade distribution")
    print("4. Calculate class statistics")
    print("5. Check if student passed/failed")
    print("6. Compare two students")
    print("7. Exit")
    print("=" * 60)

def calculate_single_grade():
    """Calculate grade for a single student"""
    print("\n--- Single Student Grade Calculator ---")
    
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("✗ Name cannot be empty!")
            return
        
        score = float(input("Enter score (0-100): "))
        
        if score < 0 or score > 100:
            print("✗ Score must be between 0 and 100!")
            return
        
        # Calculate grade details
        letter_grade = get_letter_grade(score)
        gpa = get_gpa(letter_grade)
        status = get_status(score)
        comment = get_performance_comment(score)
        
        # Display results
        print("\n" + "-" * 50)
        print(f"Student: {name}")
        print(f"Score: {score:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")
        print(f"Status: {status}")
        print(f"Comment: {comment}")
        print("-" * 50)
        
    except ValueError:
        print("✗ Please enter a valid number!")

def calculate_multiple_grades():
    """Calculate grades for multiple students"""
    print("\n--- Multiple Students Grade Calculator ---")
    
    try:
        num_students = int(input("How many students? "))
        
        if num_students <= 0:
            print("✗ Number must be positive!")
            return
        
        students = []
        
        for i in range(num_students):
            print(f"\n--- Student {i+1} ---")
            name = input("Name: ").strip()
            score = float(input("Score (0-100): "))
            
            if score < 0 or score > 100:
                print(f"✗ Invalid score for {name}. Skipping...")
                continue
            
            letter_grade = get_letter_grade(score)
            gpa = get_gpa(letter_grade)
            status = get_status(score)
            
            students.append({
                "name": name,
                "score": score,
                "letter_grade": letter_grade,
                "gpa": gpa,
                "status": status
            })
        
        # Display results table
        if students:
            print("\n" + "=" * 70)
            print(f"{'Name':<20} {'Score':<10} {'Grade':<10} {'GPA':<10} {'Status':<10}")
            print("=" * 70)
            
            for student in students:
                print(f"{student['name']:<20} {student['score']:<10.2f} "
                      f"{student['letter_grade']:<10} {student['gpa']:<10.2f} "
                      f"{student['status']:<10}")
            
            print("=" * 70)
            
            # Calculate averages
            avg_score = sum(s['score'] for s in students) / len(students)
            avg_gpa = sum(s['gpa'] for s in students) / len(students)
            passed = sum(1 for s in students if s['status'] == "PASS")
            
            print(f"\nClass Average Score: {avg_score:.2f}")
            print(f"Class Average GPA: {avg_gpa:.2f}")
            print(f"Students Passed: {passed}/{len(students)}")
        
    except ValueError:
        print("✗ Please enter valid numbers!")

def view_grade_distribution():
    """Show grade distribution ranges"""
    print("\n" + "=" * 60)
    print("                 GRADE DISTRIBUTION")
    print("=" * 60)
    print("Grade | Range      | GPA  | Description")
    print("-" * 60)
    print("A+    | 97-100     | 4.0  | Outstanding")
    print("A     | 93-96      | 4.0  | Excellent")
    print("A-    | 90-92      | 3.7  | Excellent")
    print("B+    | 87-89      | 3.3  | Very Good")
    print("B     | 83-86      | 3.0  | Good")
    print("B-    | 80-82      | 2.7  | Good")
    print("C+    | 77-79      | 2.3  | Satisfactory")
    print("C     | 73-76      | 2.0  | Satisfactory")
    print("C-    | 70-72      | 1.7  | Satisfactory")
    print("D+    | 67-69      | 1.3  | Poor")
    print("D     | 63-66      | 1.0  | Poor")
    print("D-    | 60-62      | 0.7  | Poor")
    print("F     | 0-59       | 0.0  | Failing")
    print("=" * 60)

def calculate_class_statistics():
    """Calculate statistics for a class"""
    print("\n--- Class Statistics Calculator ---")
    
    try:
        num_students = int(input("How many students? "))
        
        if num_students <= 0:
            print("✗ Number must be positive!")
            return
        
        scores = []
        
        for i in range(num_students):
            score = float(input(f"Enter score for student {i+1}: "))
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("✗ Invalid score. Skipping...")
        
        if not scores:
            print("✗ No valid scores entered!")
            return
        
        # Calculate statistics
        total = sum(scores)
        average = total / len(scores)
        highest = max(scores)
        lowest = min(scores)
        passed = sum(1 for s in scores if s >= 60)
        failed = len(scores) - passed
        
        # Grade distribution
        grade_counts = {}
        for score in scores:
            grade = get_letter_grade(score)
            grade_counts[grade] = grade_counts.get(grade, 0) + 1
        
        # Display statistics
        print("\n" + "=" * 50)
        print("CLASS STATISTICS")
        print("=" * 50)
        print(f"Total Students:     {len(scores)}")
        print(f"Average Score:      {average:.2f}")
        print(f"Highest Score:      {highest:.2f}")
        print(f"Lowest Score:       {lowest:.2f}")
        print(f"Students Passed:    {passed} ({passed/len(scores)*100:.1f}%)")
        print(f"Students Failed:    {failed} ({failed/len(scores)*100:.1f}%)")
        print("\nGrade Distribution:")
        for grade in sorted(grade_counts.keys()):
            count = grade_counts[grade]
            percentage = (count / len(scores)) * 100
            print(f"  {grade}: {count} students ({percentage:.1f}%)")
        print("=" * 50)
        
    except ValueError:
        print("✗ Please enter valid numbers!")

def check_pass_fail():
    """Check if a student passed or failed"""
    print("\n--- Pass/Fail Checker ---")
    
    try:
        score = float(input("Enter score (0-100): "))
        
        if score < 0 or score > 100:
            print("✗ Score must be between 0 and 100!")
            return
        
        status = get_status(score)
        letter_grade = get_letter_grade(score)
        
        print("\n" + "-" * 40)
        if status == "PASS":
            print(f"✓ PASSED with {letter_grade}")
            print(f"Score: {score:.2f}")
            if score >= 60 and score < 70:
                print("Note: Consider improving to reach higher grades")
        else:
            print(f"✗ FAILED with {letter_grade}")
            print(f"Score: {score:.2f}")
            print(f"Need {60 - score:.2f} more points to pass")
        print("-" * 40)
        
    except ValueError:
        print("✗ Please enter a valid number!")

def compare_students():
    """Compare two students' grades"""
    print("\n--- Compare Two Students ---")
    
    try:
        print("Student 1:")
        name1 = input("Name: ").strip()
        score1 = float(input("Score: "))
        
        print("\nStudent 2:")
        name2 = input("Name: ").strip()
        score2 = float(input("Score: "))
        
        if not (0 <= score1 <= 100 and 0 <= score2 <= 100):
            print("✗ Scores must be between 0 and 100!")
            return
        
        grade1 = get_letter_grade(score1)
        grade2 = get_letter_grade(score2)
        gpa1 = get_gpa(grade1)
        gpa2 = get_gpa(grade2)
        
        print("\n" + "=" * 60)
        print("COMPARISON RESULTS")
        print("=" * 60)
        print(f"{'Metric':<20} {name1:<20} {name2:<20}")
        print("-" * 60)
        print(f"{'Score':<20} {score1:<20.2f} {score2:<20.2f}")
        print(f"{'Letter Grade':<20} {grade1:<20} {grade2:<20}")
        print(f"{'GPA':<20} {gpa1:<20.2f} {gpa2:<20.2f}")
        print("=" * 60)
        
        # Determine winner
        if score1 > score2:
            diff = score1 - score2
            print(f"\n{name1} scored higher by {diff:.2f} points!")
        elif score2 > score1:
            diff = score2 - score1
            print(f"\n {name2} scored higher by {diff:.2f} points!")
        else:
            print(f"\n Both students have the same score!")
        
    except ValueError:
        print("✗ Please enter valid numbers!")

def main():
    """Main program"""
    print("Welcome to Grade Calculator System!")
    print("This system helps you calculate and analyze student grades.")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            calculate_single_grade()
        elif choice == '2':
            calculate_multiple_grades()
        elif choice == '3':
            view_grade_distribution()
        elif choice == '4':
            calculate_class_statistics()
        elif choice == '5':
            check_pass_fail()
        elif choice == '6':
            compare_students()
        elif choice == '7':
            print("\nThank you for using Grade Calculator!")
            print("Study hard and aim high!")
            break
        else:
            print("\n✗ Invalid choice! Please enter 1-7.")

# Run the program
if __name__ == "__main__":
    main()