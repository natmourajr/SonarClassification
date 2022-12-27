import pickle


def write_list_of_hidden_neurons(filename, hidden_neurons):
    with open(filename,'wb') as file_handler:
        pickle.dump([hidden_neurons],file_handler)
    return 0
def get_list_of_hidden_neurons(filename):
    with open(filename,'rb') as file_handler:
        [hidden_neurons] = pickle.load(file_handler)
        
    return hidden_neurons

def update_model_status(filename, ifold, ineuron, iinit, status):
    with open(filename,'rb') as file_handler:
        [model_status] = pickle.load(file_handler)
    model_status[ifold, ineuron, iinit] = status
    with open(filename,'wb') as file_handler:
        pickle.dump([model_status],file_handler)
    return 0
    