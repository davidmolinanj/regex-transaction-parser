# regex-transaction-parser

[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](#)
[![Topic: Regular Expressions & Data Parsing](https://img.shields.io/badge/Topic-Regex%20%26%20Validation-success.svg)](#)

A modular Python application designed to process, validate, filter, and generate transaction logs using **Regular Expressions (Regex)**. The system robustly handles multiple data formats, including phone numbers, Spanish identity documents (DNI/NIE), complex timestamps, geographical coordinates (calculating distances via the Haversine formula), and monetary amounts.

## 🚀 Key Features

* **Advanced Regex Validation:** Processes and validates complex structured logs with multiple data formats and localizations.
* **Modular Architecture:** Code organized into dedicated modules for each validation (`compra.py`, `telefono.py`, `nif.py`, `coordenada.py`, `dinero.py`, `instante_temporal.py`).
* **Geospatial Filtering:** Calculates geographical distances between coordinates using the Haversine formula (`-slocation`).
* **Chronological Filtering:** Parses and compares dates across various formats to filter transactions within specific time ranges (`-stime`).
* **Synthetic Data Generation:** Includes a tool to randomly generate valid and realistic log datasets (`-generate`).

## 🛠️ Project Structure

* `main.py`: Main entry point handling command-line arguments.
* `comando.py`: Core logic for normalization, filtering, and data generation.
* `compra.py`: Transaction parser coordinating individual validators.
* `dic_er.py`: Centralized repository of all compiled regular expressions.
* `coordenada.py` & `instante_temporal.py`: Geospatial and temporal validation engines.
* `nif.py` & `telefono.py`: Identity document control letter verification and phone number normalization.

## 📋 Requirements

* **Python 3.x**
* Exclusively uses the Python standard library (`re`, `sys`, `math`, `random`). No external dependencies required.

## 💻 Usage & Commands

The main program is executed from the terminal using `main.py` along with the desired command flag and the text file to be analyzed (e.g., `logG3.txt`). Each option is explained below:

### 1. Normalize and Display (`-n`)
Validates the formatting of transactions in the file line by line. Optionally, you can append two numbers to force specific output formats for both time (1, 2, or 3) and coordinates (1, 2, or 3).
* **Standard usage:** `python main.py -n tests/logG3.txt`
* **Forced formats usage:** `python main.py -n tests/logG3.txt 1 1`

### 2. Filter by Phone Number (`-sphone`)
Extracts and displays exclusively the transactions matching a specific 9-digit phone number.
* **Usage example:** `python main.py -sphone 123456789 tests/logG3.txt`

### 3. Filter by DNI/NIE (`-snif`)
Filters transactions associated with a specific identity document. The system internally validates that the control letter matches the numbers before filtering.
* **Usage example:** `python main.py -snif X2229423X tests/logG3.txt`

### 4. Filter by Time Range (`-stime`)
Displays purchases made within a specified time window bounded by two timestamps (start date and end date), supporting any of the three time formats configured in the regular expressions.
* **Usage example:** `python main.py -stime "2020-06-22 23:23" "2020-06-22 23:23" tests/logG3.txt`

### 5. Filter by Location and Distance (`-slocation`)
Searches for and extracts transactions that occurred within a specific distance radius (in kilometers), taking user-provided geographical coordinates as the point of origin.
* **Usage example:** `python main.py -slocation "-15.847566204432525, 25.737288846644418" 3000 tests/logG3.txt`

### 6. Generate Random Logs (`-generate`)
Synthetic data creation tool. Generates a specified number of transaction lines with completely valid and random formats and data, saving them to a new file.
* **Usage example:** `python main.py -generate tests/output_logs.txt 40`
