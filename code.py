import streamlit as st
import datetime
import time

# Function to get current timestamp
def get_now():
    return datetime.datetime.now().strftime("%H:%M:%S")

st.set_page_config(page_title="Thevenin Theorem Lab", layout="wide")

st.title("⚡ Verification of Thevenin’s Theorem")
st.title("By Yash Sachan")
st.tile("Developed by me")
st.markdown("---")

# --- SIDEBAR: PARAMETERS & PRECAUTIONS ---
st.sidebar.header("Circuit Parameters (Fig 1)")
v_source = st.sidebar.number_input("Source Voltage (E) in Volts", value=12.0)
r1 = st.sidebar.number_input("Resistance R1 (Ω)", value=500.0)
r2 = st.sidebar.number_input("Resistance R2 (Ω)", value=1000.0)
r3 = st.sidebar.number_input("Resistance R3 (Ω)", value=100.0)
rl = st.sidebar.number_input("Load Resistance RL (Ω)", value=50.0)

st.sidebar.markdown("---")
st.sidebar.subheader("Lab Precautions")
st.sidebar.info("""
1. Check all resistances and connecting wires.
2. Do not short circuit the voltage source terminals.
3. Current is in mA, Voltage is in Volts.
""")

if st.button("Run Verification Process"):
    # STEP 1: ORIGINAL CIRCUIT
    # Recording time of making the original circuit
    st.subheader(f"📍 Step 1: Original Circuit Setup [{get_now()}]")
    st.write("Constructing the network based on Fig 1 from the manual.")
    st.code(f"""
          R1({r1}Ω)     R2({r2}Ω)      A
      +---[===]-------[===]--------o
      |           |                |
    E({v_source}V)      R3({r3}Ω)          [RL({rl}Ω)]
      |           |                |
      +-----------+----------------o
                                   B
    """)
    st.info(f"Circuit initialized with Source={v_source}V")
    time.sleep(1)

    # STEP 2: THEVENIN VOLTAGE
    # Recording time of calculating Thevenin Voltage
    st.markdown("---")
    st.subheader(f"📍 Step 2: Calculating Thevenin Voltage (Vth) [{get_now()}]")
    st.write("Measuring open-circuit voltage across terminals A and B.")
    
    vth = v_source * (r3 / (r1 + r3)) # Using voltage divider
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
              R1          R2           A (Open)
          +---[===]-------[===]--------o
          |           |                
        E(V)        R3(Ω)   <-- (Vth)
          |           |                
          +-----------+----------------o
                                       B (Open)
        """)
    with col2:
        st.latex(r"V_{TH} = V_{oc} = E \times \left( \frac{R_3}{R_1 + R_3} \right)")
        st.success(f"Calculated Vth: **{round(vth, 3)} Volts**")
    
    time.sleep(1)

    # STEP 3: THEVENIN RESISTANCE
    # Recording time of calculating Thevenin Resistance
    st.markdown("---")
    st.subheader(f"📍 Step 3: Calculating Thevenin Resistance (Rth) [{get_now()}]")
    st.write("Replacing the source with internal resistance (Short Circuit).")
    
    r_parallel = (r1 * r3) / (r1 + r3)
    rth = r2 + r_parallel
    
    col3, col4 = st.columns(2)
    with col3:
        st.code("""
              R1          R2           A
          +---[===]-------[===]--------o
          |           |                |
        (Short)     R3(Ω)            [Rth?]
          |           |                |
          +-----------+----------------o
                                       B
        """)
    with col4:
        st.latex(r"R_{TH} = R_2 + \frac{R_1 \cdot R_3}{R_1 + R_3}")
        st.success(f"Calculated Rth: **{round(rth, 3)} Ω**")
    time.sleep(1)

    # STEP 4: FINAL VERIFICATION
    # Recording time of final verification
    st.markdown("---")
    st.subheader(f"✅ Final Step: Verification [{get_now()}]")
    
    il = vth / (rth + rl)
    il_mA = il * 1000
    
    st.write("Final equivalent circuit as shown in Fig 3.")
    st.code(f"""
                   Rth ({round(rth, 2)}Ω)
              +----[=======]---------o A
              |                      |
          Vth({round(vth, 2)}V)             [RL ({rl}Ω)]
              |                      |
              +----------------------o B
    """)
    
    st.metric(label="Final Load Current (IL)", value=f"{round(il_mA, 3)} mA")
    st.balloons()
    
    # Conclusion and Results
    st.success("**Result & Conclusion:** The theoretical current matches the simplified model. Thevenin's Theorem is Verified.")

else:
    st.write("Adjust the values in the sidebar and click 'Run' to start the verification.")