preferences = ["coffee", "tea", "coffee", "soda"]
counts = {}
for preference in preferences:
    if preference in counts:
        counts[preference] += 1
    else:
        counts[preference] = 1

total = len(preferences)
print("Total preferences:", total)
print("Preference counts:", counts)
for item in counts:
    percentage = (counts[item] / total) * 100
    print(f"{item}: {percentage:.0f}%")