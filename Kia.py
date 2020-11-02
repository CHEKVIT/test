import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-n','--name', required = False, help = "some description")

params, tmp = ap.parse_known_args()
print(tmp)
print(params)