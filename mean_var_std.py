import numpy as np

def calculate(list):

    #check argument
    if  len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # initialise dictionary
    calculations = {
        'mean': [ [], [], 0.0  ],
        'variance': [ [], [], 0.0  ],
        'standard deviation': [ [], [], 0.0  ],
        'max': [ [], [], 0.0  ],
        'min': [ [], [], 0.0  ],
        'sum': [ [], [], 0.0  ]
    }

    # create numpy array
    matrix = np.array([ list[0:3],
                        list[3:6],
                        list[6:9]])

    # calculate means
    calculations["mean"][0] = np.mean(matrix, 0).tolist()
    calculations["mean"][1] = np.mean(matrix, 1).tolist()
    calculations["mean"][2] = np.mean(matrix).tolist()


    # calculate variance
    calculations["variance"][0] = np.var(matrix, 0).tolist()
    calculations["variance"][1] = np.var(matrix, 1).tolist()
    calculations["variance"][2] = np.var(matrix).tolist()

    # calculate standard deviation
    calculations["standard deviation"][0] = np.std(matrix, 0 ).tolist()
    calculations["standard deviation"][1] = np.std(matrix, 1).tolist()
    calculations["standard deviation"][2] = np.std(matrix).tolist()

    # max
    calculations["max"][0] = np.max(matrix, 0).tolist()
    calculations["max"][1] = np.max(matrix, 1).tolist()
    calculations["max"][2] = np.max(matrix).tolist()

    #min
    calculations["min"][0] = np.min(matrix, 0).tolist()
    calculations["min"][1] = np.min(matrix, 1).tolist()
    calculations["min"][2] = np.min(matrix).tolist()

    #sum
    calculations["sum"][0] = np.sum(matrix, 0).tolist()
    calculations["sum"][1] = np.sum(matrix, 1).tolist()
    calculations["sum"][2] = np.sum(matrix).tolist()


    return calculations
