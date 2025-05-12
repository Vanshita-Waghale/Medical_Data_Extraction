# 🏥 OCR-based Medical Data Extraction Project

> 🔧 Built as part of the **Codebasics Bootcamp** Python course.
> 📚 Inspired by and implemented using lessons from the [Codebasics Python course](https://codebasics.io) — check it out if you're interested in learning by building real-world projects.

---

## 📌 Problem Statement

Insurance companies receive **medical prescriptions and patient documents** in scanned format (images/PDFs). Extracting information manually from these documents is time-consuming, error-prone, and not scalable—especially during peak periods like pandemics.

A company like “Mr. X Data Analytics” processes this data manually, but they’re now looking to upgrade to a **semi-automated software system** to boost productivity and accuracy.

---

## ✅ Solution Overview

This project automates the **OCR-based data extraction** from patient and prescription documents using Python and tools like **Tesseract OCR**, **OpenCV**, **Regex**, and **FastAPI**.

Instead of typing data manually:

* 🧠 The system **extracts text** from images
* 🔍 Cleans and **filters it using Regex**
* 🧪 Validates with test cases
* 🚀 Runs on a FastAPI server
* 👨‍⚕️ A human only **reviews** and submits the corrected output

---

## 🔧 Technologies Used

| Tool / Library | Purpose                                |
| -------------- | -------------------------------------- |
| Python         | Core programming language              |
| OpenCV         | Image preprocessing                    |
| Pytesseract    | OCR - Optical Character Recognition    |
| PDF2Image      | Converts PDFs to images                |
| Regex          | Pattern matching & data extraction     |
| Pytest         | Unit testing (Test-Driven Development) |
| FastAPI        | API backend server                     |
| Postman        | Testing HTTP endpoints                 |

---

## ⚙️ Detailed Workflow Steps

### 1. 📥 PDF to Image Conversion

* Used **`pdf2image`** library to convert PDF files (like prescriptions or reports) into image format.
* This is required because **Tesseract works on images**, not PDFs.

### 2. 🖼️ Raw OCR (Without Preprocessing)

* Applied **pytesseract** on the raw images.
* However, due to shadows, fonts, and formatting, **raw extraction was inaccurate**.

Example (without preprocessing):

```
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222
```

### 3. 🧹 Image Preprocessing using OpenCV

* Implemented **adaptive thresholding** with OpenCV:

  * Divides image into regions and applies different thresholds.
  * Removes shadows and improves contrast.
* Resulted in **much cleaner image** and **better OCR results**.

Example (after preprocessing):

```
Prednisone, Taper 5 mg every 3 days
Lialda - take 2 pill every day for 1 month
```

### 4. 🔎 Extracting Specific Data Using Regex

* Built **custom regex patterns** to extract:

  * Doctor name
  * Patient name and address
  * Date
  * Medicines and instructions
* Patterns designed based on standard formats in medical docs.

> ✅ Tip: Used [regex101.com](https://regex101.com/) to build and test patterns interactively.

### 5. 🧪 Testing with Pytest (TDD)

* Used **pytest** for test-driven development.
* Wrote unit tests for:

  * Regex extractors
  * OCR output cleanup
  * API response validation

### 6. 🚀 FastAPI Backend

* Hosted the logic using **FastAPI** for quick and scalable API serving.
* Features:

  * Auto Swagger docs
  * Input validation using Pydantic
  * Runs with `uvicorn` for development

### 7. 📬 Testing API with Postman

* No frontend UI is built.
* Used **Postman** to:

  * Send image/PDF files as HTTP POST requests
  * View extracted output in JSON
  * Validate and iterate over endpoint behavior

---

## 📥 How to Install and Run the Project

### ✅ Prerequisites

* Python 3.7+
* [Tesseract OCR Installed](https://github.com/tesseract-ocr/tesseract)
* Git
* Postman (for API testing)

---

### 🔧 Step-by-Step Installation Guide

#### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/OCR-Medical-Data-Extraction.git
cd OCR-Medical-Data-Extraction
```

#### Step 2: Set Up Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure the following are in `requirements.txt`:

```txt
opencv-python
pytesseract
pdf2image
regex
fastapi
uvicorn
pytest
```

#### Step 4: Install Tesseract OCR Engine

* **Windows**: [Download here](https://github.com/UB-Mannheim/tesseract/wiki)
* **macOS**:

  ```bash
  brew install tesseract
  ```
* **Linux**:

  ```bash
  sudo apt-get install tesseract-ocr
  ```

Make sure the OCR engine path is correctly set in your code or environment variable.

#### Step 5: Run the FastAPI Server

```bash
uvicorn main:app --reload
```

API will be hosted at:
📍 `http://127.0.0.1:8000`
📘 Docs available at:
📍 `http://127.0.0.1:8000/docs`

#### Step 6: Test Using Postman

* Method: `POST`
* URL: `http://127.0.0.1:8000/extract`
* Upload image or PDF file
* View extracted data in response

#### Step 7: Run Tests (Optional)

```bash
pytest
```

---

## 📊 Results

* Accurate data extraction from both prescription and patient detail documents.
* Significant improvement in OCR accuracy after preprocessing.
* Regex-based filtering ensures only **relevant medical data** is captured.

---

## 📈 Benefits

✅ Saves 30+ seconds per document
✅ Increases throughput without increasing workforce
✅ Reduces errors due to manual typing
✅ Seamlessly integrates with existing legacy software
✅ Human-in-the-loop ensures high data quality

---

## 📦 Project Structure

```
OCR-Medical-Data-Extraction/
│
├── main.py                  # FastAPI app
├── processor/
│   ├── image_converter.py   # PDF to image logic
│   ├── preprocessor.py      # Image thresholding and cleanup
│   ├── extractor.py         # Tesseract + Regex logic
│
├── tests/
│   ├── test_extraction.py   # Pytest cases
│
├── requirements.txt
├── README.md
```

---

## 🧠 About

A backend project to automate data extraction from medical prescriptions and documents using OCR and pattern recognition.

> Built with ❤️ during the **Codebasics Bootcamp Python Course**

---

