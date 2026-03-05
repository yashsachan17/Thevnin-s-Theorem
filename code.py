"""Android-ready Kivy app to verify Thevenin, Norton, and Superposition theorems.

Run locally:
    python code.py

Package for Android (example):
    buildozer init
    # Add required dependencies in buildozer.spec: python3,kivy
    buildozer -v android debug
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

KV = """
<SectionTitle@Label>:
    size_hint_y: None
    height: "34dp"
    bold: True
    color: 0.1, 0.2, 0.5, 1

<TheoremVerifierUI>:
    orientation: "vertical"
    padding: "12dp"
    spacing: "10dp"

    ScrollView:
        do_scroll_x: False

        BoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: self.minimum_height
            spacing: "12dp"

            SectionTitle:
                text: "Thevenin Theorem (Voltage Divider Equivalent)"
            GridLayout:
                cols: 2
                size_hint_y: None
                height: self.minimum_height
                row_default_height: "42dp"
                row_force_default: True
                spacing: "6dp"

                Label:
                    text: "Source Voltage Vs (V)"
                    halign: "left"
                    text_size: self.size
                TextInput:
                    id: thevenin_vs
                    multiline: False
                    input_filter: "float"

                Label:
                    text: "R1 (Ohms)"
                    halign: "left"
                    text_size: self.size
                TextInput:
                    id: thevenin_r1
                    multiline: False
                    input_filter: "float"

                Label:
                    text: "R2 (Ohms)"
                    halign: "left"
                    text_size: self.size
                TextInput:
                    id: thevenin_r2
                    multiline: False
                    input_filter: "float"

            Button:
                text: "Verify Thevenin"
                size_hint_y: None
                height: "44dp"
                on_press: root.compute_thevenin()

            Label:
                text: root.thevenin_result
                size_hint_y: None
                height: "58dp"
                color: 0, 0.35, 0, 1

            Widget:
                size_hint_y: None
                height: "2dp"

            SectionTitle:
                text: "Norton Theorem (Converted from Thevenin)"
            GridLayout:
                cols: 2
                size_hint_y: None
                height: self.minimum_height
                row_default_height: "42dp"
                row_force_default: True
                spacing: "6dp"

                Label:
                    text: "Thevenin Voltage Vth (V)"
                    halign: "left"
                    text_size: self.size
                TextInput:
                    id: norton_vth
                    multiline: False
                    input_filter: "float"

                Label:
                    text: "Thevenin Resistance Rth (Ohms)"
                    halign: "left"
                    text_size: self.size
                TextInput:
                    id: norton_rth
                    multiline: False
                    input_filter: "float"

            Button:
                text: "Verify Norton"
                size_hint_y: None
                height: "44dp"
                on_press: root.compute_norton()

            Label:
                text: root.norton_result
                size_hint_y: None
                height: "58dp"
                color: 0, 0.35, 0, 1

            Widget:
                size_hint_y: None
                height: "2dp"

            SectionTitle:
                text: "Superposition Theorem (Two Source Contributions)"
            GridLayout:
                cols: 2
                size_hint_y: None
                height: self.minimum_height
                row_default_height: "42dp"
                row_force_default: True
                spacing: "6dp"

                Label:
                    text: "Contribution from source 1"
                    halign: "left"
                    text_size: self.size
                TextInput:
                    id: sp_v1
                    multiline: False
                    input_filter: "float"

                Label:
                    text: "Contribution from source 2"
                    halign: "left"
                    text_size: self.size
                TextInput:
                    id: sp_v2
                    multiline: False
                    input_filter: "float"

                Label:
                    text: "Measured total (optional)"
                    halign: "left"
                    text_size: self.size
                TextInput:
                    id: sp_measured
                    multiline: False
                    input_filter: "float"

            Button:
                text: "Verify Superposition"
                size_hint_y: None
                height: "44dp"
                on_press: root.compute_superposition()

            Label:
                text: root.superposition_result
                size_hint_y: None
                height: "68dp"
                color: 0, 0.35, 0, 1
"""


class TheoremVerifierUI(BoxLayout):
    thevenin_result = StringProperty("Enter values and press Verify Thevenin")
    norton_result = StringProperty("Enter values and press Verify Norton")
    superposition_result = StringProperty("Enter values and press Verify Superposition")

    @staticmethod
    def _positive_number(value: str, name: str) -> float:
        if value is None or value.strip() == "":
            raise ValueError(f"{name} is required")
        numeric = float(value)
        if numeric <= 0:
            raise ValueError(f"{name} must be > 0")
        return numeric

    @staticmethod
    def _number(value: str, name: str) -> float:
        if value is None or value.strip() == "":
            raise ValueError(f"{name} is required")
        return float(value)

    def compute_thevenin(self):
        try:
            vs = self._number(self.ids.thevenin_vs.text, "Vs")
            r1 = self._positive_number(self.ids.thevenin_r1.text, "R1")
            r2 = self._positive_number(self.ids.thevenin_r2.text, "R2")

            v_th = vs * (r2 / (r1 + r2))
            r_th = (r1 * r2) / (r1 + r2)
            self.thevenin_result = f"Vth = {v_th:.4f} V, Rth = {r_th:.4f} Ω"
        except Exception as exc:  # UI-safe error display
            self.thevenin_result = f"Error: {exc}"

    def compute_norton(self):
        try:
            v_th = self._number(self.ids.norton_vth.text, "Vth")
            r_th = self._positive_number(self.ids.norton_rth.text, "Rth")

            i_n = v_th / r_th
            self.norton_result = f"In = {i_n:.6f} A, Rn = {r_th:.4f} Ω"
        except Exception as exc:  # UI-safe error display
            self.norton_result = f"Error: {exc}"

    def compute_superposition(self):
        try:
            source_1 = self._number(self.ids.sp_v1.text, "Source 1 contribution")
            source_2 = self._number(self.ids.sp_v2.text, "Source 2 contribution")
            predicted_total = source_1 + source_2

            measured_input = self.ids.sp_measured.text.strip()
            if measured_input:
                measured_total = float(measured_input)
                error = measured_total - predicted_total
                ok = abs(error) < 1e-6
                verdict = "Verified" if ok else "Not matched"
                self.superposition_result = (
                    f"Predicted total = {predicted_total:.6f}. "
                    f"Measured = {measured_total:.6f}. "
                    f"Difference = {error:.6f} ({verdict})"
                )
            else:
                self.superposition_result = (
                    f"Predicted total output = {predicted_total:.6f}. "
                    "Enter measured total to compare."
                )
        except Exception as exc:  # UI-safe error display
            self.superposition_result = f"Error: {exc}"


class TheoremVerifierApp(App):
    title = "Circuit Theorem Verifier"

    def build(self):
        Builder.load_string(KV)
        return TheoremVerifierUI()


if __name__ == "__main__":
    TheoremVerifierApp().run()
