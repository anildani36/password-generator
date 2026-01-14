# 🔐 PassGen | Modern Password Generator

A sleek, cryptographically secure password generation tool built with **Python 3.13** and **Flask**, designed with a strong focus on **security, minimalism, and user experience**.  
PassGen provides a real-time, responsive interface to create **high-entropy passwords on the fly**.

---

## ✨ Features

- **High-Entropy Generation**
  - Uses Python’s `secrets` module (cryptographically secure)
  - Avoids predictable pseudo-random generators

- **Real-Time UI Updates**
  - Password regenerates instantly as you adjust length or options

- **Modern Slider Experience**
  - Custom-styled range slider
  - Dynamic fill line for clear visual feedback

- **One-Click Copy**
  - Clipboard API integration
  - Smooth slide-up & fade notification animation

- **Responsive MVC Design**
  - Mobile-friendly layout
  - Clean separation of Models, Views, and Controllers
  - Built with Bootstrap 4.4

---

## 🛠 Tech Stack

**Backend**
- Python 3.13
- Flask (MVC Architecture)

**Frontend**
- Bootstrap 4.4
- FontAwesome 5
- Vanilla JavaScript (ES6+)

**Templating**
- Jinja2

---

## 📂 Project Structure

```

passgen-flask/
├── app.py              # Controller: Route handling & API endpoints
├── templates/          # Views: Responsive Jinja2 templates
│   └── index.html
└── README.md           # Documentation

````

---

## 🚀 Getting Started

### Prerequisites
- Python **3.13+**
- **uv** (Fast Python package manager)

---

### Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/your-username/passgen-flask.git
cd passgen-flask
````

2️⃣ **Create & activate a virtual environment using uv**

```bash
uv venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
```

3️⃣ **Install dependencies**

```bash
uv pip install flask
```

4️⃣ **Run the application**

```bash
python app.py
```

5️⃣ **Open in browser**

```
http://127.0.0.1:5000
```

---

## 💡 How It Works

1. **Select Length**

   * Use the slider to choose password length (8–25 characters)

2. **Customize Characters**

   * Toggle:

     * Uppercase
     * Lowercase
     * Numbers
     * Symbols

3. **Instant Feedback**

   * Password updates immediately via Fetch API calls

4. **Security First**

   * Passwords generated using `secrets.choice()`
   * Resistant to brute-force predictability

---

## 📸 UI Preview

* Centered **Glassmorphism-inspired** container
* Branding-focused **Navbar**
* Clean footer labeled under **TechWithAnil**
* Smooth micro-interactions for copy actions

![PassGen Dashboard](screentshots/password-gen-ui.png)

---

## 🔒 Security Notes

* No passwords are stored or logged
* All generation occurs server-side using secure entropy
* No external APIs involved

---

## 👨‍💻 Author

**TechWithAnil**
Built for security. Designed for simplicity.

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

⭐ If you find this project useful, consider starring the repository!
