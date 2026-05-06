# 🔐 macOS Security Audit Script

A Python script that checks your Mac's security settings and generates a report.

---

## 📋 What It Checks (6 Security Tests)

| # | Check | What It Does |
|---|-------|-------------|
| 1 | **Firewall** | Is your firewall enabled? |
| 2 | **FileVault** | Is your drive encrypted? |
| 3 | **SIP** | Are system files protected from changes? |
| 4 | **Auto-Updates** | Do you get automatic security patches? |
| 5 | **Gatekeeper** | Does your Mac check if apps are safe? |
| 6 | **Guest Account** | Is guest login disabled? |

---

## 🚀 Quick Start

**Requirements:** Python 3.6+

Check if Python is installed:
```bash
python3 --version
```

If you need to install: `brew install python3` or visit [python.org](https://www.python.org/downloads/)

**Run the script:**
```bash
cd /path/to/mac-security-audit
python3 audit.py
```

The report saves to `audit_report.txt` automatically.

---

## 📊 What You'll See

Each check shows either:
- `✅ PASS` — Security setting is enabled (good!)
- `❌ FAIL` — Security setting is disabled (needs fixing)

The script prints colored output to your terminal and saves a clean text report.

---

## ⚠️ Do I Need `sudo`?

Mostly no. The checks work without admin access. If you get permission errors, try:
```bash
sudo python3 audit.py
```

---

## 🔧 Troubleshooting

| Problem | Fix |
|---------|-----|
| `command not found: python3` | Install Python from python.org or Homebrew |
| Permission denied | Try `sudo python3 audit.py` |
| No output file | Check you can write to the folder: `touch test.txt && rm test.txt` |

---

## 📝 Notes

- This script only **checks** settings—it doesn't change anything
- The report file is clean and readable (no technical codes)
- All Python modules used are built-in (no pip install needed)

See **TESTING.md** to learn how each check works in detail.
