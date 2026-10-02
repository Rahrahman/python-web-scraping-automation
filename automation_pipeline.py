import json
from datetime import datetime
import pandas as pd

def run_automation_pipeline():
    dataset_file = "multipage_books_dataset.csv"
    print(f"Loading dataset from '{dataset_file}'...")
    df = pd.read_csv(dataset_file, encoding="utf-8")

    # 1. Analytics & Processing
    total_books = len(df)

    # Clean price column: strip currency symbols ('£') and convert to numeric float
    df["Price_Float"] = (
        df["Price"]
        .astype(str)
        .str.replace("£", "", regex=False)
        .str.strip()
        .astype(float)
    )

    avg_price = df["Price_Float"].mean()
    min_price = df["Price_Float"].min()
    max_price = df["Price_Float"].max()

    # Filter 5-star rated books
    five_star_books = df[df["Rating"] == "Five"].copy()
    five_star_count = len(five_star_books)

    # 2. Executive Summary Structure
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary = {
        "report_id": f"RPT-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "generated_at": timestamp,
        "metrics": {
            "total_books_scraped": total_books,
            "average_price": round(avg_price, 2),
            "min_price": round(min_price, 2),
            "max_price": round(max_price, 2),
            "five_star_books_count": five_star_count,
            "five_star_ratio_pct": round((five_star_count / total_books) * 100, 2) if total_books else 0.0
        },
        "top_rated_books": five_star_books[["Title", "Price", "Page_Number"]].to_dict(orient="records")
    }

    # 3. Export High-Value Items (5-star books)
    top_rated_csv = "top_rated_books.csv"
    export_cols = ["Title", "Price", "Rating", "Availability", "Page_Number"]
    five_star_books[export_cols].to_csv(top_rated_csv, index=False, encoding="utf-8")
    print(f"[+] High-value records exported to '{top_rated_csv}'.")

    # 4. Generate Email-Ready Alert Notification
    lines = [
        "=" * 60,
        "   AUTOMATED SCRAPING & DATA INTELLIGENCE REPORT",
        "=" * 60,
        f"Generated At : {timestamp}",
        f"Report ID    : {summary['report_id']}",
        f"Source File  : {dataset_file}",
        "-" * 60,
        "EXECUTIVE SUMMARY METRICS",
        "-" * 60,
        f"• Total Products Scraped : {total_books}",
        f"• Average Product Price  : £{avg_price:.2f}",
        f"• Price Range            : £{min_price:.2f} - £{max_price:.2f}",
        f"• 5-Star Rated Books     : {five_star_count} ({summary['metrics']['five_star_ratio_pct']}%)",
        "-" * 60,
        f"TOP 5-STAR RATED BOOKS ({five_star_count} items)",
        "-" * 60,
    ]

    for idx, row in enumerate(five_star_books.itertuples(), start=1):
        lines.append(f"{idx:02d}. {row.Title}")
        lines.append(f"    Price: {row.Price} | Catalog Page: {row.Page_Number} | Status: {row.Availability}")

    lines.extend([
        "-" * 60,
        "NOTIFICATION STATUS : DISPATCH READY",
        "ACTION REQUIRED     : None (Automated audit complete)",
        "=" * 60
    ])

    report_content = "\n".join(lines)
    report_file = "automated_report.txt"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report_content)

    print(f"[+] Automated notification report generated and saved to '{report_file}'.")

    # 5. Terminal Success Log
    print("\n" + "=" * 50)
    print(" PIPELINE EXECUTION SUCCESSFUL")
    print("=" * 50)
    print(f"Total Processed : {total_books} books")
    print(f"Average Price   : £{avg_price:.2f}")
    print(f"5-Star Count    : {five_star_count} books")
    print(f"Artifacts Built : {report_file}, {top_rated_csv}")
    print("=" * 50)

if __name__ == "__main__":
    run_automation_pipeline()
