import streamlit as st

# Inject custom CSS for hover effects
st.markdown("""
    <style>
        .calculate-button {
            background-color: green !important;
            color: white !important;
            transition: opacity 0.3s ease;
        }
        .calculate-button:hover {
            opacity: 0.6 !important;
        }
        .clear-button {
            background-color: red !important;
            color: white !important;
            transition: opacity 0.3s ease;
        }
        .clear-button:hover {
            opacity: 0.6 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Layout
st.title("🔢 Interactive Button Demo")

col1, col2 = st.columns(2)

with col1:
    if st.button("Calculate", key="calc", use_container_width=True):
        st.success("✅ Calculation complete!")

    # Add class to the button (via HTML)
    st.markdown('<div class="calculate-button" style="height:0;"></div>', unsafe_allow_html=True)

with col2:
    if st.button("Clear", key="clr", use_container_width=True):
        st.warning("🧹 Cleared!")

    st.markdown('<div class="clear-button" style="height:0;"></div>', unsafe_allow_html=True)
