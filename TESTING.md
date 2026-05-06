# 🧪 TESTING.md (Python Version) — How to Verify the Audit Script Works

This guide teaches you how to **test the Python audit script** and understand what happens when checks pass or fail.

---

## 🎯 Test 1: Run the Script and See Real Results

### Step 1: Open Terminal

- Press `Cmd + Space` (Spotlight)
- Type "Terminal" and press Enter
- This opens the Terminal application

### Step 2: Navigate to the script folder

```bash
cd ~/Documents/dailyish/mac-security-audit
```

Replace the path if your script is in a different location.

### Step 3: Run the Python script

```bash
python3 audit.py
```

### Step 4: Check the output file

```bash
cat audit_report.txt
```

**What you'll see**: Your Mac's actual security status. If a check is green (✅ PASS), that setting is configured correctly. If it's red (❌ FAIL), that setting needs attention.

---

## 🔍 Test 2: Understanding Each Check (Intermediate)

This test teaches you how each security setting works by running the underlying commands manually in Terminal.

### Check 1: Firewall Status

Run this command in Terminal:
```bash
defaults read /Library/Preferences/com.apple.alf globalstate
```

**Expected output**: `1` or `2` (PASS) or `0` (FAIL)

**What this means**:
- `1` or `2` = Firewall is ON ✅
- `0` = Firewall is OFF ❌

**To toggle firewall** (requires System Preferences):
1. Go to System Preferences → Security & Privacy → Firewall
2. Click "Turn On Firewall" or "Turn Off Firewall"
3. Run the command again to see the value change

---

### Check 2: FileVault Encryption

Run this command:
```bash
fdesetup status
```

**Expected output examples**:
- `FileVault is On.` ✅ (PASS)
- `FileVault is Off.` ❌ (FAIL)

**What this means**: If it says "FileVault is On", your drive is encrypted.

**To enable FileVault** (requires admin access):
1. Go to System Preferences → Security & Privacy → FileVault
2. Click "Turn On FileVault"
3. Restart your Mac
4. Once it completes, run the command again

⚠️ **Warning**: Enabling FileVault takes several hours or days depending on drive size.

---

### Check 3: System Integrity Protection (SIP)

Run this command:
```bash
csrutil status
```

**Expected output examples**:
- `System Integrity Protection status: enabled.` ✅ (PASS)
- `System Integrity Protection status: disabled.` ❌ (FAIL)

**What this means**: SIP is macOS's built-in protection layer that prevents unauthorized changes to system files.

**To toggle SIP** (advanced):
1. Restart your Mac in Recovery Mode: Hold **Cmd + R** while restarting
2. Open Terminal from Utilities menu
3. Run `csrutil disable` (to disable) or `csrutil enable` (to enable)
4. Restart normally
5. Run the command again to verify

⚠️ **Advanced Only**: Most users should keep SIP enabled.

---

### Check 4: Automatic Updates

Run this command:
```bash
defaults read /Library/Preferences/com.apple.SoftwareUpdate AutomaticCheckEnabled
```

**Expected output**: `1` (PASS) or `0` (FAIL)

**What this means**:
- `1` = Automatic checking is ON ✅
- `0` = Automatic checking is OFF ❌

**To toggle automatic updates** (System Preferences):
1. Go to System Preferences → General → Software Update
2. Check or uncheck "Automatically keep my Mac up to date"
3. Run the command again to see the value change

---

## 📊 Test 3: Run the Full Script Multiple Times

Run the script, change a setting, and run again:

```bash
# First run - see current state
python3 audit.py

# Change a setting (e.g., toggle Firewall in System Preferences)

# Second run - see how the result changed
python3 audit.py

# Compare reports
diff <(cat audit_report.txt) <(python3 audit.py > /dev/null && cat audit_report.txt)
```

**What to expect**: The second report reflects your system's updated state.

---

## 🧬 Test 4: Understanding the Python Code (For Learning)

Open `audit.py` in your text editor and look at the structure:

```python
# This function runs a shell command and returns its output
firewall_output, firewall_code = run_command(
    "defaults read /Library/Preferences/com.apple.alf globalstate"
)

# This line makes a decision (if output is "1" OR "2", PASS; otherwise FAIL)
if firewall_status in ["1", "2"]:
    print_and_log(f"{GREEN}✅ PASS{NC} — Firewall is enabled (status: {firewall_status})")
    passed_checks += 1
else:
    print_and_log(f"{RED}❌ FAIL{NC} — Firewall is disabled...")
```

**Key Python concepts**:

| Concept | Explanation |
|---------|-------------|
| `subprocess.run()` | Executes a shell command from Python |
| `capture_output=True` | Tells Python to capture what the command outputs |
| `text=True` | Returns output as readable text (not binary) |
| `in ["1", "2"]` | Checks if the value is in a list |
| `f"{GREEN}✅ PASS{NC}"` | f-string for string formatting with variables |
| `passed_checks += 1` | Increment counter by 1 |

---

## 🧪 Test 5: Step Through the Code in Your Head

This is a valuable learning exercise! Read through `audit.py` and trace what happens:

1. **Lines 1-20**: Import modules and set up color codes
2. **Lines 23-27**: Define the `run_command()` function
3. **Lines 30-50**: Check Firewall (run command, check if 1 or 2, print result)
4. **Lines 53-60**: Check FileVault (run command, check if "FileVault is On" in output)
5. **Lines 63-70**: Check SIP (run command, check if "enabled" in output)
6. **Lines 73-80**: Check Automatic Updates (run command, check if 1)
7. **Lines 83-90**: Print summary
8. **Lines 93-102**: Write report file

---

## 🎓 Test 6: Debugging (If Something Goes Wrong)

### The script shows an error

If you see an error like:
```
FileNotFoundError: [Errno 2] No such file or directory
```

**Possible causes**:
1. You're in the wrong directory (script isn't in current folder)
2. Python path is wrong

**Solution**:
```bash
pwd  # Shows current directory
ls   # Lists files - should show audit.py
```

### The output file isn't created

**Check**: Do you have write permissions?
```bash
touch test.txt  # Try creating a test file
rm test.txt     # Remove it
```

If `touch` fails, the script can't write the report file either.

### Colors aren't showing up

**Expected**: Color codes appear correctly in modern terminals.

**To force colors**: Most terminals support colors by default. If not, you can update the code to use a library like `colorama` (optional).

---

## ✅ Verification Checklist

Use this checklist to verify the Python script works correctly:

- [ ] Python 3 is installed: `python3 --version`
- [ ] Script runs without errors: `python3 audit.py`
- [ ] Output shows 4 security checks (Firewall, FileVault, SIP, Updates)
- [ ] Each check shows ✅ PASS or ❌ FAIL
- [ ] Summary line shows "X out of 4 checks passed"
- [ ] File `audit_report.txt` is created
- [ ] Colors appear in terminal output (green for PASS, red for FAIL)
- [ ] Running the script twice produces consistent results
- [ ] Changing a security setting changes the result on next run

---

## 🚀 Next Steps

Once you're comfortable with how the script works:

1. **Understand subprocess**: Modify the script to run different commands
2. **Add a new check**: Can you add a check for something else?
3. **Use error handling**: Wrap commands in try/except blocks
4. **Read the full code**: Open `audit.py` and read every line
5. **Extend the script**: Add more security checks or output formats

---

## 💡 Common Questions

**Q: Do I need to run it as `sudo` every time?**  
A: Only if you get permission errors. Most checks work without `sudo`.

**Q: Why are there weird characters like `[0;31m` in the output file?**  
A: Those are ANSI color codes. They tell terminals to display colored text. Text editors might show them as visible characters.

**Q: Can I run this on Windows or Linux?**  
A: No, this script is macOS-specific because it uses macOS commands (`defaults`, `fdesetup`, `csrutil`). However, the Python concepts work on any OS.

**Q: What if a check always fails even though I enabled the setting?**  
A: You might need to restart your Mac or log out and log back in for the system to register the change.

**Q: Can I modify the script?**  
A: Yes! Once you understand the code, try changing colors, adding checks, or modifying output format.
