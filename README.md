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


Customization
=============

I found out that including the complete QBXML scheme will make a huge python files, which require a lot of memory.
In my case - I am using Google AppEngine - the full QBXML schema won't fit on the memory. I need to customize it to reduce the size.

That's where the xsdreducer comes into play. xsdreducer allow me to cut all unnecessary and unused branches just by commenting
out all the parents that are not used.

To customize it, edit qbxmlops120_min.xsd, and then find: ```<xsd:element name="QBXMLMsgsRq">``` and ```<xsd:element name="QBXMLMsgsRs">``,
and then comment out all unnecessary elements that you don't use in your case.


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
    * You can find the .XSD schema files in the QuickBooks SDK. You should download and install the QuickBooks SDK, then Browse to: C:\Program Files\Intuit\IDN\Common\tools\validator\

* generateDS:
  * https://pypi.python.org/pypi/generateDS or  http://www.davekuhlman.org/generateDS.html
    * Install using: `pip install generateDS`

* xsdreducer:
  * http://www.abhortsoft.hu/xsdreducer/xsd_reducer.html





