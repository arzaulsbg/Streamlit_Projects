import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
# pip install opencv-python
import cv2
import numpy as np
from io import BytesIO

st.set_page_config(page_title="AI-Powered Image Editor", layout="wide")
st.markdown("<h1 style='text-align:center;'>🎨 AI Image Editor (Pillow + OpenCV)</h1>", unsafe_allow_html=True)
st.markdown("---")

# Upload section
uploaded_image = st.file_uploader("📸 Upload an Image", type=["jpg", "jpeg", "png"])

def cv2_to_pil(cv2_img):
    """Convert OpenCV image to PIL format"""
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    return Image.fromarray(cv2_img)

def pil_to_cv2(pil_img):
    """Convert PIL image to OpenCV format"""
    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

if uploaded_image:
    img = Image.open(uploaded_image)
    cv_img = pil_to_cv2(img)

    # Sidebar controls
    with st.sidebar:
        st.header("⚙️ Basic Adjustments")
        width = st.number_input("Width", value=img.width)
        height = st.number_input("Height", value=img.height)
        degree = st.slider("Rotate (°)", 0, 360, 0)

        st.subheader("🎨 Filters")
        filters = st.selectbox(
            "Select a Filter",
            [
                "None", "Blur", "Contour", "Detail", "Emboss", "Sharpen", "Smooth",
                "Sepia", "Grayscale", "Invert", "Cartoon", "Pencil Sketch", "Oil Paint", "HDR"
            ]
        )

        st.subheader("💡 Enhancements")
        brightness = st.slider("Brightness", 0.5, 2.0, 1.0)
        contrast = st.slider("Contrast", 0.5, 2.0, 1.0)
        sharpness = st.slider("Sharpness", 0.5, 2.0, 1.0)
        color = st.slider("Color Intensity", 0.5, 2.0, 1.0)

        st.markdown("---")
        apply_btn = st.button("✨ Apply Edits")

    if apply_btn:
        # Resize & rotate
        edited = img.resize((width, height)).rotate(degree)
        cv_img = pil_to_cv2(edited)

        # ---- PIL filters ----
        if filters == "Blur":
            edited = edited.filter(ImageFilter.BLUR)
        elif filters == "Contour":
            edited = edited.filter(ImageFilter.CONTOUR)
        elif filters == "Detail":
            edited = edited.filter(ImageFilter.DETAIL)
        elif filters == "Emboss":
            edited = edited.filter(ImageFilter.EMBOSS)
        elif filters == "Sharpen":
            edited = edited.filter(ImageFilter.SHARPEN)
        elif filters == "Smooth":
            edited = edited.filter(ImageFilter.SMOOTH_MORE)
        elif filters == "Grayscale":
            edited = edited.convert("L").convert("RGB")
        elif filters == "Invert":
            edited = Image.eval(edited, lambda x: 255 - x)
        elif filters == "Sepia":
            sepia = np.array(edited.convert("RGB"))
            tr = 0.393 * sepia[:, :, 0] + 0.769 * sepia[:, :, 1] + 0.189 * sepia[:, :, 2]
            tg = 0.349 * sepia[:, :, 0] + 0.686 * sepia[:, :, 1] + 0.168 * sepia[:, :, 2]
            tb = 0.272 * sepia[:, :, 0] + 0.534 * sepia[:, :, 1] + 0.131 * sepia[:, :, 2]
            sepia = np.stack([tr, tg, tb], axis=2)
            sepia = np.clip(sepia, 0, 255).astype(np.uint8)
            edited = Image.fromarray(sepia)

        # ---- OpenCV filters ----
        elif filters == "Cartoon":
            gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 7)
            edges = cv2.adaptiveThreshold(
                gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
            )
            color = cv2.bilateralFilter(cv_img, 9, 250, 250)
            cartoon = cv2.bitwise_and(color, color, mask=edges)
            edited = cv2_to_pil(cartoon)

        elif filters == "Pencil Sketch":
            gray, sketch = cv2.pencilSketch(cv_img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
            edited = cv2_to_pil(sketch)

        elif filters == "Oil Paint":
            oil = cv2.xphoto.oilPainting(cv_img, 7, 1) if hasattr(cv2, 'xphoto') else cv2.edgePreservingFilter(cv_img)
            edited = cv2_to_pil(oil)

        elif filters == "HDR":
            hdr = cv2.detailEnhance(cv_img, sigma_s=12, sigma_r=0.15)
            edited = cv2_to_pil(hdr)

        # Apply enhancements (brightness, contrast, etc.)
        edited = ImageEnhance.Brightness(edited).enhance(brightness)
        edited = ImageEnhance.Contrast(edited).enhance(contrast)
        edited = ImageEnhance.Sharpness(edited).enhance(sharpness)
        edited = ImageEnhance.Color(edited).enhance(color)

        # Display images
        col1, col2 = st.columns(2)
        with col1:
            st.image(img, caption="🖼️ Original Image", use_column_width=True)
        with col2:
            st.image(edited, caption=f"🎨 Edited ({filters})", use_column_width=True)

        # Download button
        buf = BytesIO()
        edited.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button(
            "📥 Download Edited Image",
            data=byte_im,
            file_name=f"edited_{filters.lower().replace(' ','_')}.png",
            mime="image/png"
        )

else:
    st.info("👆 Upload an image to get started!")
