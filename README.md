# Thevenin / Norton / Superposition Android App (Kivy)

This repository now contains a Python + Kivy app that can be packaged as an Android app.

## Features
- Verify **Thevenin theorem** for a simple voltage divider network.
- Verify **Norton theorem** from Thevenin values (`In = Vth / Rth`).
- Verify **Superposition theorem** by summing source contributions and optionally comparing with measured output.

## Run locally
```bash
python code.py
```

## Build Android APK (Buildozer)
1. Install Buildozer and Android build dependencies.
2. Initialize:
   ```bash
   buildozer init
   ```
3. In `buildozer.spec`, set at least:
   - `requirements = python3,kivy`
   - `package.name = theoremverifier`
4. Build debug APK:
   ```bash
   buildozer -v android debug
   ```

The generated APK can be installed on an Android device for use as a theorem verification tool.
