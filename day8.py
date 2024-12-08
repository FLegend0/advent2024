f = open('day8.in', 'r')

antennamap = {}

unique_locations = []

rowcount = 0
columncount = 0

for i in f:
    i = i.strip()
    columncount = 0
    for j in i:
        if j != '.':
            if j not in antennamap:
                antennamap[j] = []
            antennamap[j].append((rowcount, columncount))
        columncount += 1
    rowcount += 1


for key in antennamap:
    if len(antennamap[key]) > 1:
        for i in antennamap[key]:
            if i not in unique_locations:
                unique_locations.append(i)
    for i in range(0, len(antennamap[key])):
        for j in range(i+1, len(antennamap[key])):
            ant1 = antennamap[key][i]
            ant2 = antennamap[key][j]

            mandistance = (ant2[0]-ant1[0], ant2[1]-ant1[1])

            nodestop = False
            forwardnode = (ant2[0] + mandistance[0], ant2[1] + mandistance[1])
            # PART 1
            # if not (forwardnode[0] < 0 or forwardnode[0] >= rowcount or forwardnode[1] < 0 or forwardnode[1] >= columncount):
            #     if forwardnode not in unique_locations:
            #         unique_locations.append(forwardnode)
            while not nodestop:
                if not (forwardnode[0] < 0 or forwardnode[0] >= rowcount or forwardnode[1] < 0 or forwardnode[1] >= columncount):
                    if forwardnode not in unique_locations:
                        unique_locations.append(forwardnode)
                    forwardnode = (forwardnode[0] + mandistance[0], forwardnode[1] + mandistance[1])
                else:
                    nodestop = True

            nodestop = False
            backwardnode = (ant1[0] - mandistance[0], ant1[1] - mandistance[1])
            # PART 1
            # if not (backwardnode[0] < 0 or backwardnode[0] >= rowcount or backwardnode[1] < 0 or backwardnode[1] >= columncount):
            #     if backwardnode not in unique_locations:
            #         unique_locations.append(backwardnode)
            while not nodestop:
                if not (backwardnode[0] < 0 or backwardnode[0] >= rowcount or backwardnode[1] < 0 or backwardnode[1] >= columncount):
                    if backwardnode not in unique_locations:
                        unique_locations.append(backwardnode)
                    backwardnode = (backwardnode[0] - mandistance[0], backwardnode[1] - mandistance[1])
                else:
                    nodestop = True

print(len(unique_locations))