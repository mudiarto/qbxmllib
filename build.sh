#
# require:
#  * generateDS: can be installed using pip install generateDS
#  * xsdreducer: already provided, need java to run
#

# reduce the schema
java -cp xsdreducer/XsdReducer.jar:xsdreducer/lib/xsom-20081112.jar:xsdreducer/lib/jaxb1-impl.jar xsdreducer.XsdReducer -sourceDir schemas/min -targetDir schemas/final -property schemas/qbxml_min.property -verbose


# I need to put external encoding since the data input will be encoded in utf8
generateDS.py -s qbxmllib/qbxmllib.py --subclass-suffix="" --super="qbxmlops120" -o qbxmllib/qbxmlops120.py --root-element="QBXML" --namespacedef="http://developer.intuit.com/" --external-encoding='utf-8' schemas/final/qbxmlops120_min.xsd



