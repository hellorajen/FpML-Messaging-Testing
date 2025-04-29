from flask import Flask, request, make_response
import xml.etree.ElementTree as ET

app = Flask(__name__)

SOAP_NS = {
    'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    'fpml': 'http://www.fpml.org/FpML-5/confirmation'
}

@app.route('/fpml', methods=['POST'])
def handle_fpml():
    # Parse SOAP envelope
    try:
        soap_xml = ET.fromstring(request.data)
        fpml = soap_xml.find('.//fpml:FpML', SOAP_NS)
        
        if fpml is None:
            return _soap_error("Missing FpML payload"), 400
            
        if not _validate_fpml(fpml):
            return _soap_error("Invalid FpML"), 400
            
        # Process trade (mock example)
        trade_id = fpml.find('.//fpml:tradeId', SOAP_NS).text
        return _soap_response(f"""
            <ns2:tradeConfirmation xmlns:ns2="urn:bank:fpml">
                <status>CONFIRMED</status>
                <tradeId>{trade_id}</tradeId>
            </ns2:tradeConfirmation>
        """)
        
    except ET.ParseError:
        return _soap_error("Malformed XML"), 400

def _validate_fpml(fpml_element):
    """Basic FpML validation"""
    required = ['tradeHeader', 'swap']
    return all(fpml_element.find(f'.//fpml:{tag}', SOAP_NS) is not None for tag in required)

def _soap_response(body):
    """Wrap response in SOAP envelope"""
    response = f"""<?xml version="1.0"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>{body}</soap:Body>
    </soap:Envelope>"""
    return make_response(response, 200, {'Content-Type': 'text/xml'})

def _soap_error(message):
    """SOAP fault response"""
    return f"""<?xml version="1.0"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <soap:Fault>
                <faultcode>soap:Client</faultcode>
                <faultstring>{message}</faultstring>
            </soap:Fault>
        </soap:Body>
    </soap:Envelope>""", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)