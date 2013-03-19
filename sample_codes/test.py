import StringIO
from qbxmllib import qbxmllib as qbxml

# generating qbxml
root = (
    qbxml.QBXML(
        QBXMLMsgsRq=qbxml.QBXMLMsgsRq(
            onError="stopOnError",
            CompanyQueryRq=[qbxml.CompanyQueryRqType(
                IncludeRetElement=["CompanyName", "Address"],
                OwnerID=["0", "1"],
            )]
        )
    )
)

output = StringIO.StringIO()
output.write('<?xml version="1.0" encoding="utf-8"?><?qbxml version="11.0" ?>') # NOTE: somehow required by qbwc
root.export(output, 0, pretty_print=False)
result = output.getvalue()
output.close()

print result

# parsing qbxml
from qbxmllib.qbxmlutils import parseString

root2 = parseString(result)
print root2.QBXMLMsgsRq.CompanyQueryRq[0].OwnerID






