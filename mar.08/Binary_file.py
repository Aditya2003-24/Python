# dump or load

# pypi.org se install kar sakte hai pickle ko

# pickle.dump  pickle.dump(data,file)

# pickle.load(file)
import pickle

# f=open('first','ab')
# data=[10,20,30,'aditya']
# pickle.dump(data,f)
# f.close()

f=open('first','rb')
data=pickle.load(f)
print(data)