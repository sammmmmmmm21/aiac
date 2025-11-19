document.addEventListener('DOMContentLoaded', () => {
    const marks1Input = document.getElementById('marks1');
    const marks2Input = document.getElementById('marks2');
    const marks3Input = document.getElementById('marks3');
    const calculateBtn = document.getElementById('calculateBtn');
    const totalMarksSpan = document.getElementById('totalMarks');
    const gradeSpan = document.getElementById('grade');

    calculateBtn.addEventListener('click', () => {
        const marks1 = parseInt(marks1Input.value) || 0;
        const marks2 = parseInt(marks2Input.value) || 0;
        const marks3 = parseInt(marks3Input.value) || 0;

        // Basic validation: ensure marks are within 0-100
        if (marks1 < 0 || marks1 > 100 ||
            marks2 < 0 || marks2 > 100 ||
            marks3 < 0 || marks3 > 100) {
            alert('Please enter marks between 0 and 100 for all subjects.');
            return;
        }

        const totalMarks = marks1 + marks2 + marks3;
        const averageMarks = totalMarks / 3;

        let grade;
        if (averageMarks >= 90) {
            grade = 'A+';
        } else if (averageMarks >= 80) {
            grade = 'A';
        } else if (averageMarks >= 70) {
            grade = 'B';
        } else if (averageMarks >= 60) {
            grade = 'C';
        } else if (averageMarks >= 50) {
            grade = 'D';
        } else {
            grade = 'F';
        }

        totalMarksSpan.textContent = totalMarks;
        gradeSpan.textContent = grade;
    });
});
