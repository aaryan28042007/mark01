import streamlit as st
import math

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Calculator")
st.caption("Simple & Scientific Calculator (Streamlit)")

# ---------------- SESSION STATE ----------------
if "expr" not in st.session_state:
    st.session_state.expr = ""

# ---------------- FUNCTIONS ----------------
def press(val):
    st.session_state.expr += str(val)

def clear():
    st.session_state.expr = ""

def backspace():
    st.session_state.expr = st.session_state.expr[:-1]

def calculate():
    try:
        st.session_state.expr = str(
            eval(st.session_state.expr, {"__builtins__": None}, math.__dict__)
        )
    except:
        st.session_state.expr = "Error"

def apply_func(func):
    try:
        value = float(eval(st.session_state.expr))
        st.session_state.expr = str(func(value))
    except:
        st.session_state.expr = "Error"

# ---------------- MODE SELECT ----------------
mode = st.radio(
    "Calculator Mode",
    ["Simple", "Scientific"],
    horizontal=True
)

# ---------------- DISPLAY ----------------
st.text_input(
    "Display",
    st.session_state.expr,
    disabled=True
)

st.divider()

# ======================================================
# SIMPLE CALCULATOR
# ======================================================
if mode == "Simple":

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
    ]

    for row in buttons:
        cols = st.columns(4)
        for i, key in enumerate(row):
            if cols[i].button(key, use_container_width=True):
                if key == "=":
                    calculate()
                else:
                    press(key)

    col1, col2 = st.columns(2)
    if col1.button("C", use_container_width=True):
        clear()
    if col2.button("⌫", use_container_width=True):
        backspace()

# ======================================================
# SCIENTIFIC CALCULATOR
# ======================================================
else:
    sci1 = ["sin", "cos", "tan", "√"]
    sci2 = ["log", "ln", "π", "e"]
    sci3 = ["x²", "x³", "^", "1/x"]

    for row in [sci1, sci2, sci3]:
        cols = st.columns(4)
        for i, key in enumerate(row):
            if cols[i].button(key, use_container_width=True):
                if key == "sin":
                    apply_func(lambda x: math.sin(math.radians(x)))
                elif key == "cos":
                    apply_func(lambda x: math.cos(math.radians(x)))
                elif key == "tan":
                    apply_func(lambda x: math.tan(math.radians(x)))
                elif key == "√":
                    apply_func(math.sqrt)
                elif key == "log":
                    apply_func(math.log10)
                elif key == "ln":
                    apply_func(math.log)
                elif key == "π":
                    press(math.pi)
                elif key == "e":
                    press(math.e)
                elif key == "x²":
                    apply_func(lambda x: x**2)
                elif key == "x³":
                    apply_func(lambda x: x**3)
                elif key == "^":
                    press("**")
                elif key == "1/x":
                    apply_func(lambda x: 1/x)

    st.divider()

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
    ]

    for row in buttons:
        cols = st.columns(4)
        for i, key in enumerate(row):
            if cols[i].button(key, use_container_width=True):
                if key == "=":
                    calculate()
                else:
                    press(key)

    col1, col2 = st.columns(2)
    if col1.button("C", use_container_width=True):
        clear()
    if col2.button("⌫", use_container_width=True):
        backspace()