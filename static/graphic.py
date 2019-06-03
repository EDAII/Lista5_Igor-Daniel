import matplotlib.pyplot as plt
import numpy as np


class Plot:
    @staticmethod
    def plotting_graph(total_time):
        x = np.linspace(0, total_time, 10)
        y = x
        plt.plot(x, y)
        plt.title('Time - Search Method')
        plt.xlabel('time(x 1000)')
        plt.ylabel('time(x 1000)')
        plt.savefig('method.png', bbox_inches='tight')
        plt.show()

    @staticmethod
    # Função para comparar gráficos
    def compare_graph(total_time_one, total_time_two):
        x = np.linspace(0, total_time_one, 10)
        y = x

        x_2 = np.linspace(0, total_time_two, 10)
        y_2 = x_2

        plt.subplot(1, 2, 1)
        plt.plot(x, y)
        plt.title('Time 1')
        plt.xlabel('time(x 1000)')
        plt.ylabel('time(x 1000)')

        plt.subplot(1, 2, 2)
        plt.plot(x_2, y_2, color='xkcd:salmon')
        plt.title('Time 2')
        plt.xlabel('time(x 1000)')
        plt.ylabel('time(x 1000)')

        plt.savefig('compare_methods.png', bbox_inches='tight')
        plt.show()
