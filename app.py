import streamlit as st
import matplotlib.pyplot as plt

from Task1 import read_files, add_signals, mul_const


# =========================
# Page
# =========================

st.set_page_config(
    page_title="DSP Signal Processing",
    layout="wide"
)

st.title("DSP Signal Processing")


# =========================
# Load Signals
# =========================

signals = read_files("input1")

signal_names = list(signals.keys())


# =========================
# Display Signals
# =========================

# ============= Display Signals =============

st.header("Display Signals")

selected_signals = st.multiselect(
    "Choose signal(s):",
    signal_names
)

display_type = st.radio(
    "Choose display type:",
    ["Continuous", "Discrete", "Both"],
    horizontal=True
)

if st.button("Display"):

    if not selected_signals:
        st.warning("Please select at least one signal.")

    else:

        # Create columns depending on number of selected signals
        cols = st.columns(len(selected_signals))

        for col, signal_name in zip(cols, selected_signals):

            with col:

                signal = signals[signal_name]

                indices = signal["indices"]
                samples = signal["samples"]

                st.subheader(signal_name)

                # -------- Continuous --------
                if display_type in ["Continuous", "Both"]:

                    fig, ax = plt.subplots(figsize=(5, 3))

                    ax.plot(indices, samples)

                    ax.set_xlabel("Index")
                    ax.set_ylabel("Signal Value")
                    ax.set_title("Continuous")

                    ax.grid(True, alpha=0.3)

                    st.pyplot(fig, use_container_width=False)

                    plt.close(fig)

                # -------- Discrete --------
                if display_type in ["Discrete", "Both"]:

                    fig, ax = plt.subplots(figsize=(5, 3))

                    ax.stem(indices, samples)

                    ax.set_xlabel("Index")
                    ax.set_ylabel("Signal Value")
                    ax.set_title("Discrete")

                    ax.grid(True, alpha=0.3)

                    st.pyplot(fig, use_container_width=False)

                    plt.close(fig)


# =========================
# Operations
# =========================

st.header("Signal Operations")

operation = st.selectbox(
    "Choose operation:",
    ["Addition", "Multiplication"]
)


# =========================
# Addition
# =========================

if operation == "Addition":

    selected_addition = st.multiselect(
        "Select signals to add:",
        signal_names
    )

    if st.button("Perform Addition"):

        if len(selected_addition) < 2:

            st.warning(
                "Please select at least two signals."
            )

        else:

            indices, samples = add_signals(
                signals,
                selected_addition
            )

            st.success("Addition completed successfully!")

            st.subheader("Addition Result")


            # Continuous

            fig, ax = plt.subplots()

            ax.plot(indices, samples)

            ax.set_xlabel("Index")
            ax.set_ylabel("Signal Value")
            ax.set_title("Continuous - Addition Result")

            ax.grid(True, alpha=0.3)

            st.pyplot(fig)


            # Discrete

            fig, ax = plt.subplots()

            ax.stem(indices, samples)

            ax.set_xlabel("Index")
            ax.set_ylabel("Signal Value")
            ax.set_title("Discrete - Addition Result")

            ax.grid(True, alpha=0.3)

            st.pyplot(fig)


# =========================
# Multiplication
# =========================

else:

    selected_signal = st.selectbox(
        "Select signal:",
        signal_names
    )

    const = st.number_input(
        "Enter multiplication constant:",
        value=1.0
    )

    if st.button("Perform Multiplication"):

        indices, samples = mul_const(
            const,
            signals,
            selected_signal
        )

        st.success("Multiplication completed successfully!")

        st.subheader("Multiplication Result")


        # Continuous

        fig, ax = plt.subplots()

        ax.plot(indices, samples)

        ax.set_xlabel("Index")
        ax.set_ylabel("Signal Value")
        ax.set_title(
            f"Continuous - {selected_signal} × {const}"
        )

        ax.grid(True, alpha=0.3)

        st.pyplot(fig)


        # Discrete

        fig, ax = plt.subplots()

        ax.stem(indices, samples)

        ax.set_xlabel("Index")
        ax.set_ylabel("Signal Value")
        ax.set_title(
            f"Discrete - {selected_signal} × {const}"
        )

        ax.grid(True, alpha=0.3)

        st.pyplot(fig)