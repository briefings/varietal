import pandas as pd


class Structures:

    def __init__(self, offers: pd.DataFrame, transactions: pd.DataFrame):
        """

        :return:
        """

        self.__offers = offers
        self.__transactions = transactions

    def people(self) -> pd.DataFrame:
        """
        Determines the number of transactions per unique surname. Note, a single transaction
        denotes the purchase of one or more items.

        :return:
        """

        data = self.__transactions['surname'].value_counts().reset_index(name='n_transactions')
        data.rename(columns={'index': 'surname'}, inplace=True)

        return data

    def log(self) -> pd.DataFrame:
        """
        Per offer type, denoted by offer_id, create a record per purchase

        :return:
        """

        data = self.__offers.merge(self.__transactions, how='left', on='offer_id')

        return data

    def design(self) -> pd.DataFrame:
        """

        :return:
        """

        log = self.log()
        data = pd.pivot_table(log[['surname', 'offer_id', 'n_purchases']],
                              values='n_purchases', index='surname', columns='offer_id')
        data.fillna(value=0, inplace=True)

        return data
