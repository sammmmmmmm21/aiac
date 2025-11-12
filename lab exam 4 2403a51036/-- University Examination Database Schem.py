import sqlite3
from datetime import datetime

# University Examination Database Schema, sample data, and query
# Tables: Students, Subjects, Marks
# Database: SQLite

# Create connection to database (creates file if doesn't exist)
conn = sqlite3.connect('university_exam.db')
cursor = conn.cursor()

print("=" * 60)
print("UNIVERSITY EXAMINATION DATABASE")
print("=" * 60)

# Drop tables if they exist (safe to re-run)
print("\nDropping existing tables...")
cursor.execute("DROP TABLE IF EXISTS Marks;")
cursor.execute("DROP TABLE IF EXISTS Subjects;")
cursor.execute("DROP TABLE IF EXISTS Students;")

# Create Students table
print("Creating Students table...")
cursor.execute("""
    CREATE TABLE Students (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        dob DATE,
        enrollment_year INTEGER
    )
""")

# Create Subjects table
print("Creating Subjects table...")
cursor.execute("""
    CREATE TABLE Subjects (
        subject_id INTEGER PRIMARY KEY,
        subject_name TEXT NOT NULL,
        max_marks INTEGER NOT NULL DEFAULT 100
    )
""")

# Create Marks table
print("Creating Marks table...")
cursor.execute("""
    CREATE TABLE Marks (
        mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        subject_id INTEGER NOT NULL,
        marks_obtained INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES Students(student_id),
        FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
    )
""")

# Insert sample students
print("Inserting sample students...")
students_data = [
    (1, 'Alice', 'Johnson', '2001-04-12', 2019),
    (2, 'Bob', 'Smith', '2000-11-03', 2018),
    (3, 'Carol', 'Davis', '2001-07-21', 2019),
    (4, 'Dave', 'Lee', '1999-02-10', 2017),
    (5, 'Eve', 'Turner', '2002-09-05', 2020)
]
cursor.executemany("""
    INSERT INTO Students (student_id, first_name, last_name, dob, enrollment_year)
    VALUES (?, ?, ?, ?, ?)
""", students_data)

# Insert subjects
print("Inserting subjects...")
subjects_data = [
    (1, 'Mathematics', 100),
    (2, 'Physics', 100),
    (3, 'Chemistry', 100)
]
cursor.executemany("""
    INSERT INTO Subjects (subject_id, subject_name, max_marks)
    VALUES (?, ?, ?)
""", subjects_data)

# Insert marks data
print("Inserting marks data...")
# Alice: all >85 (qualifies)
marks_data = [
    (1, 1, 92),
    (1, 2, 88),
    (1, 3, 90),
    # Bob: not all >85
    (2, 1, 80),
    (2, 2, 86),
    (2, 3, 78),
    # Carol: one =85 (does NOT qualify, since requirement is above 85%)
    (3, 1, 85),
    (3, 2, 87),
    (3, 3, 90),
    # Dave: missing one subject (should NOT qualify)
    (4, 1, 90),
    (4, 2, 92),
    # Eve: all >85 (qualifies)
    (5, 1, 90),
    (5, 2, 95),
    (5, 3, 88)
]
cursor.executemany("""
    INSERT INTO Marks (student_id, subject_id, marks_obtained)
    VALUES (?, ?, ?)
""", marks_data)

# Commit all changes
conn.commit()

# Query: find students scoring above 85% in ALL subjects
print("\n" + "=" * 60)
print("QUERY RESULTS: Students with >85% in ALL subjects")
print("=" * 60)

query = """
    SELECT
        s.student_id,
        s.first_name,
        s.last_name,
        ROUND(AVG(CAST(m.marks_obtained AS FLOAT) / sub.max_marks) * 100, 2) AS average_percentage
    FROM Students s
    JOIN Marks m ON s.student_id = m.student_id
    JOIN Subjects sub ON m.subject_id = sub.subject_id
    GROUP BY s.student_id, s.first_name, s.last_name
    HAVING
        COUNT(DISTINCT m.subject_id) = (SELECT COUNT(*) FROM Subjects)
        AND MIN(CAST(m.marks_obtained AS FLOAT) / sub.max_marks) > 0.85
    ORDER BY average_percentage DESC
"""

cursor.execute(query)
results = cursor.fetchall()

if results:
    print(f"\n{'Student ID':<12} {'First Name':<15} {'Last Name':<15} {'Avg %':<10}")
    print("-" * 52)
    for row in results:
        student_id, first_name, last_name, avg_percentage = row
        print(f"{student_id:<12} {first_name:<15} {last_name:<15} {avg_percentage:<10}")
else:
    print("\nNo students found meeting the criteria.")

# Display all students with their marks for reference
print("\n" + "=" * 60)
print("ALL STUDENTS AND THEIR MARKS")
print("=" * 60)

all_marks_query = """
    SELECT
        s.student_id,
        s.first_name,
        s.last_name,
        sub.subject_name,
        m.marks_obtained,
        ROUND(CAST(m.marks_obtained AS FLOAT) / sub.max_marks * 100, 2) AS percentage
    FROM Students s
    LEFT JOIN Marks m ON s.student_id = m.student_id
    LEFT JOIN Subjects sub ON m.subject_id = sub.subject_id
    ORDER BY s.student_id, sub.subject_id
"""

cursor.execute(all_marks_query)
all_results = cursor.fetchall()

for row in all_results:
    if row[3]:  # Only print if subject exists
        student_id, first_name, last_name, subject_name, marks, percentage = row
        print(f"Student {student_id} ({first_name} {last_name}): {subject_name} = {marks}/100 ({percentage}%)")
    else:
        student_id, first_name, last_name = row[0], row[1], row[2]
        print(f"Student {student_id} ({first_name} {last_name}): No marks recorded")

# Close connection
conn.close()
print("\n" + "=" * 60)
print("Database operations completed successfully!")
print("=" * 60)