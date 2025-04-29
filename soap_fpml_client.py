import requests
from xml.etree import ElementTree as ET

def create_soap_envelope(fpml_payload):
    return f"""<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
    <soap:Header>
        <wsse:Security>
            <wsse:UsernameToken>
                <wsse:Username>your_username</wsse:Username>
                <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">your_password</wsse:Password>
            </wsse:UsernameToken>
        </wsse:Security>
    </soap:Header>
    <soap:Body>
        {fpml_payload}
    </soap:Body>
</soap:Envelope>"""

def send_interest_rate_swap():
    fpml = """<FpML xmlns="http://www.fpml.org/FpML-5/confirmation" version="5-10">
        <trade>
            <tradeHeader>
                <partyTradeIdentifier>
                    <partyReference href="party1"/>
                    <tradeId>TRADE12345</tradeId>
                </partyTradeIdentifier>
            </tradeHeader>
            <swap><!-- Swap details here --></swap>
        </trade>
    </FpML>"""
    
    soap_msg = create_soap_envelope(fpml)
    headers = {'Content-Type': 'text/xml'}
    
    response = requests.post(
        'http://localhost:6000/fpml',
        data=soap_msg,
        headers=headers
    )
    
    print(f"HTTP Status: {response.status_code}")
    print("Response Body:")
    print(ET.tostring(ET.fromstring(response.text), encoding='unicode'))

if __name__ == '__main__':
    send_interest_rate_swap()