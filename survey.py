preferences = ["coffee", "tea", "coffee", "soda"]
counts = {}
for preference in preferences:
    if preference in counts:
        counts[preference] += 1
    else:
        counts[preference] = 1

total = len(preferences)
percentage = (counts[preference] / total) * 100
print("Total preferences:", total)
print("Preference counts:", counts)
print("Preference percentages:", percentage)