import random
random.seed(42)
customers=[]
for i in range(1,51):
    customer={
        "customer_id":f"C{i:03d}",
        "age":random.randint(18,65),
        "spending":round(random.uniform(50,2000),2),
        "visits":random.randint(1,30),
    }
    customers.append(customer)
    print('='*60)
    print("CUSTOMER SEGMENTATION ANALYSIS-DAY 17")
    print(f"\nDataset loaded:{len(customers)}customers\n")
    
    def mean (values):
        return sum(values)/len(values) if values else 0
    def stats(values):
        avg=mean(values)
        mn=min(values)
        mx=max(values)
        return avg,mn,mx
    spendings=[c["spending"]for c in customers]
    visits=[c["visits"]for c in customers]
    ages=[c["age"]for c in customers]
    avg_spend,min_spend,max_spend=stats(spendings)
    avg_visits,min_visits,max_visits=stats(visits)
    print("─── Dataset Overview ───────────────────────────────")
print(f"  Spending  → avg: ${avg_spend:.2f}  min: ${min_spend:.2f}  max: ${max_spend:.2f}")
print(f"  Visits    → avg: {avg_visits:.1f}    min: {min_visits}      max: {max_visits}")
print(f"  Age       → avg: {mean(ages):.1f}  min: {min(ages)}      max: {max(ages)}")
print()


# 3. SEGMENT CUSTOMERS  (HIGH / MEDIUM / LOW)

# Thresholds based on spending percentiles (manual)
HIGH_THRESHOLD   = avg_spend + 0.5 * (max_spend - avg_spend)   # top tier
LOW_THRESHOLD    = avg_spend - 0.5 * (avg_spend - min_spend)   # bottom tier

def spending_segment(spend):
    if spend >= HIGH_THRESHOLD:
        return "HIGH"
    elif spend >= LOW_THRESHOLD:
        return "MEDIUM"
    else:
        return "LOW"

for c in customers:
    c["segment"] = spending_segment(c["spending"])


# 4. IDENTIFY HIGH-VALUE & LOW-ENGAGEMENT

HIGH_VALUE_SPEND   = avg_spend * 1.5
LOW_ENGAGE_VISITS  = 5           # visits <= this threshold

high_value     = [c for c in customers if c["spending"] >= HIGH_VALUE_SPEND]
low_engagement = [c for c in customers if c["visits"]   <= LOW_ENGAGE_VISITS]

print("─── Segment Distribution ───────────────────────────")
for seg in ["HIGH", "MEDIUM", "LOW"]:
    group = [c for c in customers if c["segment"] == seg]
    avg_s = mean([c["spending"] for c in group])
    avg_v = mean([c["visits"]   for c in group])
    bar   = "█" * len(group)
    print(f"  {seg:<7}  {len(group):>3} customers  "
          f"avg spend ${avg_s:>7.2f}  avg visits {avg_v:>4.1f}  {bar}")
print()

print("─── High-Value Customers (spend ≥ ${:.2f}) ──────────".format(HIGH_VALUE_SPEND))
print(f"  Count: {len(high_value)}")
if high_value:
    top5 = sorted(high_value, key=lambda c: c["spending"], reverse=True)[:5]
    print("  Top 5:")
    for c in top5:
        print(f"    {c['customer_id']}  age {c['age']}  "
              f"spend ${c['spending']:.2f}  visits {c['visits']}")
print()

print("─── Low-Engagement Users (visits ≤ {}) ─────────────".format(LOW_ENGAGE_VISITS))
print(f"  Count: {len(low_engagement)}")
if low_engagement:
    sample = sorted(low_engagement, key=lambda c: c["visits"])[:5]
    print("  Sample (fewest visits):")
    for c in sample:
        print(f"    {c['customer_id']}  age {c['age']}  "
              f"spend ${c['spending']:.2f}  visits {c['visits']}")
print()


# 5. ASCII VISUALISATION

def ascii_histogram(values, bins=8, label="Value", width=40):
    mn, mx = min(values), max(values)
    step   = (mx - mn) / bins
    counts = [0] * bins
    for v in values:
        idx = min(int((v - mn) / step), bins - 1)
        counts[idx] += 1
    max_count = max(counts) or 1
    print(f"  {label} Distribution:")
    for i, cnt in enumerate(counts):
        lo  = mn + i * step
        hi  = lo + step
        bar = "▇" * int(cnt / max_count * width)
        print(f"  ${lo:>7.0f}–${hi:<7.0f} | {bar:<{width}} {cnt}")
    print()

print("─── Spending Distribution ──────────────────────────")
ascii_histogram(spendings, label="Spending ($)")

# Segment pie (ASCII)
print("─── Customer Categories (ASCII pie) ────────────────")
total = len(customers)
for seg, symbol in [("HIGH","▰"), ("MEDIUM","▱"), ("LOW","░")]:
    grp  = [c for c in customers if c["segment"] == seg]
    pct  = len(grp) / total * 100
    bar  = symbol * int(pct / 2)
    print(f"  {seg:<7} {pct:>5.1f}%  {bar}")
print()


# 6. BUSINESS STRATEGIES  (BONUS)

print("─── Business Strategies ────────────────────────────")
strategies = {
    "HIGH": [
        "Launch an exclusive VIP loyalty programme with premium perks.",
        "Offer early access to new products / limited-edition items.",
        "Assign dedicated account managers or personal shoppers.",
    ],
    "MEDIUM": [
        "Run targeted upsell campaigns (bundle deals, 'next tier' offers).",
        "Use personalised email / push with spend-milestone rewards.",
        "Introduce a referral programme to grow this segment.",
    ],
    "LOW": [
        "Send re-engagement campaigns with time-limited discount codes.",
        "Simplify the purchase journey to reduce friction.",
        "Collect feedback to understand why spending is low.",
    ],
}

for seg, tips in strategies.items():
    print(f"\n  [{seg} segment]")
    for tip in tips:
        print(f"    • {tip}")

print()
print("─── Low-Engagement Re-activation ───────────────────")
print("  • Trigger automated 'We miss you' emails after 14 days of no visit.")
print("  • Offer a free-shipping / flat-discount coupon to incentivise return.")
print("  • A/B test SMS vs email channel for best re-activation rate.")
print()
print("=" * 60)
print("  Analysis complete.  #gowaiacademy  #rftinternship")
print("=" * 60)