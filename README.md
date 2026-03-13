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

## 🛠️ Comprehensive Tech Stack

This project leverages a modern, decoupled architecture blending a responsive frontend with a robust, serverless backend.

### Frontend
- **HTML5:** Semantic and accessible HTML architecture
- **CSS3:** Vanilla CSS featuring Custom Glassmorphism UI, smooth micro-animations, and dynamic CSS variables
- **JavaScript (ES6+):** Modern Fetch API integration for seamless, no-reload module generations

### Backend & API
- **Python:** Core processing and business logic
- **FastAPI:** High-performance async REST framework for endpoints
- **Uvicorn:** Lightning-fast ASGI web server for local development

### Processing & Deployment
- **Image Processing:** `Pillow` (PIL) & `qrcode` libraries for dynamic pixel-level binary rendering
- **Deployment:** Serverlessly hosted on **Vercel** for immediate, global CDN distribution

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

## 🏆 My Contributions & Journey

This repository represents significant effort and dedication in creating a modern, lightweight, and efficient tool from scratch. Key milestones and contributions include:
- **Full-Stack Development:** Designed the **responsive Glassmorphism UI** and loosely coupled it with a robust **Python/FastAPI backend**.
- **Performance Optimization:** Successfully implemented deployment strategies through Vercel's serverless functions by configuring the **ASGI environment**.
- **Innovative Image Manipulation:** Developed logic to seamlessly manipulate `BytesIO` streams with `Pillow`, overcoming statelessness issues on serverless CDNs.
- **Open-Source Mindset:** Formed the entire architecture with vanilla libraries, completely avoiding heavy third-party UI overhead.

## 🧑‍💻 Author

**Aditya Singh** ([@imsinghaditya07](https://github.com/imsinghaditya07))  
*Developer, Designer, and Open Source Enthusiast*
