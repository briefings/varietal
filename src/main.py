"""
main.py
"""
import logging
import os
import sys

import matplotlib.pyplot as plt

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

    structures = src.data.structures.Structures(offers=offers, transactions=transactions)
    design: pd.DataFrame = structures.design()

    models = src.modelling.kmeans.interface.Interface(
        design=design.to_numpy()).exc(n_clusters_series=np.arange(2, 12))

    metrics = src.modelling.kmeans.metrics.Metrics().exc(models=models)

    left: plt.axes
    fig, left = plt.subplots()

    colour = 'tab:orange'
    left.set_xlabel('# of clusters')
    left.set_ylabel('distortion', color=colour)
    left.plot(metrics['n_clusters'], metrics['distortion'], color=colour)
    left.tick_params(axis='y', labelcolor=colour)

    colour = 'black'
    right = left.twinx()
    right.set_ylabel('distortion', color=colour)
    right.plot(metrics['n_clusters'], metrics['difference'], color=colour)
    right.tick_params(axis='y', labelcolor=colour)

    fig.tight_layout()
    plt.show()


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
