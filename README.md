
# Red Wine Quality Prediction Project

## Project Overview
This project is a web application built using **Python 3.11** and **PyCharm** for the backend, and **HTML** and **CSS** for the frontend. The app predicts the quality of red wine based on user-provided features.

## Prerequisites
Make sure the following software is installed on your system:
- **Python 3.11**: [Download Python 3.11](https://www.python.org/downloads/release/python-3110/)
- **PyCharm**: [Download PyCharm](https://www.jetbrains.com/pycharm/download/)

## Project Structure
```
redwineprediction/
│
├── app.py                # Main Python script for the Flask app
├── dataset/              # Directory containing dataset
│   └── winequality-red.csv
├── model/                # Directory containing the trained model file
│   └── wine_quality_model.pkl
├── static/               # Directory for static files (CSS, images, etc.)
│   └── styles.css         # CSS file for styling the frontend
├── templates/            # Directory for HTML templates
│   └── index.html        # Main HTML file for user input
├── train_model.py        # Python file to generate model
├── requirements.txt      # List of required Python packages
└── README.md             # This README file
```

## Setup Instructions

### 1. Clone or Download the Project
Download the project folder by either:
- **Cloning** the Git repository (if available):
  ```bash
  git clone https://github.com/akshaynstack/redwineprediction.git
  ```
- **Downloading** the ZIP file and extracting it to your desired location.

### 2. Open the Project in PyCharm
- Open **PyCharm** and select **Open**.
- Navigate to the project directory and open it.
- Create venv (recommended)

### 3. Install Project Dependencies
Ensure all required Python packages are installed:
```bash
pip install -r requirements.txt
```

### 4. Run the Flask App
Start the Flask server by running:
```bash
python app.py
```
The app should now be accessible at `http://127.0.0.1:5000/`.

## Usage
1. **Navigate to `http://127.0.0.1:5000/`** in your web browser.
2. Fill in the required input fields in the form.
3. Click **Predict** to get the predicted wine quality.
4. The result will be displayed as a popup modal in the center of the page.

## Technologies Used
- **Backend**: Python 3.11, Flask
- **Frontend**: HTML, CSS, TailwindCSS (via CDN)

## Customization
- **Styling**: Edit the `static/style.css` for custom styles.
- **Backend**: Modify `app.py` to include more complex logic or integrate additional features.
- **Model**: you can generate model using train_model.py with new datasets (run command - pyton train_model.py)

## Troubleshooting
- **Module Not Found Error**: Ensure that all packages listed in `requirements.txt` are installed.
- **Port Already in Use**: If the port 5000 is occupied, run the app on a different port:
  ```python
  app.run(port=5001)
  ```
---

**Note**: If you are using a different Python version, update the README accordingly.
