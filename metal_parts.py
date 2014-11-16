BOLT  = 1
NUT   = 2
RING  = 3
SCRAP = 4

PROFIT = {
        BOLT:  { BOLT:  0.20, NUT: -0.07, RING: -0.07, SCRAP: -0.07 },
        NUT:   { BOLT: -0.07, NUT:  0.15, RING: -0.07, SCRAP: -0.07 },
        RING:  { BOLT: -0.07, NUT: -0.07, RING:  0.05, SCRAP: -0.07 },
        SCRAP: { BOLT: -0.03, NUT: -0.03, RING: -0.03, SCRAP:  0.03 },
}
