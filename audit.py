#!/usr/bin/env python3

################################################################################
# macOS Security Audit Script (Python Version - Enhanced)
# Purpose: Audits macOS security settings with detailed descriptions
# Output: Clean readable report file (no ANSI codes), colored terminal output
# Requirements: Python 3.6+
################################################################################

import subprocess
import sys
from typing import Tuple

# Define ANSI color codes for terminal output only
RED = '\033[0;31m'
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
YELLOW = '\033[0;33m'
NC = '\033[0m'  # NC = "No Color" - resets to default terminal color

# Initialize counters for the summary
passed_checks = 0
total_checks = 6  # Updated to 6 checks (added Gatekeeper and Guest Account)

# Create or overwrite the report file
report_file = "audit_report.txt"
report_content = []  # Store all output lines to write at the end


def print_to_terminal(colored_message: str) -> None:
    """Print colored output to terminal only (not saved to file)."""
    print(colored_message)


def print_and_log(terminal_message: str, file_message: str) -> None:
    """
    Print colored message to terminal AND store plain text version to report file.
    This separates terminal output from file output to avoid ANSI codes in the saved file.
    """
    print_to_terminal(terminal_message)
    report_content.append(file_message)


def add_to_report(message: str) -> None:
    """Add a plain text message only to the report file (not terminal)."""
    report_content.append(message)


def run_command(command: str) -> Tuple[str, int]:
    """
    Execute a shell command and return its output and exit code.
    Returns both the output text and the command's success/failure status.
    """
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=True
        )
        return result.stdout.strip(), result.returncode
    except Exception as e:
        return f"Error: {str(e)}", 1


################################################################################
# REPORT HEADER
################################################################################

print_to_terminal(f"\n{BLUE}📋 macOS SECURITY AUDIT REPORT{NC}\n")
add_to_report("=" * 80)
add_to_report("macOS SECURITY AUDIT REPORT")
add_to_report("=" * 80)
add_to_report("")
add_to_report("This report checks critical macOS security settings.")
add_to_report("Each check is marked with ✅ PASS or ❌ FAIL based on current system state.")
add_to_report("")
print_to_terminal("━" * 80)

################################################################################
# CHECK 1: FIREWALL STATUS
################################################################################

add_to_report("")
add_to_report("CHECK 1: FIREWALL STATUS")
add_to_report("-" * 40)
add_to_report("What: Is your firewall turned on?")
add_to_report("Why: Your firewall stops unwanted traffic from the internet. It blocks hackers and")
add_to_report("malware from getting into your computer.")
add_to_report("")

firewall_output, _ = run_command(
    "defaults read /Library/Preferences/com.apple.alf globalstate"
)
firewall_status = firewall_output.strip() if firewall_output else "0"

if firewall_status in ["1", "2"]:
    print_and_log(
        f"{GREEN}✅ PASS{NC} — Firewall is enabled (status: {firewall_status})",
        f"✅ PASS — Firewall is enabled (status: {firewall_status})"
    )
    passed_checks += 1
else:
    print_and_log(
        f"{RED}❌ FAIL{NC} — Firewall is disabled (status: {firewall_status})",
        f"❌ FAIL — Firewall is disabled (status: {firewall_status})"
    )
    add_to_report(f"Fix: Turn on your firewall in System Preferences → Security & Privacy → Firewall")

add_to_report("")

################################################################################
# CHECK 2: FILEVAULT ENCRYPTION
################################################################################

add_to_report("")
add_to_report("CHECK 2: FILEVAULT ENCRYPTION")
add_to_report("-" * 40)
add_to_report("What: Is your hard drive encrypted?")
add_to_report("Why: Encryption scrambles your data so no one can read it if they steal your Mac.")
add_to_report("Without it, anyone could get your files, photos, and passwords.")
add_to_report("")

filevault_output, _ = run_command("fdesetup status")

if "FileVault is On" in filevault_output:
    print_and_log(
        f"{GREEN}✅ PASS{NC} — FileVault encryption is enabled",
        f"✅ PASS — FileVault encryption is enabled"
    )
    passed_checks += 1
else:
    print_and_log(
        f"{RED}❌ FAIL{NC} — FileVault encryption is disabled",
        f"❌ FAIL — FileVault encryption is disabled"
    )
    add_to_report(f"Fix: Enable in System Preferences → Security & Privacy → FileVault (takes several hours)")

add_to_report("")

################################################################################
# CHECK 3: SYSTEM INTEGRITY PROTECTION (SIP)
################################################################################

add_to_report("")
add_to_report("CHECK 3: SYSTEM INTEGRITY PROTECTION (SIP)")
add_to_report("-" * 40)
add_to_report("What: Is your system protected from file changes?")
add_to_report("Why: SIP stops anyone, even with admin access, from messing with important")
add_to_report("system files. This blocks malware and other bad stuff from breaking your Mac.")
add_to_report("")

sip_output, _ = run_command("csrutil status")

if "enabled" in sip_output:
    print_and_log(
        f"{GREEN}✅ PASS{NC} — System Integrity Protection (SIP) is enabled",
        f"✅ PASS — System Integrity Protection (SIP) is enabled"
    )
    passed_checks += 1
else:
    print_and_log(
        f"{RED}❌ FAIL{NC} — System Integrity Protection (SIP) is disabled",
        f"❌ FAIL — System Integrity Protection (SIP) is disabled"
    )
    add_to_report(f"Fix: Enable in Recovery Mode (hold Cmd+R at startup) → Terminal → csrutil enable")

add_to_report("")

################################################################################
# CHECK 4: AUTOMATIC UPDATES
################################################################################

add_to_report("")
add_to_report("CHECK 4: AUTOMATIC SECURITY UPDATES")
add_to_report("-" * 40)
add_to_report("What: Does your Mac automatically get security updates?")
add_to_report("Why: Hackers find holes in software all the time. Updates fix these holes so")
add_to_report("your Mac stays safe. Automatic updates make sure you never miss one.")
add_to_report("")

autoupdate_output, _ = run_command(
    "defaults read /Library/Preferences/com.apple.SoftwareUpdate AutomaticCheckEnabled"
)
autoupdate_status = autoupdate_output.strip() if autoupdate_output else "0"

if autoupdate_status == "1":
    print_and_log(
        f"{GREEN}✅ PASS{NC} — Automatic security updates are enabled",
        f"✅ PASS — Automatic security updates are enabled"
    )
    passed_checks += 1
else:
    print_and_log(
        f"{RED}❌ FAIL{NC} — Automatic security updates are disabled",
        f"❌ FAIL — Automatic security updates are disabled"
    )
    add_to_report(f"Fix: Turn on automatic updates in System Preferences → General → Software Update")

add_to_report("")

################################################################################
# CHECK 5: GATEKEEPER (XProtect/Malware Protection)
################################################################################

add_to_report("")
add_to_report("CHECK 5: GATEKEEPER & XPROTECT (MALWARE PROTECTION)")
add_to_report("-" * 40)
add_to_report("What: Does your Mac check if apps are safe before you run them?")
add_to_report("Why: Gatekeeper blocks suspicious apps and malware from running on your")
add_to_report("computer. It keeps track of apps that have viruses or sketchy code.")
add_to_report("")

gatekeeper_output, _ = run_command("spctl status")

if "assessments enabled" in gatekeeper_output:
    print_and_log(
        f"{GREEN}✅ PASS{NC} — Gatekeeper is enabled (applications verified)",
        f"✅ PASS — Gatekeeper is enabled (applications verified)"
    )
    passed_checks += 1
else:
    print_and_log(
        f"{RED}❌ FAIL{NC} — Gatekeeper is disabled (assessments disabled)",
        f"❌ FAIL — Gatekeeper is disabled (assessments disabled)"
    )
    add_to_report(f"Fix: Enable in System Preferences → Security & Privacy or Terminal: spctl --master-enable")

add_to_report("")

################################################################################
# CHECK 6: GUEST ACCOUNT
################################################################################

add_to_report("")
add_to_report("CHECK 6: GUEST ACCOUNT STATUS")
add_to_report("-" * 40)
add_to_report("What: Can guests log into your Mac without a password?")
add_to_report("Why: Guest accounts are for when friends or family want to use your Mac.")
add_to_report("If a guest account is on, anyone who walks up can access your files and data.")
add_to_report("")

guest_output, _ = run_command(
    "defaults read /Library/Preferences/com.apple.loginwindow GuestEnabled"
)
guest_status = guest_output.strip() if guest_output else "1"

if guest_status == "0":
    print_and_log(
        f"{GREEN}✅ PASS{NC} — Guest account is disabled",
        f"✅ PASS — Guest account is disabled"
    )
    passed_checks += 1
else:
    print_and_log(
        f"{RED}❌ FAIL{NC} — Guest account is enabled",
        f"❌ FAIL — Guest account is enabled"
    )
    add_to_report(f"Fix: Disable in System Preferences → Users & Groups → Guest Account")

add_to_report("")

################################################################################
# SUMMARY SECTION
################################################################################

add_to_report("=" * 80)
add_to_report("SUMMARY")
add_to_report("=" * 80)
add_to_report("")

print_to_terminal("\n" + "━" * 80)
print_and_log(
    f"\n📊 Summary: {GREEN}{passed_checks}{NC} out of {total_checks} checks passed\n",
    f"\n📊 SUMMARY: {passed_checks} out of {total_checks} checks passed\n"
)

# Add detailed summary to report
if passed_checks == total_checks:
    add_to_report("🎉 EXCELLENT: All security checks passed!")
    add_to_report("Your Mac has comprehensive security protections enabled.")
elif passed_checks >= 5:
    add_to_report(f"⚠️  GOOD: {passed_checks}/{total_checks} checks passed")
    add_to_report(f"  {total_checks - passed_checks} check(s) need attention.")
elif passed_checks >= 3:
    add_to_report(f"⚠️  FAIR: {passed_checks}/{total_checks} checks passed")
    add_to_report(f"  {total_checks - passed_checks} check(s) need attention.")
else:
    add_to_report(f"🚨 POOR: {passed_checks}/{total_checks} checks passed")
    add_to_report(f"  {total_checks - passed_checks} check(s) need immediate attention!")

add_to_report("")
add_to_report("Next steps:")
add_to_report("1. Review each failed check above")
add_to_report("2. Follow the recommendation for each failed check")
add_to_report("3. Re-run this audit to verify improvements: python3 audit.py")
add_to_report("")
add_to_report("=" * 80)
add_to_report("END OF REPORT")
add_to_report("=" * 80)

################################################################################
# WRITE REPORT TO FILE
################################################################################

try:
    with open(report_file, 'w') as f:
        f.write('\n'.join(report_content))
    print(f"✅ Report saved to {report_file}")
except IOError as e:
    print(f"⚠️  Warning: Could not save report to file: {e}", file=sys.stderr)

sys.exit(0)
