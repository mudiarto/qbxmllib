
===============================================================
qbxmllib
===============================================================

Description
=============

Python QBXML API generated from qbxml schemas

usage example :

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




Contents
==========

- ./schemas/ -- The XML schemas from which these modules
  (qbxmllib.py etc) were generated.

- qbxmllib/qbxmllib.py -- The qbxml data bindings generated from
  the qbxml XML schema.

- qbxmllib/qbxmlutils.py -- Utility functions etc. for use with the
  qbxmllib module.



History
=========





Credits
=========

* QBXML:
  * from Intuit
  * see: http://developer.intuit.com/qbsdk-current/common/newosr/index.html.
    You can find the .XSD schema files in the QuickBooks SDK. You should download and install the QuickBooks SDK,
    then Browse to: C:\Program Files\Intuit\IDN\Common\tools\validator\

* generateDS:
  * http://www.rexx.com/~dkuhlman/generateDS.html

* xsdreducer:
  * http://www.abhortsoft.hu/xsdreducer/xsd_reducer.html





