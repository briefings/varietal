"""
main.py
"""
import logging
import os
import sys


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

    # The clients and the number of transactions per client
    structures.people().info()

    # offers & transactions
    structures.log().info()

    # Design matrix
    design = structures.design()
    logger.info(design.head())


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
