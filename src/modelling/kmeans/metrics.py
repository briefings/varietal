import logging

import dask_ml.cluster as dc
import numpy as np
import pandas as pd


class Metrics:

    def __init__(self):
        """

        """

        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    @staticmethod
    def exc(models: [dc.KMeans]) -> pd.DataFrame:
        """
        model: dc.KMeans
        for model in models:
            self.__logger.info(model.inertia_)

        :param models:
        :return:
        """

        distortions = {models[i].n_clusters: models[i].inertia_
                       for i in range(len(models))}
        frame = pd.DataFrame.from_dict(distortions, orient='index', columns=['distortion'])
        frame.reset_index(drop=False, inplace=True)
        frame.rename(columns={'index': 'n_clusters'}, inplace=True)

        differences = np.diff(frame['distortion'].to_numpy())
        differences = np.insert(differences.copy(), obj=0, values=np.nan, axis=0)
        frame.loc[:, 'difference'] = differences

        return frame
