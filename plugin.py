import requests
import tkinter as tk
from tkinter import messagebox

class MeshyAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.meshy.ai/api"

    def generate_3d_model(self, input_data):
        # Make API request to generate 3D model
        url = f"{self.base_url}/generate_3d_model"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.post(url, json=input_data, headers=headers)
            # Check for errors in the response
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "error", "message": response.text}
        except requests.exceptions.RequestException as e:
            return {"status": "error", "message": str(e)}

def submit():
    api_key = api_key_entry.get()
    input_data = input_data_entry.get("1.0", tk.END).strip()
    
    if not api_key or not input_data:
        messagebox.showerror("Error", "API key and input data are required")
        return
    
    meshy_api = MeshyAPI(api_key)
    result = meshy_api.generate_3d_model(input_data)
    
    if result["status"] == "error":
        messagebox.showerror("Error", result["message"])
    else:
        messagebox.showinfo("Success", "3D model generated successfully")

# Create the main window
root = tk.Tk()
root.title("Meshy API 3D Model Generator")

# Create and place the API key label and entry
tk.Label(root, text="API Key:").grid(row=0, column=0, padx=10, pady=10)
api_key_entry = tk.Entry(root, width=50)
api_key_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the input data label and text box
tk.Label(root, text="Input Data:").grid(row=1, column=0, padx=10, pady=10)
input_data_entry = tk.Text(root, width=50, height=10)
input_data_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
