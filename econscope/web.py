from flask import Flask, render_template, send_from_directory, jsonify
import os
import econscope.data.data as econdata

app = Flask(__name__)  # instantiate Flask with current name
pwd = os.path.dirname(__file__)  # get directory name of current file


def file_read(filename):
    with open(os.path.join(pwd, filename), 'r') as fh:  # concatenate path + filename, fh=file handle
        return fh.read()


web_data = {
    "topics": [
        "unemployment",
        "businesses",
        "commodities",
        "gdp",
        "other"
    ]
}


@app.route("/")
def home_view():
    return render_template('home.html', web_data=web_data)


@app.route("/znew")
def new_home():
    return render_template('znew/home.html')


@app.route("/weekly-update")
def weekly_update():
    return render_template('update.html', web_data=web_data)


@app.route("/assets/<path:suburl>")
def get_assets(suburl):
    dirs = suburl.split("/")
    dirname = "assets/" + "/".join(dirs[:-1])
    return send_from_directory(dirname, dirs[-1])


@app.route("/data/<string:target>")
def data_view(target):
    return jsonify(econdata.get(target=target))


@app.route("/charts/<string:filename>")
def chart_view(filename):
    return render_template("charts/" + filename)
