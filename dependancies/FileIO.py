import pickle as pkl

def save(name, data):
    file = open(name + "-pk.dt", "wb")
    file.truncate(0)

    pkl.dump(data, file)
    file.close()

def recall(name):
    file = open(name + "-pk.dt", "rb")
    data = pkl.load(file)
    file.close()

    return data
