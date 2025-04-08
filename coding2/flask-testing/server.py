import flask
import requests
import json
import subprocess
import tempfile
app = flask.Flask(__name__)
@app.route('/')
def index():
    return flask.render_template('index.html')
@app.route('/auth')
def auth():
    return flask.redirect('http://localhost:8080')
@app.route('/dav')
def dav():
    return flask.redirect('http://localhost:5232')
@app.route('/cert')
def cert():
    return flask.render_template('cert.html')
@app.route('/certgen', methods=['POST'])
def certgen():
    req = flask.request
    request = {
        "CN": req.form['CN'],
        "key": {
            "algo": "rsa",
            "size": 2048
        },
        "names": [
            {
                "C": req.form['C'],
                "ST": req.form['ST'],
                "L": req.form['L'],
                "O": req.form['O'],
                "OU": req.form['OU']
            }
        ]
    }
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_json_file:
        json.dump(request, temp_json_file)
        temp_json_file.close()
    cfssl_proc = subprocess.Popen(
        ["cfssl", "genkey", temp_json_file.name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    cfssljson_proc = subprocess.Popen(
        ["cfssljson", "-bare", "csr-req"],
        stdin=cfssl_proc.stdout,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    csr_output, error = cfssljson_proc.communicate()
    if error:
        print("Error generating CSR:", error.decode())
        exit(1)
    sign_request = json.dumps({
        "certificate_request": csr_output.decode().strip(),
        "profile": "www"
    })
    curl_proc = subprocess.Popen(
        ["curl", "-d", sign_request, "https://localhost:8980/api/v1/cfssl/sign"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    signed_cert, error = curl_proc.communicate()
    if error:
        print("Error signing certificate:", error.decode())
        exit(1)

    # Step 4: Save the signed certificate to a PEM file
    with open("signed_cert.pem", "wb") as cert_file:
        cert_file.write(signed_cert)

    print("Signed certificate saved to 'signed_cert.pem'")
app.run(host='localhost', port=3000)