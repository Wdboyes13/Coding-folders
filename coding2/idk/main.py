from grgl import bsns, jsr
ppl = [["Goondonalds"], ["Goonerty Property Brothers"]]
inst = []
for i in range(len(ppl)): 
    inst.append(bsns(ppl[i][0]))
for i in inst:
    i.dmpjson()
js = jsr("names.json"); js.dmp()