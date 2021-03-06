import matplotlib.pyplot as plt

import printer
import data_import

from SelfOrganizingMap.NeighborhoodFunction.GaussianFunction import GaussianFunction
from SelfOrganizingMap.SelfOrganizingMap import SelfOrganizingMap

neighborhoodFunction = GaussianFunction(radius=2)
som = SelfOrganizingMap(matrix_height=5,
                        matrix_width=5,
                        input_length=2,
                        neighborhood_function=neighborhoodFunction,
                        learning_rate=0.6,
                        minimum_tiredness_potential=0.7)

# data = data_import.generate_heart()
data = data_import.read_file('attract.txt')

data = data[:1000]

data = data_import.scale_data_set_to_range(data, 0, 1)

printer.print_neurons_connections_over_data_points(som, data, width=900, height=900)

som.learn(data, 30, visualize=False)

printer.print_neurons_connections_over_data_points(som, data, width=900, height=900)

plt.hist(som.quantization_errors, bins=len(som.quantization_errors))
plt.show()
