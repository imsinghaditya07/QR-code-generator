<h1 align="center">🚀 ChromaQR - The Next-Generation QR Code Generator</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
</p>

<p align="center">
  <b>Elevate your digital presence with a stunning, highly-customizable QR Code generator. Built with modern, serverless architecture on Vercel for unparalleled speed and aesthetics.</b>
</p>

## 🌟 Live Demo

Check out the live deployment here:  
🚀 **[ChromaQR Generator](https://qr-code-generator-inky-gamma-97.vercel.app/)**

## 🛠️ Tech Stack Included

This repository blends a powerful frontend alongside a serverless backend.

- **Frontend:** HTML5, Vanilla CSS3 (Custom Glass UI and animations), JavaScript (ES6)
- **Backend:** Python + FastAPI 
- **Image Processing Library:** `Pillow` (PIL), `qrcode` Python libraries
- **Deployment Platform:** Vercel (Hobby Free Tier)
- **Development Tooling:** Uvicorn ASGI Web Server

## ✨ Features

- **Endlessly Custom:** Personalize your QR foreground and background with infinite gradient possibilities.
- **Premium Themes:** 5 unique module shapes like "Smooth Dots," "Rounded Corners," and "Vertical Bars."
- **Serverless API:** No loading or page-refreshing; generates binary blobs inline via modern fetch patterns.
- **Micro-Animations & Glassmorphism UI:** Stunning UI utilizing frosted-glass effects and soothing background ambiance.
- **100% Free architecture:** We cut out the paid dependencies. Open source code generating images directly using the `Pillow` Python backend library and FastAPI.

## 📸 Overview of the Architecture

This application decouples the frontend and backend strictly, all built onto a single ultra-light repository to live natively on Vercel.

| **Layer** | **Technologies Used** | **Purpose** |
| :--- | :--- | :--- |
| **Frontend UI** | HTML5, Vanilla CSS3 | Creates the modern, breathtaking dark glass UI. |
| **Client Logic** | JavaScript (ES6) | Uses `fetch()` to handle REST requests to the Python endpoint and automatically downloads PNGs. |
| **Backend Engine** | Python, FastAPI | Validates Hex colors and formats them into tuples. Creates `BytesIO` streams. |
| **Image Generator**| `qrcode[pil]`, `Pillow` | Uses specific module drawers (like `RoundedModuleDrawer`) to manipulate pixel rendering logic directly onto an image object. |
| **Hosting** | Vercel (`vercel.json`) | Instructs the CDN to serve `index.html` static routes globally while hooking `/api/index.py` to AWS Serverless Lambda functions automatically. |

## 🚀 How to Run Locally

If you'd like to customize the website and run it directly on your own machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/imsinghaditya07/QR-code-generator.git
   cd QR-code-generator
   ```

2. **Set up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate # On Windows: .\venv\Scripts\Activate.ps1
   ```

3. **Install Requirements:**
   ```bash
   pip install -r api/requirements.txt
   ```

4. **Change the Dev URL (Important!)**
   Inside `script.js` line 36, change `fetch('/api/generate'...` to `fetch('http://127.0.0.1:8000/api/generate'...` to use your local development server API.

5. **Start to Serve:**
   Open 2 terminals.
   Terminal 1 (Python Backend): `python -m uvicorn api.index:app --reload --port 8000`
   Terminal 2 (Static Frontend): `python -m http.server 3000`

6. Go to `http://127.0.0.1:3000` to view the app!

## ☁️ About Vercel Deployment

This codebase is specifically tuned for single-click deployment to Vercel.
The `vercel.json` maps frontend static assets using `@vercel/static` while building Python logic inside the `/api` route via `@vercel/python`.

## 🧑‍💻 Author

Built by [Aditya Singh](https://github.com/imsinghaditya07)
