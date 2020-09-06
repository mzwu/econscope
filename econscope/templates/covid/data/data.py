import econscope.templates.covid.data.fetch as fetch

testdata = {
    "bardata": {
        "data1": [220, 240, 270, 250, 280],
        "data2": [180, 150, 300, 70, 120],
        "data3": [200, 310, 150, 100, 180]
    }
}


def get(target="bardata"):
    """ Return Data for Charts"""
    if target in testdata:
        return testdata[target]
    else:
        return fetch.get(target=target)