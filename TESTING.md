# 🧪 Testing the Security Audit Script

Learn how the script works by manually running each security check.

---

## Quick Test: Run It

```bash
python3 audit.py
```

View the report:
```bash
cat audit_report.txt
```

---

## Test Each Check Manually

### 1. Firewall Status
```bash
defaults read /Library/Preferences/com.apple.alf globalstate
```
**Result:** `1` or `2` = PASS (enabled), `0` = FAIL (disabled)

**To toggle:** System Preferences → Security & Privacy → Firewall

---

### 2. FileVault Encryption
```bash
fdesetup status
```
**Result:** "FileVault is On" = PASS, "FileVault is Off" = FAIL

**To enable:** System Preferences → Security & Privacy → FileVault
*(Note: Takes several hours)*

---

### 3. System Integrity Protection (SIP)
```bash
csrutil status
```
**Result:** "enabled" = PASS, "disabled" = FAIL

**To toggle:** Recovery Mode (Cmd+R on startup) → Terminal → `csrutil enable` or `csrutil disable`

---

### 4. Automatic Updates
```bash
defaults read /Library/Preferences/com.apple.SoftwareUpdate AutomaticCheckEnabled
```
**Result:** `1` = PASS (enabled), `0` = FAIL (disabled)

**To toggle:** System Preferences → General → Software Update

---

### 5. Gatekeeper (Malware Protection)
```bash
spctl status
```
**Result:** "assessments enabled" = PASS, "assessments disabled" = FAIL

**To enable:** System Preferences → Security & Privacy or Terminal: `spctl --master-enable`

---

### 6. Guest Account Status
```bash
defaults read /Library/Preferences/com.apple.loginwindow GuestEnabled
```
**Result:** `0` = PASS (disabled), `1` = FAIL (enabled)

**To toggle:** System Preferences → Users & Groups → Guest Account

---

## Experiment: Change a Setting and Re-run

1. Pick one security setting above
2. Change it in System Preferences
3. Run `python3 audit.py` again
4. See how the result changed

This is the best way to understand what each check does!

---

## Understanding the Code

The script uses Python's `subprocess` module to run shell commands and check their output. Here's the pattern:

```python
# Run a command and get the result
firewall_status, return_code = run_command("defaults read ...")

# Check if it passed or failed
if firewall_status in ["1", "2"]:
    print("✅ PASS")
else:
    print("❌ FAIL")
```

Each check follows this same pattern: run a command, check the output, print the result.

---

## Troubleshooting

**Command not found:** Make sure you're on macOS (these commands are macOS-specific)

**Permission denied:** Add `sudo` at the start of the command

**Different output than expected:** Some macOS versions have slightly different outputs. The script handles these variations.

---