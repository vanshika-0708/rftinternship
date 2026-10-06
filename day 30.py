import pandas as pd
import re
from datetime import datetime
from pathlib import Path

# Optional PDF support:
# pip install pypdf streamlit

def process_csv(file):
    df = pd.read_csv(file)

    # Calculate total amount
    if "Total_Amount" not in df.columns:
        df["Total_Amount"] = df["Unit_Price"] * df["Quantity"]

    # Convert dates
    df["Invoice_Date"] = pd.to_datetime(df["Invoice_Date"], errors="coerce")
    df["Due_Date"] = pd.to_datetime(df["Due_Date"], errors="coerce")

    # Identify overdue invoices
    today = pd.Timestamp.today().normalize()
    df["Status"] = df["Due_Date"].apply(
        lambda x: "Overdue" if pd.notna(x) and x < today else "Pending"
    )

    return df


def extract_pdf_invoice(pdf_file):
    """Extract common invoice fields from a text-based PDF."""
    try:
        from pypdf import PdfReader
    except ImportError:
        raise ImportError("Install pypdf using: pip install pypdf")

    reader = PdfReader(pdf_file)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)

    invoice = re.search(r"(?:Invoice\s*(?:No|Number|#)?)\s*[:\-]?\s*([A-Z0-9\-]+)", text, re.I)
    customer = re.search(r"(?:Customer|Bill To)\s*[:\-]?\s*(.+)", text, re.I)
    date = re.search(r"(?:Invoice Date|Date)\s*[:\-]?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})", text, re.I)

    return {
        "Invoice_Number": invoice.group(1).strip() if invoice else "",
        "Customer": customer.group(1).strip() if customer else "",
        "Invoice_Date": date.group(1).strip() if date else "",
        "Extracted_Text": text
    }


def save_report(df, output="consolidated_invoice_report.csv"):
    df.to_csv(output, index=False)
    return output


# -----------------------------
# STREAMLIT DASHBOARD
# -----------------------------
def run_dashboard():
    import streamlit as st

    st.set_page_config(page_title="Invoice Processing System", page_icon="🧾")
    st.title("🧾 Automated Invoice Processing System")
    st.write("Upload invoice CSV files or text-based PDF invoices.")

    uploaded = st.file_uploader(
        "Upload CSV or PDF",
        type=["csv", "pdf"],
        accept_multiple_files=True
    )

    if uploaded:
        reports = []

        for file in uploaded:
            if file.name.lower().endswith(".csv"):
                reports.append(process_csv(file))

            elif file.name.lower().endswith(".pdf"):
                result = extract_pdf_invoice(file)
                st.subheader(f"📄 {file.name}")
                st.json({
                    "Invoice Number": result["Invoice_Number"],
                    "Customer": result["Customer"],
                    "Invoice Date": result["Invoice_Date"]
                })

        if reports:
            final = pd.concat(reports, ignore_index=True)

            st.subheader("📊 Consolidated Invoice Report")
            st.dataframe(final)

            st.metric("Total Invoices", len(final))
            st.metric("Total Amount", f"₹{final['Total_Amount'].sum():,.2f}")
            st.metric("Overdue Invoices", (final["Status"] == "Overdue").sum())

            csv = final.to_csv(index=False).encode("utf-8")
            st.download_button(
                "⬇️ Download Consolidated Report",
                csv,
                "consolidated_invoice_report.csv",
                "text/csv"
            )


if __name__ == "__main__":
    # For normal Python execution:
    # python invoice_processor.py
    #
    # For Streamlit:
    # streamlit run invoice_processor.py
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--dashboard":
        run_dashboard()
    else:
        df = process_csv("sample_invoices.csv")
        output = save_report(df)
        print("\n✅ Invoice processing completed!")
        print(f"📄 Report saved as: {output}")
        print(f"💰 Total invoice amount: ₹{df['Total_Amount'].sum():,.2f}")
        print(f"⚠️ Overdue invoices: {(df['Status'] == 'Overdue').sum()}")
        print("\n📊 Consolidated Report:")
        print(df)