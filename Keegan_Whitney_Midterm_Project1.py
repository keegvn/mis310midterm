import tkinter as tk

#function to calculate average
def calculate_average(scores):
    total = 0
    for score in scores:
        total = total + score
    return total / len(scores)

#function to determine letter grade
def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

#main function when button is clicked
def show_results():
    try:
        score1 = float(entry1.get())
        score2 = float(entry2.get())
        score3 = float(entry3.get())

        scores = [score1, score2, score3]

        average = calculate_average(scores)

        grade = get_letter_grade(average)

        highest = scores[0]
        for s in scores:
            if s > highest:
                highest = s

        if average >= 60:
            status = "Passing"
        else:
            status = "Failing"

        if average >= 90:
            message = "Honor Roll"
        elif average < 70:
            message = "Needs Improvement"
        else:
            message = "Good Work"

        result_label.config(
            text=
            "Average: " + str(round(average, 2)) +
            "\nLetter Grade: " + grade +
            "\nHighest Score: " + str(highest) +
            "\nStatus: " + status +
            "\nMessage: " + message
        )

    except:
        result_label.config(text="Error: Enter valid numbers")

#clear function
def clear_all():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    result_label.config(text="")

window = tk.Tk()
window.title("Student Grade Application")
window.geometry("350x320")

tk.Label(window, text="Student Grade Application", font=("Arial", 14)).pack(pady=10)

tk.Label(window, text="Enter Score 1").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter Score 2").pack()
entry2 = tk.Entry(window)
entry2.pack()

tk.Label(window, text="Enter Score 3").pack()
entry3 = tk.Entry(window)
entry3.pack()

tk.Button(window, text="Calculate Results", command=show_results).pack(pady=10)
tk.Button(window, text="Clear", command=clear_all).pack()

result_label = tk.Label(window, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=15)

window.mainloop()