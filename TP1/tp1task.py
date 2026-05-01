document={"D1": "Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza",
          "D2":"Five pizza were ready , but 3 bourak burned!",
          "D3":"We only had 8 chamiyya, no pizza, and one tea.",
          "D4":"Is 6 too much? I ate nine bourak lol."}
nombre={"0":"zero","1":"one","2":"two",
        "3":"three","4":"four","5":"five",
        "6":"six","7":"even","8":"eight",
        "9":"nine","10":"ten"}
ponctuations=".,!?::;"
def normalisation(D):
    D = D.lower()
    D_nv=""
    for c in D:
     if c in nombre:
      D_nv = D_nv + nombre[c]
     else :
      D_nv = D_nv + c
    for p in ponctuations:
        D_nv = D_nv.replace(p, "")
    return D_nv

for doc in document:
    document[doc] = normalisation(document[doc])
    print(document[doc])