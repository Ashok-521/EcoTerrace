"""
Small helper to convert the combined Markdown report to PDF and DOCX using pandoc if available.
Usage:
  python scripts/convert_report.py

If pandoc is not installed, the script prints instructions.
"""
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'report' / 'COMPLETE_REPORT.md'
OUT_PDF = ROOT / 'report' / 'REROOT_Report.pdf'
OUT_DOCX = ROOT / 'report' / 'REROOT_Report.docx'

def has_pandoc():
    return shutil.which('pandoc') is not None

def convert_with_pandoc():
    cmd_pdf = [
        'pandoc', str(SRC), '-o', str(OUT_PDF), '--from', 'markdown', '--toc'
    ]
    cmd_docx = [
        'pandoc', str(SRC), '-o', str(OUT_DOCX), '--from', 'markdown', '--toc'
    ]
    print('Running:', ' '.join(cmd_pdf))
    subprocess.check_call(cmd_pdf)
    print('Running:', ' '.join(cmd_docx))
    subprocess.check_call(cmd_docx)

if __name__ == '__main__':
    if not SRC.exists():
        print('Source file not found:', SRC)
        raise SystemExit(1)
    if has_pandoc():
        try:
            convert_with_pandoc()
            print('Converted to:', OUT_PDF, OUT_DOCX)
        except subprocess.CalledProcessError as e:
            print('Pandoc failed:', e)
    else:
        print('Pandoc not found on PATH.')
        print('Install pandoc and run:')
        print('  pandoc "{}" -o "{}" --from markdown --toc'.format(SRC, OUT_PDF))
        print('  pandoc "{}" -o "{}" --from markdown --toc'.format(SRC, OUT_DOCX))
