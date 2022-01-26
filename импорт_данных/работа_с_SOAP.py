from zeep import Client


client = Client('http://www.dneonline.com/calculator.asmx?WSDL')
result = client.service.Add(2, 3)
print(result)
