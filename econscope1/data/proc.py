import pandas
import econscope.data.common as common


class Proc(object):
    def __init__(self):
        pass

    @classmethod
    def process(cls, **kwargs):
        # process gateway
        target = kwargs.pop("target")
        data = kwargs.pop("data", None)
        ops = kwargs.pop("ops", None)
        func = getattr(cls, target, None)
        if func is None:
            return data
        return func(data=data, ops=ops)

    @classmethod
    def nyt_us_states(cls, data=None, ops=None):
        """ only takes on argument, state name or all """
        df = pandas.DataFrame(data)
        if ops[0].upper() in common.states:
            state = common.states[ops[0].upper()]
            return df.loc[df['state'] == state][['date', 'cases', 'deaths']].to_dict(orient="list")
        else:
            return df.groupby("date")[['cases', 'deaths']].apply(lambda x: x.astype(int).sum()). \
                reset_index().to_dict(orient="list")