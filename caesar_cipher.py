import tkinter as tk
from tkinter import messagebox


class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CipherGuard - Caesar Cipher")
        self.root.geometry("900x650")
        self.root.minsize(760, 560)
        self.root.configure(bg="#0f172a")

        self.shift_var = tk.IntVar(value=3)
        self.status_var = tk.StringVar(value="Ready")

        self.build_ui()

    def encrypt_text(self, text, shift):
        result = []
        for char in text:
            if 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            elif 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                result.append(char)
        return ''.join(result)

    def process(self, mode):
        text = self.input_box.get("1.0", tk.END).rstrip("\n")
        if not text.strip():
            messagebox.showwarning("Empty Message", "Please enter a message first.")
            return

        shift = self.shift_var.get()
        if mode == "decrypt":
            shift = -shift

        output = self.encrypt_text(text, shift)
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert("1.0", output)
        self.status_var.set(
            "Encryption completed successfully."
            if mode == "encrypt"
            else "Decryption completed successfully."
        )

    def clear_all(self):
        self.input_box.delete("1.0", tk.END)
        self.output_box.delete("1.0", tk.END)
        self.shift_var.set(3)
        self.status_var.set("Ready")

    def copy_output(self):
        text = self.output_box.get("1.0", tk.END).rstrip("\n")
        if not text:
            messagebox.showinfo("Nothing to Copy", "There is no output to copy.")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()
        self.status_var.set("Output copied to clipboard.")

    def build_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#111827", height=105)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header, text="CIPHERGUARD", font=("Segoe UI", 25, "bold"),
            fg="#38bdf8", bg="#111827"
        ).pack(anchor="w", padx=35, pady=(20, 0))

        tk.Label(
            header, text="Caesar Cipher • Encryption & Decryption",
            font=("Segoe UI", 11), fg="#cbd5e1", bg="#111827"
        ).pack(anchor="w", padx=37, pady=(2, 0))

        # Main content
        main = tk.Frame(self.root, bg="#0f172a")
        main.pack(fill="both", expand=True, padx=30, pady=22)

        # Input/output panels
        panels = tk.Frame(main, bg="#0f172a")
        panels.pack(fill="both", expand=True)

        left = tk.Frame(panels, bg="#1e293b")
        left.pack(side="left", fill="both", expand=True, padx=(0, 10))

        right = tk.Frame(panels, bg="#1e293b")
        right.pack(side="left", fill="both", expand=True, padx=(10, 0))

        self.make_panel_title(left, "INPUT MESSAGE", "Enter plaintext to encrypt or ciphertext to decrypt.")
        self.input_box = self.make_textbox(left)

        self.make_panel_title(right, "OUTPUT", "Processed text will appear here.")
        self.output_box = self.make_textbox(right)

        # Controls
        controls = tk.Frame(main, bg="#0f172a")
        controls.pack(fill="x", pady=(18, 0))

        shift_frame = tk.Frame(controls, bg="#1e293b")
        shift_frame.pack(side="left", fill="x", expand=True)

        tk.Label(
            shift_frame, text="SHIFT VALUE", font=("Segoe UI", 10, "bold"),
            fg="#94a3b8", bg="#1e293b"
        ).pack(side="left", padx=(15, 8), pady=14)

        tk.Spinbox(
            shift_frame, from_=0, to=25, textvariable=self.shift_var,
            width=5, font=("Segoe UI", 12, "bold"),
            bg="#0f172a", fg="#f8fafc", insertbackground="#f8fafc",
            buttonbackground="#334155", relief="flat"
        ).pack(side="left", pady=10)

        tk.Label(
            shift_frame, text="(0–25)", font=("Segoe UI", 9),
            fg="#64748b", bg="#1e293b"
        ).pack(side="left", padx=8)

        buttons = tk.Frame(controls, bg="#0f172a")
        buttons.pack(side="right")

        self.make_button(buttons, "ENCRYPT", "#0284c7", lambda: self.process("encrypt"))
        self.make_button(buttons, "DECRYPT", "#7c3aed", lambda: self.process("decrypt"))
        self.make_button(buttons, "COPY", "#334155", self.copy_output)
        self.make_button(buttons, "CLEAR", "#475569", self.clear_all)

        # Footer/status
        footer = tk.Frame(self.root, bg="#111827", height=48)
        footer.pack(fill="x", side="bottom")
        footer.pack_propagate(False)

        tk.Label(
            footer, text="●", font=("Segoe UI", 10), fg="#22c55e", bg="#111827"
        ).pack(side="left", padx=(30, 6), pady=14)

        tk.Label(
            footer, textvariable=self.status_var, font=("Segoe UI", 9),
            fg="#cbd5e1", bg="#111827"
        ).pack(side="left", pady=14)

        tk.Label(
            footer, text="SkillCraft Technology • Task 01",
            font=("Segoe UI", 9), fg="#64748b", bg="#111827"
        ).pack(side="right", padx=30)

    def make_panel_title(self, parent, title, subtitle):
        tk.Label(
            parent, text=title, font=("Segoe UI", 11, "bold"),
            fg="#e2e8f0", bg="#1e293b"
        ).pack(anchor="w", padx=18, pady=(16, 2))
        tk.Label(
            parent, text=subtitle, font=("Segoe UI", 8),
            fg="#64748b", bg="#1e293b"
        ).pack(anchor="w", padx=18, pady=(0, 8))

    def make_textbox(self, parent):
        box = tk.Text(
            parent, wrap="word", font=("Consolas", 11),
            bg="#0b1220", fg="#e2e8f0", insertbackground="#38bdf8",
            selectbackground="#0369a1", relief="flat", padx=14, pady=14
        )
        box.pack(fill="both", expand=True, padx=14, pady=(0, 14))
        return box

    def make_button(self, parent, text, color, command):
        tk.Button(
            parent, text=text, command=command,
            font=("Segoe UI", 9, "bold"), fg="white", bg=color,
            activebackground=color, activeforeground="white",
            relief="flat", bd=0, padx=15, pady=11, cursor="hand2"
        ).pack(side="left", padx=4)


if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
