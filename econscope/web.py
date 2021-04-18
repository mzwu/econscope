from flask import Flask, render_template, send_from_directory, jsonify
import os
import econscope.templates.covid.data.data as econdata

app = Flask(__name__)  # instantiate Flask with current name

pwd = os.path.dirname(__file__)  # get directory name of current file


def file_read(filename):
    with open(os.path.join(pwd, filename), 'r') as fh:  # concatenate path + filename, fh=file handle
        return fh.read()



@app.route("/")
def home_view():
    return render_template('index.html')


@app.route("/templates/<path:suburl>")
def get_assets(suburl):
    dirs = suburl.split("/")
    dirname = "templates/" + "/".join(dirs[:-1])
    return send_from_directory(dirname, dirs[-1])


@app.route("/data/<string:target>")
def data_view(target):
    return jsonify(econdata.get(target=target))


@app.route("/charts/<string:filename>")
def chart_view(filename):
    return render_template("charts/" + filename)


@app.route("/404")
def error_404():
    return render_template('404.html')


@app.route("/covid19-cases-tracker")
def cases_tracker():
    return render_template('covid/cases.html')


@app.route("/covid19-economic-analysis")
def econ_analysis():
    return render_template('covid/analysis/econanalysis-1.html')


@app.route("/covid19-unemployment")
def unemploy():
    return render_template('covid/analysis/unemployment.html')


@app.route("/covid19-gvmt-stimulus")
def gvmt_stimulus():
    return render_template('covid/analysis/stimulus.html')


@app.route("/covid19-business")
def business():
    return render_template('covid/analysis/business.html')


@app.route("/covid19-gdp")
def gdp():
    return render_template('covid/analysis/gdp.html')


@app.route("/covid19-dec2020-stimulus")
def dec2020_stimulus():
    return render_template('covid/analysis/dec2020stimulus.html')


@app.route("/covid19-safety-info")
def safety_info():
    return render_template('covid/safetyinfo.html')


@app.route("/about")
def about_me():
    return render_template('about.html')


@app.route("/contact")
def contact_me():
    return render_template('contact.html')


@app.route("/updates-2021-april")
def weekly_updates_april_2021():
    return render_template('updates/2021/2021april.html')


@app.route("/updates-2021-march")
def weekly_updates_march_2021():
    return render_template('updates/2021/2021march.html')


@app.route("/updates-2021-february")
def weekly_updates_february_2021():
    return render_template('updates/2021/2021february.html')


@app.route("/updates-2021-january")
def weekly_updates_january_2021():
    return render_template('updates/2021/2021january.html')


@app.route("/updates-2020-december")
def weekly_updates_december_2020():
    return render_template('updates/2020/updates2020december.html')


@app.route("/updates-2020-november")
def weekly_updates_november_2020():
    return render_template('updates/2020/updates2020november.html')


@app.route("/updates-2020-october")
def weekly_updates_october_2020():
    return render_template('updates/2020/updates2020october.html')


@app.route("/updates-2020-september")
def weekly_updates_september_2020():
    return render_template('updates/2020/updates2020september.html')


@app.route("/updates-2020-august")
def weekly_updates_august_2020():
    return render_template('updates/2020/updates2020august.html')


@app.route("/updates-2020-july")
def weekly_updates_july_2020():
    return render_template('updates/2020/updates2020july.html')


@app.route("/updates-2020-june")
def weekly_updates_june_2020():
    return render_template('updates/2020/updates2020june.html')


@app.route("/updates-2020-may")
def weekly_updates_may_2020():
    return render_template('updates/2020/updates2020may.html')


@app.route("/updates-2020-april")
def weekly_updates_april_2020():
    return render_template('updates/2020/updates2020april.html')


@app.route('/updates-2021-0417')
def update_04172021():
    return render_template("updates/2021/04172021.html")


@app.route('/updates-2021-0410')
def update_04102021():
    return render_template("updates/2021/04102021.html")


@app.route('/updates-2021-0403')
def update_04032021():
    return render_template("updates/2021/04032021.html")


@app.route('/updates-2021-0327')
def update_03272021():
    return render_template("updates/2021/03272021.html")


@app.route('/updates-2021-0320')
def update_03202021():
    return render_template("updates/2021/03202021.html")


@app.route('/updates-2021-0313')
def update_03132021():
    return render_template("updates/2021/03132021.html")


@app.route('/updates-2021-0306')
def update_03062021():
    return render_template("updates/2021/03062021.html")


@app.route('/updates-2021-0227')
def update_02272021():
    return render_template("updates/2021/02272021.html")


@app.route('/updates-2021-0220')
def update_02202021():
    return render_template("updates/2021/02202021.html")


@app.route('/updates-2021-0213')
def update_02132021():
    return render_template("updates/2021/02132021.html")


@app.route('/updates-2021-0206')
def update_02062021():
    return render_template("updates/2021/02062021.html")


@app.route('/updates-2021-0130')
def update_01302021():
    return render_template("updates/2021/01302021.html")


@app.route('/updates-2021-0123')
def update_01232021():
    return render_template("updates/2021/01232021.html")


@app.route('/updates-2021-0116')
def update_01162021():
    return render_template("updates/2021/01162021.html")


@app.route('/updates-2021-0109')
def update_01092021():
    return render_template("updates/2021/01092021.html")


@app.route('/updates-2020-1226')
def update_12262020():
    return render_template("updates/2020/12262020.html")


@app.route('/updates-2020-1219')
def update_12192020():
    return render_template("updates/2020/12192020.html")


@app.route('/updates-2020-1212')
def update_12122020():
    return render_template("updates/2020/12122020.html")


@app.route('/updates-2020-1205')
def update_12052020():
    return render_template("updates/2020/12052020.html")


@app.route('/updates-2020-1128')
def update_11282020():
    return render_template("updates/2020/11282020.html")


@app.route('/updates-2020-1121')
def update_11212020():
    return render_template("updates/2020/11212020.html")


@app.route('/updates-2020-1114')
def update_11142020():
    return render_template("updates/2020/11142020.html")


@app.route('/updates-2020-1107')
def update_11072020():
    return render_template("updates/2020/11072020.html")


@app.route('/updates-2020-1031')
def update_10312020():
    return render_template("updates/2020/10312020.html")


@app.route('/updates-2020-1024')
def update_10242020():
    return render_template("updates/2020/10242020.html")


@app.route('/updates-2020-1017')
def update_10172020():
    return render_template("updates/2020/10172020.html")


@app.route('/updates-2020-1010')
def update_10102020():
    return render_template("updates/2020/10102020.html")


@app.route('/updates-2020-1003')
def update_10032020():
    return render_template("updates/2020/10032020.html")


@app.route('/updates-2020-0926')
def update_09262020():
    return render_template("updates/2020/09262020.html")


@app.route('/updates-2020-0919')
def update_09192020():
    return render_template("updates/2020/09192020.html")


@app.route('/updates-2020-0912')
def update_09122020():
    return render_template("updates/2020/09122020.html")


@app.route('/updates-2020-0905')
def update_09052020():
    return render_template("updates/2020/09052020.html")


@app.route('/updates-2020-0829')
def update_08292020():
    return render_template("updates/2020/08292020.html")


@app.route('/updates-2020-0822')
def update_08222020():
    return render_template("updates/2020/08222020.html")


@app.route('/updates-2020-0815')
def update_08152020():
    return render_template("updates/2020/08152020.html")


@app.route('/updates-2020-0808')
def update_08082020():
    return render_template("updates/2020/08082020.html")


@app.route('/updates-2020-0801')
def update_08012020():
    return render_template("updates/2020/08012020.html")


@app.route('/updates-2020-0725')
def update_07252020():
    return render_template("updates/2020/07252020.html")


@app.route('/updates-2020-0718')
def update_07182020():
    return render_template("updates/2020/07182020.html")


@app.route('/updates-2020-0711')
def update_07112020():
    return render_template("updates/2020/07112020.html")


@app.route('/updates-2020-0704')
def update_07042020():
    return render_template("updates/2020/07042020.html")


@app.route('/updates-2020-0627')
def update_06272020():
    return render_template("updates/2020/06272020.html")


@app.route('/updates-2020-0620')
def update_06202020():
    return render_template("updates/2020/06202020.html")


@app.route('/updates-2020-0613')
def update_06132020():
    return render_template("updates/2020/06132020.html")


@app.route('/updates-2020-0606')
def update_06062020():
    return render_template("updates/2020/06062020.html")


@app.route('/updates-2020-0530')
def update_05302020():
    return render_template("updates/2020/05302020.html")


@app.route('/updates-2020-0523')
def update_05232020():
    return render_template("updates/2020/05232020.html")


@app.route('/updates-2020-0516')
def update_05162020():
    return render_template("updates/2020/05162020.html")


@app.route('/updates-2020-0509')
def update_05092020():
    return render_template("updates/2020/05092020.html")


@app.route('/updates-2020-0502')
def update_05022020():
    return render_template("updates/2020/05022020.html")


@app.route('/updates-2020-0425')
def update_04252020():
    return render_template("updates/2020/04252020.html")

