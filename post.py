import cv2
import pytesseract
import pandas as pd
import re
from fuzzywuzzy import fuzz
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"



def load_pincode_data(csv_file="Pincode_Hierarchical_Address.csv"):
    df = pd.read_csv(csv_file)
    df.columns = df.columns.str.strip().str.lower()
    df['pincode'] = df['pincode'].astype(str)
    df['address'] = df['address'].str.lower()
    return df


def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or unreadable at path: " + image_path)
    return pytesseract.image_to_string(image)


def normalize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_pincode(text):
    matches = re.findall(r'\d{6}', text)
    return matches[0] if matches else None


def validate_info(text, df):
    normalized_text = normalize(text)
    extracted_pincode = extract_pincode(normalized_text)

    if not extracted_pincode:
        return "❌ No pincode found in the image."

    for _, row in df.iterrows():
        if extracted_pincode == row['pincode']:
            return f"✅ Correct Pincode {extracted_pincode} found for the address."

    
    best_score = 0
    best_pincode, best_address = None, None
    for _, row in df.iterrows():
        score = fuzz.ratio(normalized_text, row['address'])
        if score > best_score:
            best_score = score
            best_pincode = row['pincode']
            best_address = row['address']

    if best_score > 70:
        return f"❌ Incorrect Pincode!\nSuggested: {best_pincode}\nAddress: {best_address}"
    else:
        return "❌ No good address match found."


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("📍 Pincode Validator")
        self.root.geometry("700x600")
        self.root.configure(bg="#f5f5f5")

        try:
            self.df = load_pincode_data()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")
            self.df = None

        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 10), padding=10)
        style.configure("TLabel", background="#f5f5f5", font=("Segoe UI", 10))

        ttk.Label(root, text="Upload an image to validate Pincode and Address:", font=("Segoe UI", 12, "bold"), background="#f5f5f5").pack(pady=20)
        ttk.Button(root, text="📤 Upload Image", command=self.load_image).pack(pady=10)

        self.img_label = ttk.Label(root)
        self.img_label.pack(pady=10)

        self.result_box = tk.Text(root, height=15, width=80, wrap="word", font=("Segoe UI", 10))
        self.result_box.pack(padx=20, pady=20)
        self.result_box.configure(state='disabled')

    def load_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if not image_path:
            return

        if self.df is None:
            messagebox.showerror("Error", "CSV not loaded correctly.")
            return

        try:
            image = Image.open(image_path)
            image.thumbnail((300, 300))
            img_tk = ImageTk.PhotoImage(image)
            self.img_label.configure(image=img_tk)
            self.img_label.image = img_tk

            extracted_text = extract_text_from_image(image_path)
            result = validate_info(extracted_text, self.df)

            self.result_box.configure(state='normal')
            self.result_box.delete(1.0, tk.END)
            self.result_box.insert(tk.END, f"🔍 Extracted Text:\n{extracted_text}\n\n--- Result ---\n{result}\n")
            self.result_box.configure(state='disabled')

        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


