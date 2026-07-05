from database.save_report import save_report

report_id = save_report(
    "cbc_report.pdf"
)

print(report_id)