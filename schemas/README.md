
The qbxmllib.py module in this package was generated from
the XML schemas in this directory.


there are several .xsd's files here, which originated from Quickbooks SDK, from validator & docs


I'm using qbxmlops120.xsd which automatically includes qbxml120.xsd, qbxmltypes120.xs, and qbxmlso120.xsd

Then I use generateDS to process the xsd, to generate a python file

NOTES: in the validator, there are several additional Quickbooks with different name like QBU,QBA,QBC,QBO
I think they meant:
QBU -> Quickbooks User
QBA -> stands for Quickbooks Accountant
QBC -> Quickbooks Client
those 3 are pretty close to each other

while QBO -> Quickbooks Online, which are somewhat different


NOTES:
because of the size of the xsd files, I need to reduce it first to include only element that I need. To do that, 
I created qbxmlops120_min.xsd, then prune qbxml, and prune QBXMLMsgRq so it only listed element that I need,
and then use ./reduce.sh to remove the dependency. Do not forget to rebuild !
I got the reducer from : http://www.abhortsoft.hu/xsdreducer/xsd_reducer.html

