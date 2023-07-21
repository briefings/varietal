import pandas as pd

import src.functions.streams


class Data:

    def __init__(self):
        """

        :return:
        """

        self.__streams = src.functions.streams.Streams()

    def offers(self) -> pd.DataFrame:

        uri = 'https://raw.githubusercontent.com/miscellane/hub/develop/data/wine/offers.csv'
        fields={'Offer #': 'offer_id', 'Campaign': 'campaign', 'Varietal': 'varietal',
                'Minimum Qty (kg)': 'minimum_qty_kg', 'Discount (%)': 'discount_percentage',
                'Origin': 'origin', 'Past Peak': 'past_peak'}

        data = self.__streams.api(uri=uri, header=0)
        data.rename(columns=fields, inplace=True)

        return data
