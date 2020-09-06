import requests
import csv
from .timer import Timer
from .proc import Proc

_data_source = {
    "nyt_us_states": {
        "url": "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv",
        "interval": 43200  # refreshes every 12 hours
    },
    "nyt_us_counties": {
        "url": "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv",
        "interval": 43200  # refreshes every 12 hours
    },
    "xkey_test_data": {
        "url": "https://iad.xkey.org/xwu/data/test.csv",
        "interval": 10
    }
}


def get(**kwargs):
    """ get data from external URI """
    target = kwargs.pop("target", None)
    url = kwargs.pop("url", None)
    ops = []
    if url is not None:
        return get_from_url(url)
    if "__" in target:
        tgts = target.split("__")
        target = tgts[0]
        ops = tgts[1:]
    if target not in _data_source:
        return {}
    refresh = True
    tgt = _data_source[target]
    interval = tgt.get("interval", 43200)
    ts_curr = Timer.get_epoch()
    if "data" in tgt and "updated" in tgt and ts_curr - tgt["updated"] < interval:
        refresh = False
    if refresh:
        tgt["data"] = get_from_url(tgt["url"])
        if tgt["data"]:
            tgt["updated"] = ts_curr
    if ops:
        data = Proc.process(target=target, data=tgt["data"], ops=ops)
    else:
        data = tgt["data"]
    return data


def get_from_url(url):
    columns = {}
    with requests.Session() as s:
        dnld = s.get(url)
        decoded_content = dnld.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        headers = next(cr, None)
        for hdr in headers:
            columns[hdr] = []
        for row in cr:
            for h, v in zip(headers, row):
                columns[h].append(v)
    return columns