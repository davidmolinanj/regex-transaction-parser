# 📊 Transaction & Log Parser (Regex Engine)

[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](#)
[![Topic: Regular Expressions & Data Parsing](https://img.shields.io/badge/Topic-Regex%20%26%20Validation-success.svg)](#)

A robust, modular Python application designed to parse, validate, filter, and generate structured transaction logs using advanced **Regular Expressions (Regex)**. The system handles multi-format fields including phone numbers, Spanish IDs (DNI/NIE), complex timestamps, geographical coordinates (with Haversine distance calculations), and currency amounts.

## 🚀 Key Features

* **Advanced Regex Pattern Matching:** Validates complex structured logs containing multiple international and localized data formats.
* **Modular Architecture:** Clean separation of concerns with dedicated modules for validation (`compra.py`, `telefono.py`, `nif.py`, `coordenada.py`, `dinero.py`, `instante_temporal.py`).
* **Geospatial Filtering:** Calculates geographical distances between coordinates using the Haversine formula (`-slocation`).
* **Chronological Filtering:** Parses and compares dates across various formats to filter transactions within specific time ranges (`-stime`).
* **Synthetic Data Generation:** Includes a generator tool to produce randomized, realistic log datasets on the fly (`-generate`).

## 🛠️ Project Structure

* `main.py`: Main entry point handling command-line arguments (`sys.argv`).
* `comando.py`: Core logic for normalization, filtering, and dataset generation.
* `compra.py`: Transaction parser coordinating individual field validators.
* `dic_er.py`: Centralized repository of pre-compiled regular expressions.
* `coordenada.py` & `instante_temporal.py`: Geospatial and temporal validation engines.
* `nif.py` & `telefono.py`: ID control-letter verification and phone normalization.

## 💻 Usage & Commands

Run the program from the command line specifying the desired operation:

1. **Normalize and display valid records:**
   ```bash
   python main.py -n tests/logG3.txt
