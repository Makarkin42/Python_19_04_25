import json
import pickle
import time

test = {}
for i in range(20):
    test[i] = f"{i*2}"
print(test)

# pick = pickle.dumps(test)
# print(pick)
#
# picktest = pickle.loads(pick)
# print(picktest)

sonj = json.dumps(test)
#print(sonj)

jsontest = json.loads(sonj)
#print(jsontest)

test = {}
'''for i in range(2**20):
    test[i] = f"{i*2}"
print(2**20)

start = time.time()
with open("p_test.pickle","wb") as f:
    pickle.dump(test,f)
print("pickle",time.time() - start)

start = time.time()
with open("p_test.json","w") as f:
    json.dump(test,f)
print("json",time.time() - start)'''