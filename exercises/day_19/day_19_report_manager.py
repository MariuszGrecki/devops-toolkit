from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
reports_dir = BASE_DIR / "output" / "reports"

reports_dir.mkdir(parents=True, exist_ok=True)

report_file = reports_dir / "health_report.txt"

report = (
    "=== INFRASTRUCTURE HEALTH REPORT ===\n"
    "api-production: HEALTHY\n"
    "worker-01: WARNING\n"
    "database-01: CRITICAL\n"
)

report_file.write_text(report, encoding="utf-8")

content = report_file.read_text(encoding="utf-8")

print(content)