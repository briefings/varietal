"""
main.py
"""
import logging
import os
import sys

import numpy as np
import pandas as pd


def main():
    """
    Entry point

    :return:
    """

    logger.info('Varietal')

    offers = read.offers()
    offers.info()

    transactions = read.transactions()
    transactions.info()

    # Structures
    #  - The clients and the number of transactions per client
    #  - The offers & transactions log, i.e., <offers> left join <transactions>
    #  - Design matrix frame
    structures = src.data.structures.Structures(offers=offers, transactions=transactions)
    design: pd.DataFrame = structures.design()

    models = src.modelling.kmeans.interface.Interface(
        design=design.to_numpy()).exc(n_clusters_series=np.arange(2, 12))
    logger.info(type(models[0]))
    src.modelling.kmeans.metrics.Metrics().exc(models=models)


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Re-visit: https://scikit-learn.org/stable/computing/parallelism.html
    # os.environ['OMP_NUM_THREADS'] = '1'

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Classes
    import src.data.read
    import src.data.structures
    import src.modelling.kmeans.interface
    import src.modelling.kmeans.metrics

    # Instances
    read = src.data.read.Read()

    main()
