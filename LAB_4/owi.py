import math

# top terms from all 5 documents
terms = ["case", "children", "polio", "disease", "year"]

# number of documents in the collection
N = 500000

# number of known documents top 5 documents from the query
R = 5                   


# number of documents term t occurs in 
n = [67897, 23678, 153, 7473, 266010 ]


r = [4, 4, 5, 4, 3]


for i in range(len(terms)):
    top = (r[i] + 0.5) * (N - n[i] - R + r[i] + 0.5)
    down = (n[i] - r[i] + 0.5) * (R - r[i] + 0.5)
    rw = math.log(top/down)
    ow = r[i] * rw

    print(str(terms[i]) + ", " + "rw= " + str(rw) + "  ow= " + str(ow))
