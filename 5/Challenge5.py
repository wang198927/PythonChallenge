import pickle

pklFile = open("banner.p","rb")

pklData = pickle.load(pklFile)

print("\n".join("".join(tuple[0]*tuple[1] for tuple in row)for row in pklData))