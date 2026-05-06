# 🔐 macOS Security Audit Script (Python Version)

A simple, beginner-friendly Python script that checks your Mac's security settings and generates a Pass/Fail report.

---

## 📋 What This Script Checks

### 1. **Firewall** 🛡️
- **What it checks**: Is the macOS firewall enabled?
- **Why it matters**: The firewall blocks unauthorized network connections from reaching your Mac, protecting against external attacks.
- **How it works**: Uses Python's `subprocess` module to run the firewall status command. PASS if enabled (status is 1 or 2), FAIL if disabled (status is 0).

### 2. **FileVault Encryption** 🔒
- **What it checks**: Is your hard drive encrypted with FileVault?
- **Why it matters**: Encryption protects your data if someone steals your Mac or gets physical access to the drive. Without it, anyone could read your files.
- **How it works**: Runs the FileVault status command and checks if the output contains "FileVault is On". PASS if enabled, FAIL if disabled.

### 3. **System Integrity Protection (SIP)** 🔐
- **What it checks**: Is SIP (Apple's built-in security layer) enabled?
- **Why it matters**: SIP prevents even administrators from modifying critical system files, protecting against malware and system tampering.
- **How it works**: Runs the SIP status command and checks if "enabled" appears in the output. PASS if on, FAIL if off.

### 4. **Automatic Updates** 🔄
- **What it checks**: Are automatic security updates enabled?
- **Why it matters**: Security updates patch vulnerabilities. Without them, your Mac stays vulnerable to known exploits.
- **How it works**: Checks if automatic update checking is turned on (value = 1). PASS if enabled, FAIL if disabled.

---

## 🚀 How to Run the Script

### Prerequisites

This script requires **Python 3.6 or later**. Most Macs come with Python pre-installed, but let's verify:

```bash
python3 --version
```

**Expected output**: `Python 3.x.x` (where x is the version number)

If you see "command not found", Python isn't installed. You can install it via:
- **Option 1**: Download from [python.org](https://www.python.org/downloads/)
- **Option 2**: Install via Homebrew: `brew install python3`

---

### Step 1: Navigate to the Script Directory

Open Terminal and navigate to the folder containing `audit.py`:

```bash
cd /path/to/mac-security-audit
```

Replace `/path/to/mac-security-audit` with the actual path. Example:
```bash
cd ~/Documents/dailyish/mac-security-audit
```

---

### Step 2: Run the Script

```bash
python3 audit.py
```

**What does `python3 audit.py` mean?**
- `python3` = the Python interpreter (the program that understands Python code)
- `audit.py` = the name of your script file
- Python reads the file and executes the code inside it line by line

---

### Expected Output

You'll see colored output like this:

```
📋 Checking Security Settings...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ PASS — Firewall is enabled (status: 1)
✅ PASS — FileVault encryption is enabled
❌ FAIL — System Integrity Protection (SIP) is disabled
✅ PASS — Automatic security updates are enabled

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Summary: 3 out of 4 checks passed

✅ Report saved to audit_report.txt
```

---

## 💾 Output File

The script automatically saves **all output** to a file called **`audit_report.txt`** in the same folder as the script.

You can view it with:
```bash
cat audit_report.txt
```

Or open it in your text editor.

---

## ⚠️ Do I Need Administrator Privileges?

**Mostly no**, but there are some edge cases:

- ✅ **Firewall check**: Works without `sudo`
- ✅ **FileVault check**: Works without `sudo` (though you won't see full details without `sudo`)
- ✅ **SIP check**: Works without `sudo`
- ✅ **Automatic updates check**: Works without `sudo`

**However**, if the script reports permission errors, try running with `sudo`:
```bash
sudo python3 audit.py
```

⚠️ **Warning**: Be cautious when running Python scripts with `sudo`. Only do this if you trust the script (in this case, you wrote it!).

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| `command not found: python3` | Python isn't installed. Install it from python.org or via Homebrew: `brew install python3` |
| `ModuleNotFoundError` or similar import error | The script uses only Python standard library modules (subprocess, sys, typing). No pip install needed. |
| Permission denied errors | Try running with `sudo python3 audit.py` |
| Colors don't show up in output | This is normal in some terminals. The color codes are still there, just not visible. |
| `audit_report.txt` isn't created | Check that you have write permissions in the current folder: `touch test.txt && rm test.txt` |

---

## 📚 Python Concepts Used in This Script

Want to understand Python better? Here are key concepts:

- **`subprocess` module**: Allows Python to run shell commands and capture their output
- **`Tuple` type hints**: `Tuple[str, int]` means "return a tuple with a string and an integer"
- **`try/except` blocks**: Gracefully handle errors when commands fail
- **String methods**: `.strip()` removes whitespace, `in` checks for substrings
- **File I/O**: `open()` and `with` statement for safe file operations
- **ANSI color codes**: `\033[0;31m` and similar sequences colorize terminal output
- **List comprehension and joins**: `'\n'.join(report_content)` combines list items with newlines

See **TESTING.md** for hands-on ways to understand how each check works.

---

## 📝 Notes

- This script is **read-only** — it only checks settings, it doesn't change anything.
- Some checks may require admin access or specific system configuration.
- The script uses Python's `subprocess` module, which is part of the Python standard library (no pip packages needed).
- Test in **TESTING.md** to learn how to make checks PASS or FAIL intentionally.
