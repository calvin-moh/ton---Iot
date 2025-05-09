
# DeepDefend: Optimized Multi-Model Approach for Network Intrusion Detection Using Deep Learning and IoT Security

This repository contains all code artefacts, model architecture, notebooks, and a Flask web application developed for my MSc Final research project titled **"DeepDefend: Optimized Multi-Model Approach for Network Intrusion Detection Using Deep Learning and IoT Security Enhancement"** by Shahna Shahul Hameed.

---

## 📦 Project Access

All source code, datasets, trained models, and app files are available in the shared Google Drive folder below:

🔗 **[Access Full Project Folder on Google Drive](https://drive.google.com/drive/folders/1s6vDLcgATOLEcPle3C7cYpGmR1fHh38Y?usp=drive_link)**

> 📥 After downloading, place files into the appropriate folders (`/datasets/`, `/models/`, `/app/`) as needed.

---

## 🧠 Project Overview

DeepDefend is a hybrid intrusion detection system combining deep learning (CNN-LSTM) with classical ML models and Perceptual Pigeon Galvanized Optimization (PPGO). It is trained on multiple datasets, targeting the detection of various cyberattacks including DDoS, XSS, backdoors, and brute force on IoT networks.

---

## 🗂️ Repository Structure

```bash
.
├── app/                       # Flask web app with frontend & backend
│   ├── app.py
│   ├── templates/
│   ├── static/                # Contains saved model files (.pkl)
│   └── files/                 # Data summaries, test/train inputs
│
├── datasets/                 # CSV datasets (to be downloaded separately)
├── Jupyter_Code/             # All analysis notebooks
│   ├── Cyber_Intrusion.ipynb
│   ├── PPGO_IOT (1).ipynb
│   ├── TON_IOT.ipynb
│   ├── Train_Model.ipynb
│   ├── UNSW_Intrusion (1).ipynb
│   └── NSL_KDD/              # NSL-KDD files & processing
│
├── models/                   # ML model files (.pkl)
├── predictions/              # Output predictions from models
├── plots_UNSW/               # Correlation heatmaps, visualizations
└── TON_IOT/                  # Individual IoT device datasets
```

---

## 📊 Datasets Used

- **NSL-KDD**: Legacy dataset for benchmarking intrusion detection.
- **UNSW-NB15**: Modern labeled dataset for various cyberattacks.
- **ToN-IoT**: IoT-specific telemetry + attack traffic datasets.

---

## ⚙️ Technologies Used

- Python, Flask, NumPy, Pandas, Scikit-learn
- Keras/TensorFlow (for ANN, CNN-LSTM models)
- Plotly, Seaborn, Matplotlib
- Optimization: PPGO (custom)
- Git, GitHub

---

## 🚀 Running the Flask App

To launch the local web app:

```bash
cd app
pip install -r requirements.txt
python app.py
```

Then visit `http://127.0.0.1:5000/` in your browser.

---

## 🧪 Notebooks & Model Training

Each notebook in `Jupyter_Code/` corresponds to different model training pipelines or dataset applications.

Example:
- `Cyber_Intrusion.ipynb`: End-to-end deep learning pipeline
- `PPGO_IOT.ipynb`: Optimization implementation
- `UNSW_Intrusion.ipynb`: Preprocessing & model training on UNSW

---

## 📥 External Files (Required Downloads)

Some large files are hosted on Drive to avoid GitHub's 100MB limit:

📁 [Download All Resources Here (Google Drive)](https://drive.google.com/drive/folders/1s6vDLcgATOLEcPle3C7cYpGmR1fHh38Y?usp=drive_link)

Place them into:
- `/datasets/` → for .csv files
- `/models/` and `/app/static/` → for .pkl model files

---

## 📈 Results Summary

| Dataset      | Accuracy | Notes                             |
|--------------|----------|-----------------------------------|
| NSL-KDD      | 97.8%    | High recall, low false positives |
| UNSW-NB15    | 98.5%    | Best results on minority classes |
| ToN-IoT      | 78–85%   | Device-specific models evaluated |

---

## 👩‍💻 Author

**Shahna Shahul Hameed**  
MSc Artificial Intelligence, Dublin, Ireland

(shahna.s.hameed24@gmail.com)

🔗 *[LinkedIn Profile](https://www.linkedin.com/in/shahna-shahul-hameed/)* | *[GitHub Profile](https://github.com/shahna-2409)*

---

## 📄 Project Report

The full MSc research report is available for download/reference:

📘 [Download Final Thesis Report (PDF)](FINAL-REPORT.pdf)

This report explains the background, objectives, methodology, experimental results, and key findings of the DeepDefend project.


## 📄 License

Licensed under the MIT License.
