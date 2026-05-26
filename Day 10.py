# 1. GIVEN LOGS
logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

# 2. COUNT ERROR, INFO, WARNING
error_count = 0
info_count = 0
warning_count = 0

for log in logs:
    log_upper = log.upper()
    if "ERROR" in log_upper:
        error_count += 1
    elif "INFO" in log_upper:
        info_count += 1
    elif "WARNING" in log_upper:
        warning_count += 1

print("--- LOG ANALYSIS ---")
print("ERROR count  :", error_count)
print("INFO count   :", info_count)
print("WARNING count:", warning_count)

# BONUS - FIND MOST FREQUENT LOG TYPE
counts = {
    "ERROR": error_count,
    "INFO": info_count,
    "WARNING": warning_count
}

most_frequent = max(counts, key=counts.get)
print("\nMost Frequent Log Type:", most_frequent)

# BONUS - IGNORE CASE SENSITIVITY (already handled with .upper())
print("\n--- CASE INSENSITIVE TEST ---")
test_logs = [
    "error disk full",
    "Info Started",
    "WARNING memory low",
    "ERROR file missing"
]

e = 0
i = 0
w = 0

for log in test_logs:
    log_upper = log.upper()
    if "ERROR" in log_upper:
        e += 1
    elif "INFO" in log_upper:
        i += 1
    elif "WARNING" in log_upper:
        w += 1

print("ERROR  :", e)
print("INFO   :", i)
print("WARNING:", w)