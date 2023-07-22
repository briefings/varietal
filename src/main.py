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
    logger.info(offers.head())

    transactions = read.transactions()
    transactions.info()
    logger.info(transactions.head())

    people = transactions['surname'].value_counts().reset_index(name='n_transactions')
    logger.info(people)


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

    # Instances
    read = src.data.read.Read()

    main()
