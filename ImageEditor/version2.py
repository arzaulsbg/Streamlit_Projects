import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO

st.set_page_config(page_title="Image Editor", layout="wide")
st.markdown("<h1 style='text-align:center;'>🖼️ Advanced Image Editor</h1>", unsafe_allow_html=True)
st.markdown("---")

# Upload image
uploaded_image = st.file_uploader("📸 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    img = Image.open(uploaded_image)

    # Sidebar controls
    with st.sidebar:
        st.header("⚙️ Edit Controls")
        width = st.number_input("Width", value=img.width)
        height = st.number_input("Height", value=img.height)
        degree = st.slider("Rotate (°)", 0, 360, 0)

        st.subheader("🎨 Filters")
        filters = st.selectbox(
            "Choose a filter",
            [
                "None", "Blur", "Contour", "Detail", "Edge Enhance",
                "Emboss", "Sharpen", "Smooth", "Find Edges",
                "Sepia", "Grayscale", "Invert"
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
        # Resize and rotate
        edited = img.resize((width, height)).rotate(degree)

        # Apply basic PIL filters
        if filters == "Blur":
            edited = edited.filter(ImageFilter.BLUR)
        elif filters == "Contour":
            edited = edited.filter(ImageFilter.CONTOUR)
        elif filters == "Detail":
            edited = edited.filter(ImageFilter.DETAIL)
        elif filters == "Edge Enhance":
            edited = edited.filter(ImageFilter.EDGE_ENHANCE_MORE)
        elif filters == "Emboss":
            edited = edited.filter(ImageFilter.EMBOSS)
        elif filters == "Sharpen":
            edited = edited.filter(ImageFilter.SHARPEN)
        elif filters == "Smooth":
            edited = edited.filter(ImageFilter.SMOOTH_MORE)
        elif filters == "Find Edges":
            edited = edited.filter(ImageFilter.FIND_EDGES)
        elif filters == "Grayscale":
            edited = edited.convert("L").convert("RGB")
        elif filters == "Invert":
            edited = Image.eval(edited, lambda x: 255 - x)
        elif filters == "Sepia":
            sepia_img = edited.convert("RGB")
            pixels = sepia_img.load()
            for y in range(sepia_img.height):
                for x in range(sepia_img.width):
                    r, g, b = pixels[x, y]
                    tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                    tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                    tb = int(0.272 * r + 0.534 * g + 0.131 * b)
                    pixels[x, y] = (min(255, tr), min(255, tg), min(255, tb))
            edited = sepia_img

        # Apply enhancements
        edited = ImageEnhance.Brightness(edited).enhance(brightness)
        edited = ImageEnhance.Contrast(edited).enhance(contrast)
        edited = ImageEnhance.Sharpness(edited).enhance(sharpness)
        edited = ImageEnhance.Color(edited).enhance(color)

        # Display original and edited images side-by-side
        col1, col2 = st.columns(2)
        with col1:
            st.image(img, caption="🖼️ Original Image", use_column_width=True)
        with col2:
            st.image(edited, caption="🎨 Edited Image", use_column_width=True)

        # Download edited image
        buf = BytesIO()
        edited.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button(
            "📥 Download Edited Image",
            data=byte_im,
            file_name="edited_image.png",
            mime="image/png"
        )

else:
    st.info("👆 Upload an image to get started!")
