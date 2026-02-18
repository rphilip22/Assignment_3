preferences = ["coffee", "tea", "coffee", "soda"]
counts = {}

# Count the occurrences of each preference
for preference in preferences:
    if preference in counts:
        counts[preference] += 1
    else:
        counts[preference] = 1

# Calculate total preferences
total = len(preferences)
print("Total preferences:", total)
print("Preference counts:", counts)

# Print percentages for each preference
for item in counts:
    percentage = (counts[item] / total) * 100
    print(f"{item}: {percentage:.0f}%")
