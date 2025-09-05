# 🍽️ Sangi Manki Hotel — Vadivelu Special

A simple Streamlit app that simulates ordering from a small local "Sangi Manki Hotel" with Vadivelu-style dialogues and GIF reactions. This repository contains a single Python script (`app.py`) that displays a menu, accepts the user's money and order selection, and shows a success or failure GIF depending on whether the user has enough money.

---

## Features

* Simple, friendly UI built with Streamlit.
* Local-first GIF display (shows GIFs from the app folder if present).
* Menu with prices and random Vadivelu dialogues for success/failure.
* Easy to run locally or deploy on Streamlit Cloud.

---

## Files

* `app.py` — Main Streamlit application (the code you provided).
* `vadivelu_success.gif` — (optional) Local GIF shown on successful order.
* `vadivelu_fail.gif` — (optional) Local GIF shown on failed order.

> **Note:** GIF files are optional. If they are not present, the app will still work — but will not show the GIFs. For best results, use small GIFs (\~200–800 KB).

---

## Prerequisites

* Python 3.8+ (recommended)
* `pip` package manager

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/sangi-manki-hotel.git
cd sangi-manki-hotel
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install streamlit
```

---

## Usage

Run the Streamlit app locally:

```bash
streamlit run app.py
```

This opens the app in your default browser (usually at `http://localhost:8501`).

### How it works

* Enter the amount of money you have in the input field.
* Pick an item from the menu.
* Click **Place Order**.
* If you have enough money, a success message and the success GIF (if present) will appear.
* If you don't have enough money, an error message with the shortage amount and the fail GIF (if present) will appear.

---

## Configuration

You can customize:

* Menu items and prices in the `menu` dictionary at the top of `app.py`.
* Success/failure dialogues in the `success_dialogues` and `fail_dialogues` lists.
* Local GIF filenames by editing `LOCAL_SUCCESS_GIF` and `LOCAL_FAIL_GIF` variables.

---

## Deploying to Streamlit Community Cloud

1. Push your repo to GitHub.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io) and sign in.
3. Create a new app and point it to your GitHub repository and branch.
4. Set the main file to `app.py` and deploy.

If GIFs are used, make sure they are included in the repo (in the same folder as `app.py`).

---

## Example `app.py`

> The repository already includes the full `app.py` implementation. Below is a short excerpt of the main behaviour:

```python
# Example excerpt
if st.button("Place Order"):
    price = menu[item]
    if money >= price:
        st.success(f"Vadivelu: {random.choice(success_dialogues)}")
        show_gif(LOCAL_SUCCESS_GIF, caption="Victory!")
    else:
        shortage = price - money
        st.error(f"Vadivelu: {random.choice(fail_dialogues)}  (Short by Rs.{shortage})")
        show_gif(LOCAL_FAIL_GIF, caption="Ouch!")
```

---

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to:

* Add more menu items or dialogues
* Improve the UI/UX
* Add unit tests or CI

---

## License

This project is provided under the MIT License. See `LICENSE` file for details.

---

## Author

Created by Ragu — feel free to customize and share. 😄
