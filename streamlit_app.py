import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="QR Code Generator",
    page_icon="📱",
    layout="centered"
)

# Title and description
st.title("📱 QR Code Generator")
st.markdown("Generate QR codes from any URL instantly!")

# Input section
url = st.text_input(
    "Enter a URL:",
    placeholder="https://example.com",
    help="Enter the full URL including https://"
)

# Customization options in an expander
with st.expander("⚙️ Customize QR Code (Optional)"):
    col1, col2 = st.columns(2)
    
    with col1:
        box_size = st.slider(
            "Box Size",
            min_value=5,
            max_value=20,
            value=10,
            help="Size of each box in the QR code"
        )
        
        fill_color = st.color_picker(
            "Foreground Color",
            value="#000000",
            help="Color of the QR code pattern"
        )
    
    with col2:
        border = st.slider(
            "Border Size",
            min_value=1,
            max_value=10,
            value=4,
            help="Thickness of the border"
        )
        
        back_color = st.color_picker(
            "Background Color",
            value="#FFFFFF",
            help="Background color of the QR code"
        )

# Generate button
if st.button("Generate QR Code", type="primary"):
    if url:
        try:
            # Create QR code instance
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=box_size,
                border=border,
            )
            qr.add_data(url)
            qr.make(fit=True)

            # Create an image from the QR Code instance
            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            
            # Convert PIL Image to bytes for display and download
            buf = BytesIO()
            img.save(buf, format="PNG")
            byte_im = buf.getvalue()

            # Display the QR code
            st.success("✅ QR Code generated successfully!")
            st.image(byte_im, caption=f"QR Code for: {url}", use_container_width=True)
            
            # Download button
            # Generate a safe filename from URL
            safe_url_name = "".join(
                c for c in url if c.isalnum() or c in ['.', '_', '-']
            ).replace('/', '_').replace(':', '_').replace('?', '_').replace('=', '_')
            
            filename = f"qr_code_{safe_url_name}.png"
            if len(filename) > 200:
                filename = filename[:200] + '.png'
            
            st.download_button(
                label="⬇️ Download QR Code",
                data=byte_im,
                file_name=filename,
                mime="image/png"
            )
            
        except Exception as e:
            st.error(f"❌ Error generating QR code: {e}")
    else:
        st.warning("⚠️ Please enter a URL first!")

# Sidebar with information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This app generates QR codes from URLs.
    
    **How to use:**
    1. Enter a URL in the text box
    2. (Optional) Customize the appearance
    3. Click "Generate QR Code"
    4. Download your QR code
    
    **Features:**
    - Custom colors
    - Adjustable size
    - Instant generation
    - One-click download
    """)
    
    st.header("📚 Examples")
    st.markdown("""
    Try these URLs:
    - `https://www.google.com`
    - `https://www.github.com`
    - `https://www.wikipedia.org`
    """)
    
    st.divider()
    
    st.markdown("**Made with ❤️ using Streamlit**")
    st.markdown("[View on GitHub](https://github.com/YOUR_USERNAME/QR_Code_Maker)")

# Footer
st.divider()
st.caption("💡 Tip: QR codes work best with high contrast colors (e.g., black on white)")
