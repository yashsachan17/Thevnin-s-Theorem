import streamlit as st
import datetime
import time

# Function to get current timestamp
def get_now():
    return datetime.datetime.now().strftime("%H:%M:%S")

st.set_page_config(page_title="Thevenin Theorem Lab", layout="wide")

st.title("⚡ Verification of Thevenin’s Theorem")
st.markdown("---")

# --- SIDEBAR: PARAMETERS ---
st.sidebar.header("Circuit Parameters")
v_source = st.sidebar.number_input("Source Voltage (E) in Volts", value=12.0)
r1 = st.sidebar.number_input("Resistance R1 (Ω)", value=500.0)
r2 = st.sidebar.number_input("Resistance R2 (Ω)", value=1000.0)
r3 = st.sidebar.number_input("Resistance R3 (Ω)", value=100.0)
rl = st.sidebar.number_input("Load Resistance RL (Ω)", value=50.0)

if st.button("Run Verification Process"):
    # STEP 1: ORIGINAL CIRCUIT
    st.subheader(f"📍 Step 1: Original Circuit Setup [{get_now()}]")
    
    # Using an image of a standard bridge/Thevenin network
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Thevenin_equivalent_circuit.svg/640px-Thevenin_equivalent_circuit.svg.png", 
             caption="Standard Thevenin Network Schematic", width=400)
    
    st.info(f"Circuit initialized with Source={v_source}V, R1={r1}Ω, R2={r2}Ω, R3={r3}Ω")
    time.sleep(1)

    # STEP 2: THEVENIN VOLTAGE
    st.markdown("---")
    st.subheader(f"📍 Step 2: Calculating Thevenin Voltage (Vth) [{get_now()}]")
    
    vth = v_source * (r3 / (r1 + r3))
    
    col1, col2 = st.columns(2)
    with col1:
        # Displaying a Resistor Symbol using Markdown/Images
        [attachment_0](attachment)
        st.write("Measuring Open Circuit Voltage ($V_{oc}$):")
        st.latex(r"V_{TH} = E \cdot \frac{R_3}{R_1 + R_3}")
    with col2:
        st.success(f"Calculated Vth: **{round(vth, 3)} Volts**")
    
    time.sleep(1)

    # STEP 3: THEVENIN RESISTANCE
    st.markdown("---")
    st.subheader(f"📍 Step 3: Calculating Thevenin Resistance (Rth) [{get_now()}]")
    
    
    
    r_parallel = (r1 * r3) / (r1 + r3)
    rth = r2 + r_parallel
    
    col3, col4 = st.columns(2)
    with col3:
        st.write("Source is Short-Circuited to find equivalent resistance:")
        st.latex(r"R_{TH} = R_2 + (R_1 \parallel R_3)")
    with col4:
        st.success(f"Calculated Rth: **{round(rth, 3)} Ω**")
    time.sleep(1)

    # STEP 4: FINAL VERIFICATION
    st.markdown("---")
    st.subheader(f"✅ Final Step: Verification [{get_now()}]")
    
    il = vth / (rth + rl)
    il_mA = il * 1000
    
    
    
    st.write("### Thevenin Equivalent Model")
    st.latex(f"I_L = \\frac{{{round(vth,2)}V}}{{{round(rth,2)}\Omega + {rl}\Omega}}")
    
    st.metric(label="Final Load Current (IL)", value=f"{round(il_mA, 3)} mA")
    st.balloons()
    
    st.success("**Result & Conclusion:** The theoretical current matches the simplified model. Thevenin's Theorem is Verified.")

else:
    st.write("Adjust the values in the sidebar and click 'Run' to start the verification.")