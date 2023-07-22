import pandas as pd
import dask_ml.cluster as dc
import logging


class Metrics:

    def __init__(self):
        """

        """

        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, models: [dc.KMeans]):
        """
        model: dc.KMeans
        for model in models:
            self.__logger.info(model.inertia_)

        :param models:
        :return:
        """

        distortions = {models[i].n_clusters: models[i].inertia_
                       for i in range(len(models))}
        self.__logger.info(distortions)
        frame = pd.DataFrame.from_dict(distortions, orient='index', columns=['distortion'])
        self.__logger.info(frame)
        frame.reset_index(drop=False, inplace=True)
        frame.rename(columns={'index': 'n_clusters'}, inplace=True)
        self.__logger.info(frame)
