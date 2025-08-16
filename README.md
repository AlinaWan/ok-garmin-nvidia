# OK Garmin NVIDIA Commands

A small, silly script created in a few minutes that lets you use **“OK Garmin” voice commands** to trigger **NVIDIA-related actions** on your PC.

Instead of controlling a Garmin dashcam, this script listens for commands and executes keypresses for NVIDIA tasks.

## Supported Voice Commands and Key Bindings

| Voice Command               | Keypress    |
| --------------------------- | ----------- |
| OK Garmin, Video speichern  | Alt + F10   |
| OK Garmin, Aufnahme starten | Alt + F9    |
| OK Garmin, Aufnahme stoppen | Alt + F9    |
| OK Garmin, Foto machen      | Win + PrtSc |

## Usage

1. Install dependencies:

```bash
pip install SpeechRecognition pyautogui
```

2. Select your microphone by updating the `device_index` in the script.
3. Run the script:

```bash
python app.py
```

4. Speak your commands naturally, e.g.,

```
OK Garmin, Video speichern
OK Garmin, Foto machen
```

The script uses **fuzzy keyword matching** so minor mispronunciations or recognition errors will still trigger the correct action.
