import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

class TranslationTool:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Language Translator")
        self.root.geometry("600x450")
        
        self.translator = Translator()
        
        # --- UI Elements ---
        # Language Selection
        languages = list(LANGUAGES.values())
        
        self.label_src = tk.Label(root, text="Source Language:")
        self.label_src.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        self.src_lang_combo = ttk.Combobox(root, values=languages, width=25)
        self.src_lang_combo.set("english")
        self.src_lang_combo.grid(row=1, column=0, padx=10, pady=5)
        
        self.label_dest = tk.Label(root, text="Target Language:")
        self.label_dest.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        self.dest_lang_combo = ttk.Combobox(root, values=languages, width=25)
        self.dest_lang_combo.set("spanish")
        self.dest_lang_combo.grid(row=1, column=1, padx=10, pady=5)
        
        # Text Input Area
        self.input_text = tk.Text(root, height=8, width=65)
        self.input_text.grid(row=2, column=0, columnspan=2, padx=20, pady=10)
        self.input_text.insert(tk.END, "Enter text here...")

        # Translate Button
        self.trans_btn = tk.Button(root, text="Translate Now", bg="#4CAF50", fg="white", 
                                   font=("Arial", 10, "bold"), command=self.translate_text)
        self.trans_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Output Area
        self.output_text = tk.Text(root, height=8, width=65, bg="#f0f0f0")
        self.output_text.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

    def translate_text(self):
        try:
            # 1. Get user input
            text_to_translate = self.input_text.get("1.0", tk.END).strip()
            src_lang = self.src_lang_combo.get()
            dest_lang = self.dest_lang_combo.get()
            
            if not text_to_translate:
                messagebox.showwarning("Warning", "Please enter some text to translate.")
                return

            # 2. Process Translation
            # Mapping language name back to code (e.g., 'spanish' -> 'es')
            lang_codes = {v: k for k, v in LANGUAGES.items()}
            translated = self.translator.translate(
                text_to_translate, 
                src=lang_codes[src_lang], 
                dest=lang_codes[dest_lang]
            )
            
            # 3. Display Result
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated.text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Translation failed: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslationTool(root)
    root.mainloop()