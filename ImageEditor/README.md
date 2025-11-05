# 🖼️ Streamlit Image Editor

## 📘 Overview
The **Streamlit Image Editor** is a simple yet powerful web app that allows users to upload and edit images directly from their browser.  
It uses **Pillow (PIL)** and **OpenCV** to apply filters, resize, rotate, and enhance images with brightness, contrast, and color controls.

---

## 🧩 Version 1: Basic Image Editor (Pillow Only)

### 🧠 Description
This is the **starter version** of the image editor that allows users to:
- Upload images (`.jpg`, `.png`, `.jpeg`)
- View image details (size, mode, format)
- Resize and rotate images
- Apply basic filters (Blur, Detail, Emboss, Smooth)

### ⚙️ Features
| Feature | Description |
|----------|-------------|
| 🖼️ Upload | Upload image in multiple formats |
| 📏 Resize | Change width and height |
| 🔄 Rotate | Rotate image by degree |
| 🎨 Filters | Apply basic effects like Blur, Detail, Emboss, Smooth |
| 💾 View Info | Display size, mode, and format |

### 🧰 Requirements
```bash
pip install streamlit pillow
```

### ▶️ Run Command
```bash
streamlit run main.py
```

---

## 💡 Version 2: Enhanced Image Editor (More Filters + Controls)

### 🧠 Description
This upgraded version introduces a **modern UI** with **sidebar controls**, more filters, brightness/contrast/sharpness adjustments, and a download option.  
It gives users a professional editing feel while staying simple to use.

### ⚙️ Features
| Feature | Description |
|----------|-------------|
| 🖼️ Side-by-side View | Compare Original vs Edited image |
| 🧮 Resize & Rotate | Adjust image size and rotation |
| 🎨 Extended Filters | Blur, Contour, Emboss, Sharpen, Smooth, Grayscale, Invert, Sepia, Edge Enhance |
| 🌈 Adjustments | Brightness, Contrast, Sharpness, Color Intensity |
| 💾 Download | Download the final edited image |
| 🧱 Modular Code | Clean, well-structured functions |

### 🧰 Requirements
```bash
pip install streamlit pillow
```

### ▶️ Run Command
```bash
streamlit run main.py
```

---

## 🤖 Version 3: AI-Powered Image Editor (Pillow + OpenCV)

### 🧠 Description
The **advanced version** combines **Pillow** and **OpenCV** for powerful artistic filters.  
It introduces **AI-based effects** like Cartoonify, Pencil Sketch, Oil Painting, and HDR.  
It’s the closest you can get to a mini Photoshop built in Python!

### ⚙️ Features
| Category | Features |
|-----------|-----------|
| 🖼️ Image Upload | Supports JPG, JPEG, PNG |
| ✂️ Resize & Rotate | Interactive size and degree control |
| 🎨 Filters (Pillow) | Blur, Sharpen, Emboss, Smooth, Grayscale, Invert, Sepia |
| 🧠 AI Filters (OpenCV) | Cartoonify, Pencil Sketch, Oil Paint, HDR |
| 💡 Enhancements | Brightness, Contrast, Sharpness, Color |
| ⚡ UI | Side-by-side comparison and sidebar controls |
| 📥 Download | Export edited image as PNG |

### 🧰 Requirements
```bash
pip install streamlit pillow opencv-python opencv-contrib-python numpy
```

> Note: `opencv-contrib-python` is required for the **Oil Painting** filter.

### ▶️ Run Command
```bash
streamlit run main.py
```

---

## 🧠 Tech Stack
- **Streamlit** – Web app framework for fast prototyping  
- **Pillow (PIL)** – Image processing (resize, rotate, filter, enhance)  
- **OpenCV** – AI filters, edge detection, and artistic transformations  
- **NumPy** – Image array manipulation  
- **Python 3.8+** – Core programming language  

---

## 📸 Example Filters Preview
| Filter | Description |
|---------|-------------|
| **Cartoonify** | Turns photo into comic-style art |
| **Pencil Sketch** | Hand-drawn pencil look |
| **Oil Paint** | Adds oil painting texture |
| **HDR** | Boosts color and dynamic contrast |
| **Sepia** | Vintage brown tone |
| **Invert / Grayscale** | Classic transformations |

---

## 🚀 Future Enhancements
- ✂️ Crop and aspect ratio lock  
- 🖊️ Text or watermark overlay  
- 💾 Save in multiple formats (JPG, PNG, WEBP, PDF)  
- 🎭 AI style transfer (Neural artistic filters)  
- 🧠 Face detection & selective editing  

---

## 👨‍💻 Author
**Developed by:** Arzaul Haque  
**Tools Used:** Python, Streamlit, Pillow, OpenCV
