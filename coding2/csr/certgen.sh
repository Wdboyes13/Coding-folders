echo ""CN":"Domain or website url","key":{"algo": "rsa","size": 2048},"names":[{"C":"CA","ST":"British Columbia","L":"Chilliwack","O":"Organization","OU":"Project"}]}" >> request.json
cfssl genkey request.json | cfssl -bare csr-req
jq -n --arg csr "$(cat csr-req.csr)" '{"certificate_request": $csr, "profile":"www"}' > ssl-sign.json
curl -d @ssl-sign.json https://localhost:8980/api/v1/cfssl/sign > ssl-cert.pem
