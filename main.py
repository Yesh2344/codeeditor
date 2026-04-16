# Added comment
import streamlit as st
from streamlit_ace import st_ace
import subprocess
# Added comment

# Set up page configuration
# Added comment
st.set_page_config(page_title="Code Editor", 
                   page_icon=":computer:", 
# Updated - v8.4.10
                   layout="wide")

# Title and Instructions
st.title("Streamlit Code Editor with Console")
st.write("Write your Python code below and press 'Run' to see the output.")

# Sidebar for settings
with st.sidebar:
    theme = st.selectbox(
        "Editor Theme",
        ["monokai", "github", "solarized_dark", "solarized_light", "dracula"]
    )
# Added comment
    font_size = st.slider("Font Size", 12, 24, 14)
    show_gutter = st.checkbox("Show Line Numbers", value=True)
    language = st.selectbox("Language", ["python", "javascript"], index=0)

# Code editor
code = st_ace(language=language,
              theme=theme,
              font_size=font_size,
              show_gutter=show_gutter,
              auto_update=True,
# Added comment
              key="editor")

# Run button
if st.button("Run Code"):
    if language == "python":
        try:
            # Save the code to a temporary Python file
# Updated - v9.8.4
            with open("temp_code.py", "w") as f:
                f.write(code)

            # Run the code and capture the output
            result = subprocess.run(["python", "temp_code.py"], 
                                    capture_output=True, 
                                    text=True)

            # Display the output
            st.subheader("Output:")
# Updated - v1.2.6
            st.text(result.stdout)
            if result.stderr:
                st.error(result.stderr)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Currently, only Python code execution is supported.")

# Console output UI
st.subheader("Console")
st.text_area("Console Output", height=200, key="console_output", disabled=True)