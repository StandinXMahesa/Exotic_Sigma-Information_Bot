oldword = {"Pterinochilus Murinus":"/murinus","Monocrentropus Balfouri":"/balfouri","Augacephalus Ezendami":"/ezendami","Cyriopagopus Sp Hati Hati":"/hatihati","Poecilotheria Metallica":"/metallica","Ceratogyrus Darlingi":"/darlingi","Selenocosmia Javanensis":"/javanensis","Haplopelma Doriae":"/doriae","Lampropelma Sp Borneo Black":"/borneo","Lampropelma Nigerrimum":"/nigerriumum","Cyriopagopus Lividus":"/lividus","Poecilotheria Regalis":"/regalis"}

newword = {"Brachypelma Aratum":"/aratum","Brachypelma Boehmei":"/boehmei","Tliltocati Vagans":"/vagans","Tliltocati Albopilosum":"/albopilosum","Nhandu Chromatus":"/chromatus","Nhandu Tripedii":"trupedii","Theraphosa Blondi":"/blondi","Lasiodora Parahybana":"/parahybana","Brachypelma Emelia":"/emelia","Brachypelma Klassi":"/klassi","Grammostola Pulchripes":"/pulchripes","Chromatopelma Cyaneopubescens":"/cyaneo","Avicularia Metallica":"/avimetallica","Brachypelma Albiceps":"/albiceps"}

oldword = dict(sorted(oldword.items()))
# print(list(oldword.items()))
newword = dict(sorted(newword.items()))
print(list(newword.items()))
# print(sorted(oldword.items(),key=lambda x :x[1]))