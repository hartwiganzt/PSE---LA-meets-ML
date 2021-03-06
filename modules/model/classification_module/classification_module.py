import numpy as np


##  This class handles the classification of matrices using a neural network
from modules.view.output_service import OutputService


class Classifier:

    __path: str = ""

    __output_service: OutputService = OutputService()

    ##  Starts the classification process
    #
    #   @param path where the matrix that will be classified is located
    #   @param network path where the neural network is located
    @staticmethod
    def start(path: str, network: str):
        pass

    @staticmethod
    def __print():
        pass

    ##  Load the neural network
    #
    #   @param network path where the neural network is located
    @staticmethod
    def __load_network(network: str):
        pass

    ##  Scales all the values of a matrix into a fixed range
    #
    #   @param matrix which will be normalized
    #   @return matrix which is normalized
    @staticmethod
    def __normalize(matrix: np.ndarray) -> np.ndarray:
        pass

    @staticmethod
    def set_output_service(service: OutputService):
        Classifier.__output_service = service
