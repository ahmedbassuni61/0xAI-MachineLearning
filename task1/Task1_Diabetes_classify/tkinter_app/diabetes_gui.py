#My Prombt
#Create a simple GUI using Tkinter that take features and classify them
#Model is diabetes_model.pkl
#Features=[gender[Female,Male], age:(float), hypertension:bool, heart_disease:bool, smoking_history[never,No Info,former,current], bmi:float, HbA1c_level:float, blood_glucose_level:int, diabetes:int]

import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import numpy as np
import pandas as pd
import os

# Load trained pipeline/model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "diabetes_model.pkl")
model = joblib.load(model_path)

# Feature order (same as training data)
features = [
    "gender", "age", "hypertension", "heart_disease", "smoking_history",
    "bmi", "HbA1c_level", "blood_glucose_level"
]

# GUI window
root = tk.Tk()
root.title("Diabetes Classifier")
root.geometry("400x500")

# Input fields
entries = {}

# Boxes

#################################################################################
# Gender dropdown
tk.Label(root, text="Gender").pack()
gender_cb = ttk.Combobox(root, values=["Female", "Male"])
gender_cb.pack()
entries["gender"] = gender_cb

# Age
tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()
entries["age"] = age_entry

# Hypertension
tk.Label(root, text="Hypertension (0/1)").pack()
htn_cb = ttk.Combobox(root, values=[0, 1])
htn_cb.pack()
entries["hypertension"] = htn_cb

# Heart Disease
tk.Label(root, text="Heart Disease (0/1)").pack()
hd_cb = ttk.Combobox(root, values=[0, 1])
hd_cb.pack()
entries["heart_disease"] = hd_cb

# Smoking history
tk.Label(root, text="Smoking History").pack()
smoke_cb = ttk.Combobox(root, values=["never", "No Info", "former", "current"])
smoke_cb.pack()
entries["smoking_history"] = smoke_cb

# BMI
tk.Label(root, text="BMI").pack()
bmi_entry = tk.Entry(root)
bmi_entry.pack()
entries["bmi"] = bmi_entry

# HbA1c level
tk.Label(root, text="HbA1c Level").pack()
hba1c_entry = tk.Entry(root)
hba1c_entry.pack()
entries["HbA1c_level"] = hba1c_entry

# Blood Glucose Level
tk.Label(root, text="Blood Glucose Level").pack()
bg_entry = tk.Entry(root)
bg_entry.pack()
entries["blood_glucose_level"] = bg_entry
#################################################################################

# --- Prediction Function ---
def predict():
    try:
        # Collect inputs
        data = {
            "gender": [entries["gender"].get()],
            "age": [float(entries["age"].get())],
            "hypertension": [int(entries["hypertension"].get())],
            "heart_disease": [int(entries["heart_disease"].get())],
            "smoking_history": [entries["smoking_history"].get()],
            "bmi": [float(entries["bmi"].get())],
            "HbA1c_level": [float(entries["HbA1c_level"].get())],
            "blood_glucose_level": [int(entries["blood_glucose_level"].get())],
        }

        # Convert to DataFrame (important for pipeline with ColumnTransformer)
        df = pd.DataFrame(data)

        # Predict
        pred = model.predict(df)[0]

        if pred == 1:
            messagebox.showinfo("Result", "⚠️ Patient is Diabetic")
        else:
            messagebox.showinfo("Result", "✅ Patient is NOT Diabetic")

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


# Button
tk.Button(root, text="Classify", command=predict).pack(pady=20)

root.mainloop()
