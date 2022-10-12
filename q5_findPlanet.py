


# 5. Superman and Bottle City of Kandor
def findPlanet(ss, chk):
    p = 0
    d = 0
    tot_out = 0
    res=[]
    for solar in ss:
        tot_out = 0
        for star in solar:
            tot_out += star[0]/star[1]

        if tot_out > chk[0] and tot_out<chk[1]:
            return 1






# 5. Superman and Bottle City of Kandor
res=findPlanet([[[0.433, 200]], [[0.89, 400], [0.6, 300]]], [0.003, 0.005])
print(res)