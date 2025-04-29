# FpML-Messaging-Testing
simple app for FpML-Messaging-Testing
Comparison with SWIFT Implementation
----------------------------------------------------
Feature	       SWIFT Server	            FpML Server
----------------------------------------------------
Message Format	Block-based text	    XML
Validation	  Position-based checks	    XSD schema validation
Use Case	  Payments	                Derivatives trading



 XSD Schema Validation - Download FpML schema:

wget https://www.fpml.org/spec/fpml-5-10-7-rec-1/xsd/fpml-main-5-10.xsd

Note: Gunicorn is primarily for Unix systems. For Windows, use:
pip install waitress
waitress-serve --port=8000 soap_fpml_server:app

expected output
Family@DESKTOP-DS566KH MINGW64 ~/Documents/FpML-Messaging-Testing (main)
$ python soap_fpml_client.py
HTTP Status: 200
Response Body:
<ns0:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="urn:bank:fpml">
        <ns0:Body>
            <ns1:tradeConfirmation>
                <status>CONFIRMED</status>
                <tradeId>TRADE12345</tradeId>
            </ns1:tradeConfirmation>
        </ns0:Body>
    </ns0:Envelope>

Family@DESKTOP-DS566KH MINGW64 ~/Documents/FpML-Messaging-Testing (main)
$ 

Running server as follows
Family@DESKTOP-DS566KH MINGW64 ~/Documents/FpML-Messaging-Testing (main)
$ waitress-serve --port=6000 soap_fpml_server:app
INFO:waitress:Serving on http://0.0.0.0:6000

