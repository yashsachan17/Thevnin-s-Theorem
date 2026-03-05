# Improved Streamlit App Code

import streamlit as st
import numpy as np

st.title('Enhanced Streamlit App for Thevnin’s Theorem')

# Inputs for Thevnin's Theorem
R1 = st.number_input('Enter Resistance R1 (Ohms):', value=0.0)
R2 = st.number_input('Enter Resistance R2 (Ohms):', value=0.0)
V1 = st.number_input('Enter Voltage V1 (Volts):', value=0.0)

# Calculate Thevnin Equivalent
if st.button('Calculate Thevnin Equivalent'):  
    Rth = (R1 * R2) / (R1 + R2) if (R1 + R2) != 0 else 0  
    Vth = (R2/(R1 + R2)) * V1
    st.success(f'The Thevnin Equivalent Resistance (Rth) is: {Rth} Ohms')
    st.success(f'The Thevnin Equivalent Voltage (Vth) is: {Vth} Volts')
