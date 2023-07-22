"""
main.py
"""
import logging
import os
import sys

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
    structures.people().info()
    structures.log().info()
    design: pd.DataFrame = structures.design()
    logger.info(design.head())
    logger.info(design.to_numpy())


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Classes
    import src.data.read
    import src.data.structures

    # Instances
    read = src.data.read.Read()


    main()
