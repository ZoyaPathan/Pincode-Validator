#  PINCODE Validator

A Python-based PIN Code Validation System that verifies Indian PIN codes using a hierarchical address dataset. The application checks whether a given PIN code exists in the dataset and retrieves its corresponding location details, making it useful for address verification and postal information lookup.

---

##  Project Overview

The PINCODE Validator is designed to validate Indian postal PIN codes by searching through a structured CSV dataset containing hierarchical address information. The program allows users to input a PIN code and returns the associated address details if the PIN code exists.

This project demonstrates the use of Python for data processing, CSV file handling, and efficient searching of structured datasets.

---

##  Features

-  Validate Indian PIN codes
-  Search through a hierarchical address dataset
-  Display corresponding location details
-  Handle invalid or non-existent PIN codes gracefully
-  Simple and user-friendly Python implementation
-  Lightweight and easy to run

---

##  Technologies Used

- Python 3.x
- Pandas
- CSV Dataset

---

##  Project Structure

```
PINCODE_validator/

│── post.py                          # Main Python program
│── Pincode_Hierarchical_Address.csv # Dataset containing Indian PIN codes
│── README.md                        # Project documentation
```

---

##  Dataset Information

The project uses the following dataset:

**Pincode_Hierarchical_Address.csv**

The dataset contains hierarchical postal address information such as:

- PIN Code
- State
- District
- City
- Area
- Other location-related details

The dataset serves as the source for validating and retrieving address information.

---

##  Prerequisites

Before running the project, ensure that you have:

- Python 3.x installed
- pip installed

Check your installation:

```bash
python --version
```

or

```bash
python3 --version
```

---
 

## Running the Project

Execute the Python file:

```bash
python post.py
```

The program will prompt you to enter a PIN code.

Example:

```
Enter PIN Code: 411001
```

If the PIN code exists, the corresponding address details will be displayed.

---

##  Working

1. Load the CSV dataset.
2. Accept the PIN code as user input.
3. Search the dataset for the entered PIN code.
4. If found, display the corresponding address information.
5. If not found, display an appropriate validation message.

---


##  Contributors

- **Uttam Gupta**
- **Zoya Pathan**

---

## 📄 License

This project is developed for educational and learning purposes.
