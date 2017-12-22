input = 265149

i = 0
while (i * 2 + 1) ** 2 < input:
    i += 1

outer_rim_length = (i * 2 + 1) ** 2 - ((i - 1) * 2 + 1) ** 2
quarter_rim_length = outer_rim_length / 4
position_on_quarter = (input - ((i - 1) * 2 + 1) ** 2) % quarter_rim_length
distance_to_center = abs(position_on_quarter - quarter_rim_length / 2)

print(i + distance_to_center)
