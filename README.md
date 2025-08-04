# Streamlit Keypress

A Streamlit component that captures keyboard events in your Streamlit app.

## Installation

```bash
pip install streamlit-keypress
```

## Usage

```python
import streamlit as st
from streamlit_keypress import key_press_events

st.title("Keyboard Event Listener")

for key in key_press_events():
    st.write(f"You pressed: {key}")
```

### Handling navigation with arrow keys

`key_press_events` returns a queue of keys pressed since the last rerun, letting
you react to each key exactly once and safely trigger `st.rerun()` for
navigation:

```python
keys = key_press_events()
for key in keys:
    if key in ["ArrowLeft", "Left"]:
        progress(-1)
    elif key in ["ArrowRight", "Right"]:
        progress(1)
if keys:
    st.rerun()
```


![Demo Usage](docs/image.png)

## Features

- Captures keyboard events throughout your Streamlit app
- Returns a list of keys pressed since the last rerun
- Simple and lightweight

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
