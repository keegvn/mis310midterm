This repository contains two Python-based graphical user interface (GUI) applications built using the **Tkinter** library. These tools are designed for academic management and information retrieval.

---

## Table of Contents
1. [Student Grade Application](#1-student-grade-application)
2. [CCSU Mobile Info App](#2-ccsu-mobile-info-app)
3. [Installation & Requirements](#3-installation--requirements)

---

## 1. Student Grade Application
A utility for educators and students to quickly calculate grades and analyze performance metrics based on three input scores.

### Key Features
* **Average Calculation:** Automatically computes the mean score.
* **Letter Grade Assignment:** Uses standard grading scales (A, B, C, D, F).
* **Performance Tracking:** Identifies the highest score among the three entries.
* **Status Indicators:** Categorizes results as "Passing" or "Failing."
* **Motivational Feedback:** Provides context-aware messages such as "Honor Roll" or "Needs Improvement."
* **Error Handling:** Prevents crashes if non-numeric data is entered.

---

## 2. CCSU Mobile Info App
A desktop information portal designed for Central Connecticut State University, utilizing a data-driven approach to display campus resources.

### Key Features
* **Data Integration:** Powered by the `pandas` library to read from a local CSV database.
* **Categorized Views:**
    * **Calendar:** Displays key academic dates.
    * **Buildings:** Lists campus infrastructure and locations.
    * **Faculty:** Provides a directory of faculty names.
* **Branded Interface:** Features a custom UI with the university logo and themed color palette.
* **Dynamic Filtering:** Specifically filters out empty cells to show only relevant data for the selected category.

---

## 3. Installation & Requirements

### System Requirements
* **Python 3.x**
* **Pandas Library** (Required for the CCSU App)

### Dependencies
To install the necessary library for the CCSU Info App, run:
```bash
pip install pandas
