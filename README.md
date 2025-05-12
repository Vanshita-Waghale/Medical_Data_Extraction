# OCR-based Medical Data Extraction Project

## Overview

This project was developed as part of the CodeBasics Python course. The goal is to create an automated system that extracts important data from medical documents like prescriptions and patient details using OCR (Optical Character Recognition). By using Python and various libraries, this project helps streamline the data extraction process for health insurance companies, reducing manual work and error rates, and improving efficiency.

The OCR-based data extraction is specifically designed to help insurance companies process medical documents more efficiently, especially when there is a large volume of files to be processed, such as during the pandemic.

### Problem Statement

Health insurance companies must follow strict government regulations to issue claims, which requires processing images of patient details and prescriptions. Traditionally, these images are manually processed by outsourcing companies like “Mr. X Data Analytics” to extract useful data. However, this process is slow, error-prone, and cannot keep up with high volumes.

### Solution Approach

The solution is to automate the extraction of data from medical images using Python libraries like `pytesseract`, `opencv`, and `regex`. This approach reduces human intervention and speeds up the process, ensuring that the extracted data is accurate and ready for review and submission.

While the system automates extraction, a human is still involved to verify and correct any potential errors.

## Technologies Used

* **Python**: The main programming language used for the implementation.
* **pytesseract**: A Python wrapper for Google's Tesseract-OCR engine used to extract text from images.
* **opencv**: Used for image preprocessing to improve the quality of the text extraction.
* **pdf2image**: Converts PDF files into images to be processed by OCR.
* **Regular Expressions (regex)**: Used to filter and extract specific patterns from the OCR data.
* **pytest**: For test-driven development (TDD), used to write tests for the functionality.
* **FastAPI**: For hosting the backend service to handle OCR requests.
* **Postman**: Used to test HTTP requests to the backend service.

## Project Features

* **PDF to Image Conversion**: The project starts by converting PDF medical documents into images.
* **Image Preprocessing**: We apply preprocessing techniques (e.g., adaptive thresholding) to enhance image quality for better OCR results.
* **Data Extraction**: Once the images are processed, `pytesseract` extracts relevant data from the images.
* **Regex Pattern Matching**: Regex is used to extract specific data such as doctor names, patient details, medication information, etc.
* **Test-driven Development (TDD)**: The project was built using TDD principles to ensure high-quality code with automated tests.
* **Backend with FastAPI**: The OCR extraction functionality is exposed via a FastAPI backend.

## Installation Guide

Follow these steps to install and run the project on your local system.

### Prerequisites

Ensure that you have Python 3.x installed. You can download it from [here](https://www.python.org/downloads/).

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/OCR-Medical-Data-Extraction.git
```

Navigate to the project folder:

```bash
cd OCR-Medical-Data-Extraction
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)

Create a virtual environment to isolate the dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

* On Windows:

  ```bash
  .\venv\Scripts\activate
  ```
* On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies

Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

Make sure `requirements.txt` includes libraries like `opencv-python`, `pytesseract`, `pdf2image`, `fastapi`, `pytest`, and `regex`.

### Step 4: Install Tesseract OCR

You need to install Tesseract OCR on your system:

* **Windows**: Download the installer from [here](https://github.com/UB-Mannheim/tesseract/wiki).
* **macOS**: Install it using Homebrew:

  ```bash
  brew install tesseract
  ```
* **Linux**: Use your package manager to install it:

  ```bash
  sudo apt-get install tesseract-ocr
  ```

### Step 5: Running the Application

To run the FastAPI server, execute the following command:

```bash
uvicorn main:app --reload
```

This will start the backend server, and you can interact with it by making HTTP requests. The server should be running at `http://127.0.0.1:8000`.

### Step 6: Testing the Application

Use **Postman** to test the server and send HTTP requests to extract data from medical images.

* Set the request type to `POST` and upload the image file (patient details or prescription).
* The backend will process the image and return the extracted data.

Alternatively, you can use **pytest** to run tests:

```bash
pytest
```

### Step 7: Verify Output

Once the data is extracted, verify the results for accuracy. If there are any issues, the extracted data will be flagged for manual review.

## Workflow Diagram

1. **Upload Image** → **PDF to Image Conversion** → **Image Preprocessing** → **OCR Extraction** → **Data Extraction Using Regex** → **Return Extracted Data**

## Results

This project successfully automates the data extraction process, saving time and reducing errors. The results can be integrated into existing workflows for improved efficiency and faster turnaround times for insurance companies.

## Benefits

* **Time-saving**: Reduces the manual effort of typing data by automating extraction.
* **Cost-effective**: Lowers operational costs by minimizing the need for human intervention.
* **Accurate**: Less prone to errors compared to manual data entry.
* **Scalable**: Can handle large volumes of documents, improving productivity during peak seasons.

## Conclusion

The OCR-based Medical Data Extraction project is a powerful solution to streamline the processing of medical documents. By combining OCR, image processing, and regular expressions, this system can automatically extract valuable data from prescriptions and patient details, saving time and resources for healthcare insurance companies.

---
