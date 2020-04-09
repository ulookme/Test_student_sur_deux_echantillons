import numpy as np
from statsmodels.stats.proportion import proportions_ztest as ztest
from math import sqrt
from scipy import stats
import scipy.stats as stat


### SUJET ####
#Pour déterminer s’il existait un lien entre l’allaitement maternel à la naissance et la pression artérielle dans l’enfance,
# une étude a consisté à mesurer la pression artérielle systolique à l’âge de 7 ans chez des enfants dont on savait s’ils avaient été allaités ou non. 
# La pression artérielle systolique moyenne mesurée à 7 ans était de 98,5 mmHg (écart-type, 9,0) chez 5478 enfants
# qui avaient été allaités à la naissance et de 99,9 mmHg (écart-type 9,6) chez 1125 enfants qui n’ont pas été allaités à la naissance. La pression artérielles systolique est une variable de distribution normale. 
# La pression artérielle systolique mesurée  à l’âge de 7 ans différe-t-elle en fonction de l’allaitement maternel à la naissance ?

# méthosz :de comparaison de 2 moyennes observées sur 2 échantillons indépendants

#a ne pas faire = de comparaison de 2 moyennes observées sur 2 échantillons appariés
#Faux (les 2 groupes ont des effectifs différents et ne sont pas constitués des mêmes enfants)

#L’hypothèse nulle (H0) du test peut s’écrire :Il n’existe pas d’association entre l’allaitement à la naissance et 
# la pression artérielle systolique moyenne mesurée à l’âge de 7 ans

#Avant d’utiliser un test t de Student, les auteurs ont dû vérifier que :la variance de la pression artérielle systolique est 
# comparable dans un rapport de 1 à 3 entre les enfants allaités et les enfants non-allaités à la naissance
#C les observations sont indépendantes

#conclusion:
#La pression artérielle systolique moyenne mesurée à 7 ans différait significativement
# entre les enfants allaités (98.5 mmHg, écart-type, 9.0) et les enfants non-allaités (99.9 mmHg écart-type, 9.6) à la naissance (P <0.001)

# population 1 les enfant allaité
#le nombre de sujet au teste ou enfant de 7 appeller ici  n1 
n1=5478
#la moyenne de la tension appeller ici mu1
mu1=98,5
#l'ecartypte donné appeller ecart1
ecart1=9,0

# echantillon d'enfant n'ayant pas allaiter 
n2=1125
mu2=99,9
ecart2=11,25
# on créé des variables pour les resultat du teste t ainsi que de la pPvalue
pValue=0
To=0
#alpha etant la marge derreur nous permettant daccepter l'hoptese nulle ou alternative dépendant de la superioriter ou l'inferiorité de la Pvalue
Alpha=0,5
# on créé un boucle permettant de de retourné mille fois les resultat du teste pour se rapricher au maximun de la pvalue "vrai"
for i in range(1000):
    s1= np.random.normal(mu1, n1, ecart1)
    s2= np.random.normal(mu2, n2, ecart2)
    #le code pour T de student si dessous
    rvs= stats.ttest_ind(s1,s2)
    To += [0]
    pValue += [1]

To=To/1000
pValue=pValue/1000
print(To)
print(pValue)
#en fonction du resultat on print si l'hypothse est accepter ou nul
if pValue < Alpha:
    print("le LDL est different de l'hypothese null")
else:
    print("le LDL rejéte le fait que lallaitement na pas de liens avec la tension")

