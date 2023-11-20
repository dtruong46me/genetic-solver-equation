import matplotlib.pyplot as plt
import pylab
import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

class Visualize:
    # def __init__(self, x_result, y_result, fitness):
    #     self.x_result = x_result
    #     self.y_result = y_result
    #     self.fitness = fitness
    @staticmethod
    def plot_result(x_result, y_result, fitness):
        
        save_path = r"./genetic-solver-equation/assets/viz/"
        os.makedirs(save_path, exist_ok=True)

        plt.figure()
        plt.style.use("seaborn")

        plt.plot([i for i in range(1, len(x_result) + 1)], x_result)
        plt.title('x_value')
        plt.xlabel('Iteration')
        plt.savefig(os.path.join(save_path, 'x.png'))
        plt.tight_layout()
        plt.show()


        plt.figure()
        plt.style.use("seaborn")

        plt.plot([i for i in range(1, len(x_result) + 1)], y_result)
        plt.title('y_value')
        plt.xlabel('Iteration')
        plt.savefig(os.path.join(save_path, 'y.png'))
        plt.tight_layout()
        plt.show()

        plt.figure()
        plt.style.use("seaborn")

        plt.plot([i for i in range(1, len(x_result) + 1)], fitness)
        plt.title('Fitness')
        plt.xlabel('Iteration')
        plt.savefig(os.path.join(save_path, 'fitness.png'))
        plt.tight_layout()
        plt.show()
    

# solver = Genetic_Algorithm(min_range=-7, max_range=7)
# x_result, y_result, fitness, execution_time=solver.solve()

# save_path = r"./genetic-solver-equation/assets/viz/"
# os.makedirs(save_path, exist_ok=True)

# plt.figure()
# plt.style.use("seaborn")

# plt.plot([i for i in range(1, len(x_result) + 1)], x_result)
# plt.title('x_value')
# plt.xlabel('Iteration')
# plt.savefig(os.path.join(save_path, 'x.png'))
# plt.tight_layout()
# plt.show()


# plt.figure()
# plt.style.use("seaborn")

# plt.plot([i for i in range(1, len(x_result) + 1)], y_result)
# plt.title('y_value')
# plt.xlabel('Iteration')
# plt.savefig(os.path.join(save_path, 'y.png'))
# plt.tight_layout()
# plt.show()

# plt.figure()
# plt.style.use("seaborn")

# plt.plot([i for i in range(1, len(x_result) + 1)], fitness)
# plt.title('Fitness')
# plt.xlabel('Iteration')
# plt.savefig(os.path.join(save_path, 'fitness.png'))
# plt.tight_layout()
# plt.show()

