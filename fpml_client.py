import socket

def create_interest_rate_swap():
    return """<FpML xmlns="http://www.fpml.org/FpML-5/confirmation" version="5-10">
  <trade>
    <tradeHeader>
      <partyTradeIdentifier>
        <partyReference href="party1"/>
        <tradeId>TRADE12345</tradeId>
      </partyTradeIdentifier>
      <tradeDate>2024-05-30</tradeDate>
    </tradeHeader>
    <swap>
      <interestRateSwap>
        <effectiveDate>2024-06-03</effectiveDate>
        <fixedLeg>
          <paymentAmount>
            <currency>USD</currency>
            <amount>1000000</amount>
          </paymentAmount>
          <dayCountFraction>ACT/360</dayCountFraction>
          <fixedRate>5.25</fixedRate>
        </fixedLeg>
        <floatingLeg>
          <floatingRateIndex>LIBOR</floatingRateIndex>
          <indexTenor>6M</indexTenor>
        </floatingLeg>
      </interestRateSwap>
    </swap>
  </trade>
</FpML>"""

def send_fpml_message():
    fpml_msg = create_interest_rate_swap()
    
    with socket.socket() as sock:
        sock.connect(('localhost', 6000))
        sock.sendall(fpml_msg.encode('utf-8'))
        response = sock.recv(1024)
        print(f"Server response: {response.decode()}")
        print(f"Sent FpML (truncated):\n{fpml_msg[:200]}...")

if __name__ == "__main__":
    send_fpml_message()