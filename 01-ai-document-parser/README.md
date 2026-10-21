# AI Document Parser

## Project Overview
The AI Document Parser is a Python-based application designed to extract structured information from invoice documents, validate the extracted data, and save the results in JSON format.

This project demonstrates how Python and AI-powered document processing can reduce manual data entry and improve the efficiency of invoice processing workflows.

## Features
- Extract invoice information, including invoice number, invoice date, due date, supplier name, supplier email, and other available fields.
- Validate extracted data before saving the results.
- Generate structured JSON output.
- Handle parsing and validation errors.
- Save the extracted invoice information to an output file.

## Technologies Used
- Python
- Generative AI / AI-based extraction
- JSON
- Python exception handling
- Data validation

## Project Structure

```text
01-ai-document-parser/
├── main.py
├── requirements.txt
├── README.md
├── invoice_result.json
└── sample_invoice.pdf
```

*Note: The filenames above are examples. Keep the actual filenames used in your project.*

## Prerequisites
- Python 3.10 or a compatible version for your dependencies.
- pip package manager.
- An API key if your implementation uses an external AI service.

## Installation

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment on Windows:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Configure any required API keys using environment variables. Never commit API keys to GitHub.

## Run the Project

```bash
python main.py
```

The application processes the configured invoice and saves the extracted information to a JSON output file.

## Sample Output

```json
{
  "invoice_number": "INV-2026-001",
  "invoice_date": "2026-10-15",
  "due_date": "2026-11-14",
  "supplier_name": "ABC Technologies LLC",
  "supplier_email": "billing@abc-tech.example"
}
```

*This is an illustrative excerpt based on the sample invoice output. Your actual output may contain additional fields.*

## Learning Outcomes
- Working with Python for document processing.
- Extracting structured data from invoices.
- Validating extracted information.
- Handling errors and saving JSON output.
- Building a practical document automation solution.

## Author
Aswathy K.

## Internship
Datheon Python, Generative AI & LangChain Internship