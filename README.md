# Streamlit Code Editor

A web-based code editor with integrated console built using Streamlit.

![Screenshot of Streamlit Code Editor](https://via.placeholder.com/800x450)

## Features

- Interactive Python code editor with syntax highlighting
- Real-time code execution
- Multiple editor themes (Monokai, GitHub, Solarized Dark, Solarized Light, Dracula)
- Adjustable font size
- Optional line numbers
- Support for Python code execution
- JavaScript syntax highlighting (execution not yet supported)
- Integrated console output display

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/streamlit-code-editor.git
   cd streamlit-code-editor
   ```

2. Install the required dependencies:
   ```
   pip install streamlit streamlit-ace
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. The app will open in your default web browser at `http://localhost:8501`

3. Write your Python code in the editor and click "Run Code" to execute it

## Configuration

The editor offers several customization options in the sidebar:

- **Editor Theme**: Choose from Monokai, GitHub, Solarized Dark, Solarized Light, or Dracula
- **Font Size**: Adjust between 12 and 24 points
- **Line Numbers**: Toggle display of line numbers/gutter
- **Language**: Choose between Python and JavaScript (only Python execution is currently supported)

