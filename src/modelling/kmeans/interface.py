import numpy as np
import sklearn.cluster as sc
import dask


class Interface:

    def __init__(self, design: np.ndarray):
        """

        :param design:
        """

        self.__random_state = 5
        self.__design = design

    @dask.delayed
    def __model(self, n_clusters: int):
        """

        :param n_clusters:
        :return:
        """

        return sc.KMeans(n_clusters=n_clusters, init='k-means++', n_init=100,
                         random_state=self.__random_state, copy_x=True).fit(self.__design)

    def exc(self, n_clusters_series: np.ndarray):
        """

        :param n_clusters_series:
        :return:
        """

        computations = []
        for n_clusters in n_clusters_series:
            model = self.__model(n_clusters=n_clusters)
            computations.append(model)

        models = dask.compute(computations, scheduler='threads')[0]

        return models
