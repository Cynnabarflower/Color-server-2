from flask import Flask, jsonify, request
import ftplib
import time

app = Flask(__name__);


@app.route("/bot", methods=["POST"])
def response():
    name = dict(request.form)['name']
    data = dict(request.form)['data']
    f = open(name, 'w')
    f.write(data)
    f.close()
    ftp = ftplib.FTP("ftp.neuropsylab.com")
    ftp.login("gamedata@neuropsylab.com", 'xGA)Wj636(LQ')
    with open(name, 'rb') as f:
        ftp.storbinary('STOR '+name, f)
    ftp.close()
    query = dict(request.form).__str__()
    res = query
    return jsonify({"response": res})


if __name__ == "__main__":
    app.run(host="0.0.0.0", )
