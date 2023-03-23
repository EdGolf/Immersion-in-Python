source = [0,0,1,1,2,7,5,7,3,4,]

repetition = [x for x in set(source) if source.count(x) > 1]

print(f"Source list: {source}\nDublicate items: {repetition}")