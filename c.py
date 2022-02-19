import io, sys
from collections import namedtuple
import pandas as pd

# 309 1000 100 5 1000 7
# sa 2
# sb 4
# sc 1
# shcgeicf 82 51 579
# sbj sfc seh sfe shb sdg sf sfb sid sgc seb sjd sha sh shc sjb sce sdd sej shi sd scc sgb sfd sb sbe sif sbf sff sdh sji sga sbc see sj sbi scg sgj sfa sbg sca sih sdi sjf shh sec she scb sdc sje sde sef sci sjj sa sic sg sdb sfh scd sbd sda sgf sei sjg sib sch sig sba shj sdj sjc scf shf sfg sgh sja sie si sdf sfj sbh
# scaiafej 29 81 892
# sfb sdi sdj sgi sie sa sij scg seh sce sig scj sfg sde sbf sfi she sha scb sca sia sif sec sbh sgj sfj sbb sb shb
# sdhghhae 70 84 299
# shj sbc shb sfc sgd sib sja sgf sdd sdj sfb sfg se sf sdb sii sei scg sgb sbi sia scb sbe sgh sbd sfe sji sce sgj sie sfh shh sg sj shi sgc sjh sba sgi sjb sed sbg sif sjf sih scc sge sci sef shd sdc sdg sea sic sgg sha see she sij sd shg sdh sa sid sb sjj seb sjg sjd scj

# ○ time limit in days: L (1 ≤ L ≤ 10 3),
# ○ number of Google engineers G (1 ≤ G ≤ 10 5),
# ○ number of services S (1 ≤ S ≤ 10 4),
# ○ number of initial binaries B (1 ≤ B ≤ 10 4),
# ○ number of features F (1 ≤ F ≤ 10 4),
# ○ duration in days to create a new binary N (1 ≤ N ≤ 10).

L, G, S, B, F, N = map(int, input().split())

# ==> files/an_example.txt <==
# 10 2 5 3 2 5
#
# ==> files/breadth_of_choice.txt <==
# 442 10 504 100 1000 7
#
# ==> files/constrained_optimisation.txt <==
# 309 1000 100 5 1000 7
#
# ==> files/distinction.txt <==
# 689 10 100 10 10000 8
#
# ==> files/expectation_maximisation.txt <==
# 872 1000 200 2 100 4
#
# ==> files/five_thousand.txt <==
# 928 10 100 10 5000 1

Services = {}
for i in range(S):
    n, b = input().split()
    Services[n] = int(b)

Feature = namedtuple('Feature', [ 'name', 'M', 'D', 'U', 'services' ])
Features = {}
# the feature name (string of 1-20 lowercase leers a-z and hyphens -),
#  ■ Mi (1 ≤ Mi ≤ S) - the number of services that need to be modied to suppo the i-th feature,
#  ■ Di (1 ≤ Di ≤ 10 2) - the diculty of the i-th feature,
#  ■ Ui (1 ≤ Ui ≤ 10 5) - number of daily users that will benet from the feature once it is launched.
#  ○ The second line contains a list of f strings Si,1 , Si,2 , ..., Si,Mi - the names of the services to be modied to suppo the i-th feature.

stat_ = pd.DataFrame()

for _ in range(F):
    name, *mdu = input().split()
    M, D, U = map(int, mdu)
    ss = input().split()
    assert M == len(ss)
    Features[n] = Feature(n, M, D, U, ss)



Engineers = []
# Engineers.append(['move sc 2', 'impl foo 2'])
# Engineers.append(['wait 2', 'impl bar 1', 'impl bar 2'])

for l in range(L):
    pass

# 2
# 2
# move sc 2
# impl foo 2
# 3
# wait 2
# impl bar 1
# impl bar 2

with open('sub.c.txt', 'w') as fo:
    fo.write(str(len(Engineers)))

    for e in Engineers:
        fo.write(f'\n{len(e)}\n')
        fo.writelines('\n'.join(e))
