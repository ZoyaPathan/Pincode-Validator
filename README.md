#  PINCODE Validator

The application allows users to upload an image containing an address or postal information. Using OCR, the system extracts the text, identifies the pincode, and compares it with a CSV-based database of valid addresses and corresponding pincodes. It then displays whether the detected pincode is valid and provides the associated address information when a match is found.
---

##  Project Overview

The Pincode Validator Tool is a Python-based desktop application that leverages Optical Character Recognition (OCR) to automatically extract text from uploaded images, detect the pincode, and verify its authenticity using a structured database of addresses and pincodes. The application features an intuitive Tkinter-based graphical interface, making the validation process simple and user-friendly.

This project demonstrates the practical integration of OCR, GUI development, and database connectivity to automate address verification and minimize manual errors in pincode validation.

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
