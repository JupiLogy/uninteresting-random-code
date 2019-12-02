def blipblop(input):

    # Split into segments
    segments = input.split("|")

    # Split into subsegments, count totals for segments
    subsegment = []
    subtotals = []
    for items in segments:
        subtotals.append(0)
        subsegment.append(items.split(","))
        for word in subsegment[-1]:
            if word == "Blip":
                subtotals[-1] += 1

    # Find grand total and print
    subtotals.append(sum(subtotals))
    for i in range(len(subtotals)):
        subtotals[i] = str(subtotals[i])
    return "|".join(subtotals)
