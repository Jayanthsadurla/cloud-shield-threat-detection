import os
from flask import Flask, session, url_for, redirect, render_template, request
from werkzeug.utils import secure_filename
import numpy as np

from database import (
    user_reg,
    owner_reg,
    owner_login,
    upload_file,
    owner_viewfiles,
    upload_clouddata,
    user_loginact,
    user_viewfile,
    user_down,
    addf_act,
    server_logact,
    server_viewdata
)

from RSA import encrypt, decrypt, generate
from main import generateblockchain
from eval import main

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- OWNER ----------------
@app.route("/owner")
def owner():
    return render_template("owner.html")


@app.route("/ownerlogact", methods=['POST'])
def owner_login_act():
    status = owner_login(request.form['username'], request.form['password'])
    if status:
        session['username'] = request.form['username']
        return render_template("ownerhome.html")
    return render_template("owner.html", m1="Login failed")


@app.route("/ownerreg/")
def owner_reg_page():
    return render_template("ownerreg.html")


@app.route("/ownerregact", methods=['POST'])
def owner_reg_act():
    status = owner_reg(
        request.form['username'],
        request.form['password'],
        request.form['dob'],
        request.form['email'],
        request.form['city'],
        request.form['contactno']
    )
    return render_template("ownerhome.html" if status else "owner.html")


# ---------------- USER ----------------
@app.route("/user/")
def user():
    return render_template("user.html")


@app.route("/userreg/")
def user_reg_page():
    return render_template("userreg.html")


@app.route("/userregact", methods=['POST'])
def user_reg_act():
    status = user_reg(
        request.form['username'],
        request.form['password'],
        request.form['dob'],
        request.form['email'],
        request.form['city'],
        request.form['contactno']
    )
    return render_template("user.html", m1="Success" if status else "Failed")


@app.route("/userlogact", methods=['POST'])
def user_login_act():
    status = user_loginact(request.form['email'], request.form['password'])
    if status:
        session['email'] = request.form['email']
        return render_template("userhome.html")
    return render_template("user.html", m1="Login failed")


@app.route("/userhome")
def user_home():
    if not session.get('email'):
        return redirect(url_for('user'))
    return render_template("userhome.html")


@app.route("/vf/")
def view_files():
    email = session.get('email')
    if not email:
        return redirect(url_for('user'))

    data = user_viewfile(email)
    return render_template("vf.html", viewfiledata=data)


@app.route("/download/")
def download():
    email = session.get('email')
    if not email:
        return redirect(url_for('user'))

    data = user_down(email)
    return render_template("download.html", downloads=data)


# ---------------- SERVER ----------------
@app.route("/server/")
def server():
    return render_template("server.html")


@app.route("/serverlogact", methods=['POST'])
def server_login_act():
    status = server_logact(request.form['username'], request.form['password'])
    if status:
        session['username'] = request.form['username']
        return render_template("shome.html")
    return render_template("server.html", m1="Login failed")


# ---------------- FILE UPLOAD ----------------
@app.route("/fileupload")
def file_upload_page():
    return render_template("fileupload.html")


@app.route("/Upload", methods=['POST'])
def upload():
    file = request.files['inputfile']
    filename = secure_filename(file.filename)

    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)

    status = upload_file(request.form['fname'], filename, session.get('username'))

    return render_template("fileupload.html", m1="Success" if status else "Failed")


@app.route("/ownerviewfiles")
def owner_view():
    user = session.get('username')
    if not user:
        return redirect(url_for('owner'))

    data = owner_viewfiles(user)
    return render_template("ownerviewfiles.html", showdata=data)


# ---------------- ML PREDICTION ----------------
@app.route("/addfact", methods=['POST'])
def predict():
    try:
        classes = {0: "normal", 1: "dos", 2: "r2l", 3: "u2r", 4: "probe"}

        val = request.form['srv_count']
        pred, prob = main(val)

        result = np.argmax(prob)
        prediction = classes[int(result)]

        status = addf_act(request.form['fname'], prediction)

        return render_template("viewencfiles.html", m1="Success" if status else "Failed")

    except Exception as e:
        return f"ML Error: {str(e)}"


# ---------------- ENCRYPTION ----------------
@app.route("/Gensig/")
def gensig():
    fname = request.args.get('fname')
    owner = request.args.get('owner')
    data = request.args.get('data')

    key_pair = generate(8)
    public_key = key_pair["public"]
    private_key = key_pair["private"]

    datas, key = generateblockchain('block1', data)

    encrypted = encrypt(public_key, data)
    txt = ', '.join(map(str, encrypted))

    path = os.path.join(app.config['UPLOAD_FOLDER'], "RSA.txt")
    with open(path, "w") as f:
        f.write(txt)

    val = ', '.join(map(str, private_key))

    status = upload_clouddata(fname, owner, data, txt, val, str(key))

    if status:
        return redirect(url_for('owner_view'))
    return "Error in encryption"


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))


# ---------------- RUN ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)