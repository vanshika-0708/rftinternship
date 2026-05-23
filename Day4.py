LOGS=[
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]
#Count each log type(case-insensitive)
error_count=0
info_count=-0
warning_count=0
for log in LOGS:
    first_word=log.strip().split()[0].upper()
    if first_word=="ERROR":
        error_count+=1
    elif first_word=="INFO":
        info_count+=1
    elif first_word=="WARNING":
        warning_count+=1
# Displaay counts
print("===Log Analysis Report ===")
print("ERROR:",error_count)
print("INFO:",info_count)
print("WARNING:",warning_count)
#BONUS:Find most frequent log type
counts={"ERROR":error_count,"INFO":info_count,"WARNING":warning_count}
most_frequent=max(counts,key=counts.get)
print(f"\nMost Frequent Log Type:{most_frequent}({counts[most_frequent]} occurrences)")
