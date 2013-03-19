#!/usr/bin/env python

#
# Generated Tue Mar 19 12:18:17 2013 by generateDS.py version 2.7c.
#

import sys

import qbxmlops120 as supermod

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#

class QBXMLMsgsRq(supermod.QBXMLMsgsRq):
    def __init__(self, onError=None, responseData='includeAll', oldMessageSetID=None, newMessageSetID=None, HostQueryRq=None, CompanyQueryRq=None, AccountQueryRq=None, CustomerAddRq=None, CustomerModRq=None, CustomerQueryRq=None, ItemInventoryAddRq=None, ItemInventoryModRq=None, ItemInventoryQueryRq=None, ItemQueryRq=None, SalesReceiptAddRq=None, SalesReceiptModRq=None, SalesReceiptQueryRq=None):
        super(QBXMLMsgsRq, self).__init__(onError, responseData, oldMessageSetID, newMessageSetID, HostQueryRq, CompanyQueryRq, AccountQueryRq, CustomerAddRq, CustomerModRq, CustomerQueryRq, ItemInventoryAddRq, ItemInventoryModRq, ItemInventoryQueryRq, ItemQueryRq, SalesReceiptAddRq, SalesReceiptModRq, SalesReceiptQueryRq, )
supermod.QBXMLMsgsRq.subclass = QBXMLMsgsRq
# end class QBXMLMsgsRq


class QBXMLMsgsRs(supermod.QBXMLMsgsRs):
    def __init__(self, newMessageSetID=None, messageSetStatusCode=None, HostQueryRs=None, CompanyQueryRs=None, CustomerAddRs=None, CustomerModRs=None, CustomerQueryRs=None, ItemInventoryAddRs=None, ItemInventoryModRs=None, ItemInventoryQueryRs=None, ItemQueryRs=None, SalesReceiptAddRs=None, SalesReceiptModRs=None, SalesReceiptQueryRs=None):
        super(QBXMLMsgsRs, self).__init__(newMessageSetID, messageSetStatusCode, HostQueryRs, CompanyQueryRs, CustomerAddRs, CustomerModRs, CustomerQueryRs, ItemInventoryAddRs, ItemInventoryModRs, ItemInventoryQueryRs, ItemQueryRs, SalesReceiptAddRs, SalesReceiptModRs, SalesReceiptQueryRs, )
supermod.QBXMLMsgsRs.subclass = QBXMLMsgsRs
# end class QBXMLMsgsRs


class HostQueryRqType(supermod.HostQueryRqType):
    def __init__(self, requestID=None, IncludeListMetaData=None, IncludeRetElement=None):
        super(HostQueryRqType, self).__init__(requestID, IncludeListMetaData, IncludeRetElement, )
supermod.HostQueryRqType.subclass = HostQueryRqType
# end class HostQueryRqType


class CompanyQueryRqType(supermod.CompanyQueryRqType):
    def __init__(self, requestID=None, IncludeRetElement=None, OwnerID=None):
        super(CompanyQueryRqType, self).__init__(requestID, IncludeRetElement, OwnerID, )
supermod.CompanyQueryRqType.subclass = CompanyQueryRqType
# end class CompanyQueryRqType


class AccountQueryRqType(supermod.AccountQueryRqType):
    def __init__(self, requestID=None, metaData='NoMetaData', ListID=None, FullName=None, MaxReturned=None, ActiveStatus=None, FromModifiedDate=None, ToModifiedDate=None, NameFilter=None, NameRangeFilter=None, AccountType=None, CurrencyFilter=None, IncludeRetElement=None, OwnerID=None):
        super(AccountQueryRqType, self).__init__(requestID, metaData, ListID, FullName, MaxReturned, ActiveStatus, FromModifiedDate, ToModifiedDate, NameFilter, NameRangeFilter, AccountType, CurrencyFilter, IncludeRetElement, OwnerID, )
supermod.AccountQueryRqType.subclass = AccountQueryRqType
# end class AccountQueryRqType


class CustomerAddRqType(supermod.CustomerAddRqType):
    def __init__(self, requestID=None, CustomerAdd=None, IncludeRetElement=None):
        super(CustomerAddRqType, self).__init__(requestID, CustomerAdd, IncludeRetElement, )
supermod.CustomerAddRqType.subclass = CustomerAddRqType
# end class CustomerAddRqType


class CustomerModRqType(supermod.CustomerModRqType):
    def __init__(self, requestID=None, CustomerMod=None, IncludeRetElement=None):
        super(CustomerModRqType, self).__init__(requestID, CustomerMod, IncludeRetElement, )
supermod.CustomerModRqType.subclass = CustomerModRqType
# end class CustomerModRqType


class CustomerQueryRqType(supermod.CustomerQueryRqType):
    def __init__(self, iteratorID=None, requestID=None, iterator=None, metaData='NoMetaData', ListID=None, FullName=None, MaxReturned=None, ActiveStatus=None, FromModifiedDate=None, ToModifiedDate=None, NameFilter=None, NameRangeFilter=None, TotalBalanceFilter=None, CurrencyFilter=None, ClassFilter=None, IncludeRetElement=None, OwnerID=None):
        super(CustomerQueryRqType, self).__init__(iteratorID, requestID, iterator, metaData, ListID, FullName, MaxReturned, ActiveStatus, FromModifiedDate, ToModifiedDate, NameFilter, NameRangeFilter, TotalBalanceFilter, CurrencyFilter, ClassFilter, IncludeRetElement, OwnerID, )
supermod.CustomerQueryRqType.subclass = CustomerQueryRqType
# end class CustomerQueryRqType


class ItemInventoryAddRqType(supermod.ItemInventoryAddRqType):
    def __init__(self, requestID=None, ItemInventoryAdd=None, IncludeRetElement=None):
        super(ItemInventoryAddRqType, self).__init__(requestID, ItemInventoryAdd, IncludeRetElement, )
supermod.ItemInventoryAddRqType.subclass = ItemInventoryAddRqType
# end class ItemInventoryAddRqType


class ItemInventoryModRqType(supermod.ItemInventoryModRqType):
    def __init__(self, requestID=None, ItemInventoryMod=None, IncludeRetElement=None):
        super(ItemInventoryModRqType, self).__init__(requestID, ItemInventoryMod, IncludeRetElement, )
supermod.ItemInventoryModRqType.subclass = ItemInventoryModRqType
# end class ItemInventoryModRqType


class ItemInventoryQueryRqType(supermod.ItemInventoryQueryRqType):
    def __init__(self, iteratorID=None, requestID=None, iterator=None, metaData='NoMetaData', ListID=None, FullName=None, MaxReturned=None, ActiveStatus=None, FromModifiedDate=None, ToModifiedDate=None, NameFilter=None, NameRangeFilter=None, ClassFilter=None, IncludeRetElement=None, OwnerID=None):
        super(ItemInventoryQueryRqType, self).__init__(iteratorID, requestID, iterator, metaData, ListID, FullName, MaxReturned, ActiveStatus, FromModifiedDate, ToModifiedDate, NameFilter, NameRangeFilter, ClassFilter, IncludeRetElement, OwnerID, )
supermod.ItemInventoryQueryRqType.subclass = ItemInventoryQueryRqType
# end class ItemInventoryQueryRqType


class ItemQueryRqType(supermod.ItemQueryRqType):
    def __init__(self, iteratorID=None, requestID=None, iterator=None, metaData='NoMetaData', ListID=None, FullName=None, MaxReturned=None, ActiveStatus=None, FromModifiedDate=None, ToModifiedDate=None, NameFilter=None, NameRangeFilter=None, IncludeRetElement=None, OwnerID=None):
        super(ItemQueryRqType, self).__init__(iteratorID, requestID, iterator, metaData, ListID, FullName, MaxReturned, ActiveStatus, FromModifiedDate, ToModifiedDate, NameFilter, NameRangeFilter, IncludeRetElement, OwnerID, )
supermod.ItemQueryRqType.subclass = ItemQueryRqType
# end class ItemQueryRqType


class SalesReceiptAddRqType(supermod.SalesReceiptAddRqType):
    def __init__(self, requestID=None, SalesReceiptAdd=None, IncludeRetElement=None):
        super(SalesReceiptAddRqType, self).__init__(requestID, SalesReceiptAdd, IncludeRetElement, )
supermod.SalesReceiptAddRqType.subclass = SalesReceiptAddRqType
# end class SalesReceiptAddRqType


class SalesReceiptModRqType(supermod.SalesReceiptModRqType):
    def __init__(self, requestID=None, SalesReceiptMod=None, IncludeRetElement=None):
        super(SalesReceiptModRqType, self).__init__(requestID, SalesReceiptMod, IncludeRetElement, )
supermod.SalesReceiptModRqType.subclass = SalesReceiptModRqType
# end class SalesReceiptModRqType


class SalesReceiptQueryRqType(supermod.SalesReceiptQueryRqType):
    def __init__(self, iteratorID=None, requestID=None, iterator=None, metaData='NoMetaData', TxnID=None, RefNumber=None, RefNumberCaseSensitive=None, MaxReturned=None, ModifiedDateRangeFilter=None, TxnDateRangeFilter=None, EntityFilter=None, AccountFilter=None, RefNumberFilter=None, RefNumberRangeFilter=None, CurrencyFilter=None, IncludeLineItems=None, IncludeRetElement=None, OwnerID=None):
        super(SalesReceiptQueryRqType, self).__init__(iteratorID, requestID, iterator, metaData, TxnID, RefNumber, RefNumberCaseSensitive, MaxReturned, ModifiedDateRangeFilter, TxnDateRangeFilter, EntityFilter, AccountFilter, RefNumberFilter, RefNumberRangeFilter, CurrencyFilter, IncludeLineItems, IncludeRetElement, OwnerID, )
supermod.SalesReceiptQueryRqType.subclass = SalesReceiptQueryRqType
# end class SalesReceiptQueryRqType


class HostQueryRsType(supermod.HostQueryRsType):
    def __init__(self, statusSeverity=None, requestID=None, statusMessage=None, statusCode=None, HostRet=None):
        super(HostQueryRsType, self).__init__(statusSeverity, requestID, statusMessage, statusCode, HostRet, )
supermod.HostQueryRsType.subclass = HostQueryRsType
# end class HostQueryRsType


class CompanyQueryRsType(supermod.CompanyQueryRsType):
    def __init__(self, statusSeverity=None, requestID=None, statusMessage=None, statusCode=None, CompanyRet=None):
        super(CompanyQueryRsType, self).__init__(statusSeverity, requestID, statusMessage, statusCode, CompanyRet, )
supermod.CompanyQueryRsType.subclass = CompanyQueryRsType
# end class CompanyQueryRsType


class CustomerAddRsType(supermod.CustomerAddRsType):
    def __init__(self, statusSeverity=None, requestID=None, statusMessage=None, statusCode=None, CustomerRet=None, ErrorRecovery=None):
        super(CustomerAddRsType, self).__init__(statusSeverity, requestID, statusMessage, statusCode, CustomerRet, ErrorRecovery, )
supermod.CustomerAddRsType.subclass = CustomerAddRsType
# end class CustomerAddRsType


class CustomerModRsType(supermod.CustomerModRsType):
    def __init__(self, statusSeverity=None, requestID=None, statusMessage=None, statusCode=None, CustomerRet=None, ErrorRecovery=None):
        super(CustomerModRsType, self).__init__(statusSeverity, requestID, statusMessage, statusCode, CustomerRet, ErrorRecovery, )
supermod.CustomerModRsType.subclass = CustomerModRsType
# end class CustomerModRsType


class CustomerQueryRsType(supermod.CustomerQueryRsType):
    def __init__(self, iteratorID=None, iteratorRemainingCount=None, statusSeverity=None, retCount=None, requestID=None, statusMessage=None, statusCode=None, CustomerRet=None):
        super(CustomerQueryRsType, self).__init__(iteratorID, iteratorRemainingCount, statusSeverity, retCount, requestID, statusMessage, statusCode, CustomerRet, )
supermod.CustomerQueryRsType.subclass = CustomerQueryRsType
# end class CustomerQueryRsType


class ItemInventoryAddRsType(supermod.ItemInventoryAddRsType):
    def __init__(self, statusSeverity=None, requestID=None, statusMessage=None, statusCode=None, ItemInventoryRet=None, ErrorRecovery=None):
        super(ItemInventoryAddRsType, self).__init__(statusSeverity, requestID, statusMessage, statusCode, ItemInventoryRet, ErrorRecovery, )
supermod.ItemInventoryAddRsType.subclass = ItemInventoryAddRsType
# end class ItemInventoryAddRsType


class ItemInventoryModRsType(supermod.ItemInventoryModRsType):
    def __init__(self, statusSeverity=None, requestID=None, statusMessage=None, statusCode=None, ItemInventoryRet=None, ErrorRecovery=None):
        super(ItemInventoryModRsType, self).__init__(statusSeverity, requestID, statusMessage, statusCode, ItemInventoryRet, ErrorRecovery, )
supermod.ItemInventoryModRsType.subclass = ItemInventoryModRsType
# end class ItemInventoryModRsType


class ItemInventoryQueryRsType(supermod.ItemInventoryQueryRsType):
    def __init__(self, iteratorID=None, iteratorRemainingCount=None, statusSeverity=None, retCount=None, requestID=None, statusMessage=None, statusCode=None, ItemInventoryRet=None):
        super(ItemInventoryQueryRsType, self).__init__(iteratorID, iteratorRemainingCount, statusSeverity, retCount, requestID, statusMessage, statusCode, ItemInventoryRet, )
supermod.ItemInventoryQueryRsType.subclass = ItemInventoryQueryRsType
# end class ItemInventoryQueryRsType


class ItemQueryRsType(supermod.ItemQueryRsType):
    def __init__(self, iteratorID=None, iteratorRemainingCount=None, statusSeverity=None, retCount=None, requestID=None, statusMessage=None, statusCode=None, ItemServiceRet=None, ItemNonInventoryRet=None, ItemOtherChargeRet=None, ItemInventoryRet=None, ItemInventoryAssemblyRet=None, ItemFixedAssetRet=None, ItemSubtotalRet=None, ItemDiscountRet=None, ItemPaymentRet=None, ItemSalesTaxRet=None, ItemSalesTaxGroupRet=None, ItemGroupRet=None):
        super(ItemQueryRsType, self).__init__(iteratorID, iteratorRemainingCount, statusSeverity, retCount, requestID, statusMessage, statusCode, ItemServiceRet, ItemNonInventoryRet, ItemOtherChargeRet, ItemInventoryRet, ItemInventoryAssemblyRet, ItemFixedAssetRet, ItemSubtotalRet, ItemDiscountRet, ItemPaymentRet, ItemSalesTaxRet, ItemSalesTaxGroupRet, ItemGroupRet, )
supermod.ItemQueryRsType.subclass = ItemQueryRsType
# end class ItemQueryRsType


class SalesReceiptAddRsType(supermod.SalesReceiptAddRsType):
    def __init__(self, statusSeverity=None, requestID=None, statusMessage=None, statusCode=None, SalesReceiptRet=None, ErrorRecovery=None):
        super(SalesReceiptAddRsType, self).__init__(statusSeverity, requestID, statusMessage, statusCode, SalesReceiptRet, ErrorRecovery, )
supermod.SalesReceiptAddRsType.subclass = SalesReceiptAddRsType
# end class SalesReceiptAddRsType


class SalesReceiptModRsType(supermod.SalesReceiptModRsType):
    def __init__(self, statusSeverity=None, requestID=None, statusMessage=None, statusCode=None, SalesReceiptRet=None, ErrorRecovery=None):
        super(SalesReceiptModRsType, self).__init__(statusSeverity, requestID, statusMessage, statusCode, SalesReceiptRet, ErrorRecovery, )
supermod.SalesReceiptModRsType.subclass = SalesReceiptModRsType
# end class SalesReceiptModRsType


class SalesReceiptQueryRsType(supermod.SalesReceiptQueryRsType):
    def __init__(self, iteratorID=None, iteratorRemainingCount=None, statusSeverity=None, retCount=None, requestID=None, statusMessage=None, statusCode=None, SalesReceiptRet=None):
        super(SalesReceiptQueryRsType, self).__init__(iteratorID, iteratorRemainingCount, statusSeverity, retCount, requestID, statusMessage, statusCode, SalesReceiptRet, )
supermod.SalesReceiptQueryRsType.subclass = SalesReceiptQueryRsType
# end class SalesReceiptQueryRsType


class QBXML(supermod.QBXML):
    def __init__(self, SignonMsgsRq=None, QBXMLMsgsRq=None, SignonMsgsRs=None, QBXMLMsgsRs=None):
        super(QBXML, self).__init__(SignonMsgsRq, QBXMLMsgsRq, SignonMsgsRs, QBXMLMsgsRs, )
supermod.QBXML.subclass = QBXML
# end class QBXML


class FirstMonthFiscalYear(supermod.FirstMonthFiscalYear):
    def __init__(self, valueOf_=None):
        super(FirstMonthFiscalYear, self).__init__()
supermod.FirstMonthFiscalYear.subclass = FirstMonthFiscalYear
# end class FirstMonthFiscalYear


class FirstMonthIncomeTaxYear(supermod.FirstMonthIncomeTaxYear):
    def __init__(self, valueOf_=None):
        super(FirstMonthIncomeTaxYear, self).__init__()
supermod.FirstMonthIncomeTaxYear.subclass = FirstMonthIncomeTaxYear
# end class FirstMonthIncomeTaxYear


class ExpirationMonth(supermod.ExpirationMonth):
    def __init__(self, valueOf_=None):
        super(ExpirationMonth, self).__init__()
supermod.ExpirationMonth.subclass = ExpirationMonth
# end class ExpirationMonth


class AVSStreet(supermod.AVSStreet):
    def __init__(self, valueOf_=None):
        super(AVSStreet, self).__init__()
supermod.AVSStreet.subclass = AVSStreet
# end class AVSStreet


class AVSZip(supermod.AVSZip):
    def __init__(self, valueOf_=None):
        super(AVSZip, self).__init__()
supermod.AVSZip.subclass = AVSZip
# end class AVSZip


class CardSecurityCodeMatch(supermod.CardSecurityCodeMatch):
    def __init__(self, valueOf_=None):
        super(CardSecurityCodeMatch, self).__init__()
supermod.CardSecurityCodeMatch.subclass = CardSecurityCodeMatch
# end class CardSecurityCodeMatch


class PaymentStatus(supermod.PaymentStatus):
    def __init__(self, valueOf_=None):
        super(PaymentStatus, self).__init__()
supermod.PaymentStatus.subclass = PaymentStatus
# end class PaymentStatus


class TransactionMode(supermod.TransactionMode):
    def __init__(self, valueOf_=None):
        super(TransactionMode, self).__init__()
supermod.TransactionMode.subclass = TransactionMode
# end class TransactionMode


class JobStatus(supermod.JobStatus):
    def __init__(self, valueOf_=None):
        super(JobStatus, self).__init__()
supermod.JobStatus.subclass = JobStatus
# end class JobStatus


class DeliveryMethod(supermod.DeliveryMethod):
    def __init__(self, valueOf_=None):
        super(DeliveryMethod, self).__init__()
supermod.DeliveryMethod.subclass = DeliveryMethod
# end class DeliveryMethod


class TaxForm(supermod.TaxForm):
    def __init__(self, valueOf_=None):
        super(TaxForm, self).__init__()
supermod.TaxForm.subclass = TaxForm
# end class TaxForm


class AcquiredAs(supermod.AcquiredAs):
    def __init__(self, valueOf_=None):
        super(AcquiredAs, self).__init__()
supermod.AcquiredAs.subclass = AcquiredAs
# end class AcquiredAs


class QBFileMode(supermod.QBFileMode):
    def __init__(self, valueOf_=None):
        super(QBFileMode, self).__init__()
supermod.QBFileMode.subclass = QBFileMode
# end class QBFileMode


class SpecialItemType(supermod.SpecialItemType):
    def __init__(self, valueOf_=None):
        super(SpecialItemType, self).__init__()
supermod.SpecialItemType.subclass = SpecialItemType
# end class SpecialItemType


class SalesTaxCountry(supermod.SalesTaxCountry):
    def __init__(self, valueOf_=None):
        super(SalesTaxCountry, self).__init__()
supermod.SalesTaxCountry.subclass = SalesTaxCountry
# end class SalesTaxCountry


class CreditCardTxnType(supermod.CreditCardTxnType):
    def __init__(self, valueOf_=None):
        super(CreditCardTxnType, self).__init__()
supermod.CreditCardTxnType.subclass = CreditCardTxnType
# end class CreditCardTxnType


class ServiceStatus(supermod.ServiceStatus):
    def __init__(self, valueOf_=None):
        super(ServiceStatus, self).__init__()
supermod.ServiceStatus.subclass = ServiceStatus
# end class ServiceStatus


class PreferredDeliveryMethod(supermod.PreferredDeliveryMethod):
    def __init__(self, valueOf_=None):
        super(PreferredDeliveryMethod, self).__init__()
supermod.PreferredDeliveryMethod.subclass = PreferredDeliveryMethod
# end class PreferredDeliveryMethod


class DataExtType(supermod.DataExtType):
    def __init__(self, valueOf_=None):
        super(DataExtType, self).__init__()
supermod.DataExtType.subclass = DataExtType
# end class DataExtType


class ParentRef(supermod.ParentRef):
    def __init__(self, ListID=None, FullName=None):
        super(ParentRef, self).__init__(ListID, FullName, )
supermod.ParentRef.subclass = ParentRef
# end class ParentRef


class CustomerRef(supermod.CustomerRef):
    def __init__(self, ListID=None, FullName=None):
        super(CustomerRef, self).__init__(ListID, FullName, )
supermod.CustomerRef.subclass = CustomerRef
# end class CustomerRef


class ClassRef(supermod.ClassRef):
    def __init__(self, ListID=None, FullName=None):
        super(ClassRef, self).__init__(ListID, FullName, )
supermod.ClassRef.subclass = ClassRef
# end class ClassRef


class TermsRef(supermod.TermsRef):
    def __init__(self, ListID=None, FullName=None):
        super(TermsRef, self).__init__(ListID, FullName, )
supermod.TermsRef.subclass = TermsRef
# end class TermsRef


class SalesRepRef(supermod.SalesRepRef):
    def __init__(self, ListID=None, FullName=None):
        super(SalesRepRef, self).__init__(ListID, FullName, )
supermod.SalesRepRef.subclass = SalesRepRef
# end class SalesRepRef


class CustomerMsgRef(supermod.CustomerMsgRef):
    def __init__(self, ListID=None, FullName=None):
        super(CustomerMsgRef, self).__init__(ListID, FullName, )
supermod.CustomerMsgRef.subclass = CustomerMsgRef
# end class CustomerMsgRef


class ItemRef(supermod.ItemRef):
    def __init__(self, ListID=None, FullName=None):
        super(ItemRef, self).__init__(ListID, FullName, )
supermod.ItemRef.subclass = ItemRef
# end class ItemRef


class ItemGroupRef(supermod.ItemGroupRef):
    def __init__(self, ListID=None, FullName=None):
        super(ItemGroupRef, self).__init__(ListID, FullName, )
supermod.ItemGroupRef.subclass = ItemGroupRef
# end class ItemGroupRef


class ItemSalesTaxRef(supermod.ItemSalesTaxRef):
    def __init__(self, ListID=None, FullName=None):
        super(ItemSalesTaxRef, self).__init__(ListID, FullName, )
supermod.ItemSalesTaxRef.subclass = ItemSalesTaxRef
# end class ItemSalesTaxRef


class ItemInventoryRef(supermod.ItemInventoryRef):
    def __init__(self, ListID=None, FullName=None):
        super(ItemInventoryRef, self).__init__(ListID, FullName, )
supermod.ItemInventoryRef.subclass = ItemInventoryRef
# end class ItemInventoryRef


class AccountRef(supermod.AccountRef):
    def __init__(self, ListID=None, FullName=None):
        super(AccountRef, self).__init__(ListID, FullName, )
supermod.AccountRef.subclass = AccountRef
# end class AccountRef


class ExpenseAccountRef(supermod.ExpenseAccountRef):
    def __init__(self, ListID=None, FullName=None):
        super(ExpenseAccountRef, self).__init__(ListID, FullName, )
supermod.ExpenseAccountRef.subclass = ExpenseAccountRef
# end class ExpenseAccountRef


class PrefVendorRef(supermod.PrefVendorRef):
    def __init__(self, ListID=None, FullName=None):
        super(PrefVendorRef, self).__init__(ListID, FullName, )
supermod.PrefVendorRef.subclass = PrefVendorRef
# end class PrefVendorRef


class IncomeAccountRef(supermod.IncomeAccountRef):
    def __init__(self, ListID=None, FullName=None):
        super(IncomeAccountRef, self).__init__(ListID, FullName, )
supermod.IncomeAccountRef.subclass = IncomeAccountRef
# end class IncomeAccountRef


class COGSAccountRef(supermod.COGSAccountRef):
    def __init__(self, ListID=None, FullName=None):
        super(COGSAccountRef, self).__init__(ListID, FullName, )
supermod.COGSAccountRef.subclass = COGSAccountRef
# end class COGSAccountRef


class AssetAccountRef(supermod.AssetAccountRef):
    def __init__(self, ListID=None, FullName=None):
        super(AssetAccountRef, self).__init__(ListID, FullName, )
supermod.AssetAccountRef.subclass = AssetAccountRef
# end class AssetAccountRef


class DepositToAccountRef(supermod.DepositToAccountRef):
    def __init__(self, ListID=None, FullName=None):
        super(DepositToAccountRef, self).__init__(ListID, FullName, )
supermod.DepositToAccountRef.subclass = DepositToAccountRef
# end class DepositToAccountRef


class OverrideItemAccountRef(supermod.OverrideItemAccountRef):
    def __init__(self, ListID=None, FullName=None):
        super(OverrideItemAccountRef, self).__init__(ListID, FullName, )
supermod.OverrideItemAccountRef.subclass = OverrideItemAccountRef
# end class OverrideItemAccountRef


class TaxVendorRef(supermod.TaxVendorRef):
    def __init__(self, ListID=None, FullName=None):
        super(TaxVendorRef, self).__init__(ListID, FullName, )
supermod.TaxVendorRef.subclass = TaxVendorRef
# end class TaxVendorRef


class PaymentMethodRef(supermod.PaymentMethodRef):
    def __init__(self, ListID=None, FullName=None):
        super(PaymentMethodRef, self).__init__(ListID, FullName, )
supermod.PaymentMethodRef.subclass = PaymentMethodRef
# end class PaymentMethodRef


class PreferredPaymentMethodRef(supermod.PreferredPaymentMethodRef):
    def __init__(self, ListID=None, FullName=None):
        super(PreferredPaymentMethodRef, self).__init__(ListID, FullName, )
supermod.PreferredPaymentMethodRef.subclass = PreferredPaymentMethodRef
# end class PreferredPaymentMethodRef


class ShipMethodRef(supermod.ShipMethodRef):
    def __init__(self, ListID=None, FullName=None):
        super(ShipMethodRef, self).__init__(ListID, FullName, )
supermod.ShipMethodRef.subclass = ShipMethodRef
# end class ShipMethodRef


class CustomerTypeRef(supermod.CustomerTypeRef):
    def __init__(self, ListID=None, FullName=None):
        super(CustomerTypeRef, self).__init__(ListID, FullName, )
supermod.CustomerTypeRef.subclass = CustomerTypeRef
# end class CustomerTypeRef


class JobTypeRef(supermod.JobTypeRef):
    def __init__(self, ListID=None, FullName=None):
        super(JobTypeRef, self).__init__(ListID, FullName, )
supermod.JobTypeRef.subclass = JobTypeRef
# end class JobTypeRef


class SalesTaxCodeRef(supermod.SalesTaxCodeRef):
    def __init__(self, ListID=None, FullName=None):
        super(SalesTaxCodeRef, self).__init__(ListID, FullName, )
supermod.SalesTaxCodeRef.subclass = SalesTaxCodeRef
# end class SalesTaxCodeRef


class CustomerSalesTaxCodeRef(supermod.CustomerSalesTaxCodeRef):
    def __init__(self, ListID=None, FullName=None):
        super(CustomerSalesTaxCodeRef, self).__init__(ListID, FullName, )
supermod.CustomerSalesTaxCodeRef.subclass = CustomerSalesTaxCodeRef
# end class CustomerSalesTaxCodeRef


class TemplateRef(supermod.TemplateRef):
    def __init__(self, ListID=None, FullName=None):
        super(TemplateRef, self).__init__(ListID, FullName, )
supermod.TemplateRef.subclass = TemplateRef
# end class TemplateRef


class PriceLevelRef(supermod.PriceLevelRef):
    def __init__(self, ListID=None, FullName=None):
        super(PriceLevelRef, self).__init__(ListID, FullName, )
supermod.PriceLevelRef.subclass = PriceLevelRef
# end class PriceLevelRef


class PurchaseTaxCodeRef(supermod.PurchaseTaxCodeRef):
    def __init__(self, ListID=None, FullName=None):
        super(PurchaseTaxCodeRef, self).__init__(ListID, FullName, )
supermod.PurchaseTaxCodeRef.subclass = PurchaseTaxCodeRef
# end class PurchaseTaxCodeRef


class UnitOfMeasureSetRef(supermod.UnitOfMeasureSetRef):
    def __init__(self, ListID=None, FullName=None):
        super(UnitOfMeasureSetRef, self).__init__(ListID, FullName, )
supermod.UnitOfMeasureSetRef.subclass = UnitOfMeasureSetRef
# end class UnitOfMeasureSetRef


class OverrideUOMSetRef(supermod.OverrideUOMSetRef):
    def __init__(self, ListID=None, FullName=None):
        super(OverrideUOMSetRef, self).__init__(ListID, FullName, )
supermod.OverrideUOMSetRef.subclass = OverrideUOMSetRef
# end class OverrideUOMSetRef


class SalesTaxReturnLineRef(supermod.SalesTaxReturnLineRef):
    def __init__(self, ListID=None, FullName=None):
        super(SalesTaxReturnLineRef, self).__init__(ListID, FullName, )
supermod.SalesTaxReturnLineRef.subclass = SalesTaxReturnLineRef
# end class SalesTaxReturnLineRef


class CurrencyRef(supermod.CurrencyRef):
    def __init__(self, ListID=None, FullName=None):
        super(CurrencyRef, self).__init__(ListID, FullName, )
supermod.CurrencyRef.subclass = CurrencyRef
# end class CurrencyRef


class InventorySiteRef(supermod.InventorySiteRef):
    def __init__(self, ListID=None, FullName=None):
        super(InventorySiteRef, self).__init__(ListID, FullName, )
supermod.InventorySiteRef.subclass = InventorySiteRef
# end class InventorySiteRef


class InventorySiteLocationRef(supermod.InventorySiteLocationRef):
    def __init__(self, ListID=None, FullName=None):
        super(InventorySiteLocationRef, self).__init__(ListID, FullName, )
supermod.InventorySiteLocationRef.subclass = InventorySiteLocationRef
# end class InventorySiteLocationRef


class Address(supermod.Address):
    def __init__(self, Addr1=None, Addr2=None, Addr3=None, Addr4=None, Addr5=None, City=None, State=None, PostalCode=None, Country=None, Note=None):
        super(Address, self).__init__(Addr1, Addr2, Addr3, Addr4, Addr5, City, State, PostalCode, Country, Note, )
supermod.Address.subclass = Address
# end class Address


class AddressBlock(supermod.AddressBlock):
    def __init__(self, Addr1=None, Addr2=None, Addr3=None, Addr4=None, Addr5=None):
        super(AddressBlock, self).__init__(Addr1, Addr2, Addr3, Addr4, Addr5, )
supermod.AddressBlock.subclass = AddressBlock
# end class AddressBlock


class ShipAddress(supermod.ShipAddress):
    def __init__(self, Addr1=None, Addr2=None, Addr3=None, Addr4=None, Addr5=None, City=None, State=None, PostalCode=None, Country=None, Note=None):
        super(ShipAddress, self).__init__(Addr1, Addr2, Addr3, Addr4, Addr5, City, State, PostalCode, Country, Note, )
supermod.ShipAddress.subclass = ShipAddress
# end class ShipAddress


class ShipAddressBlock(supermod.ShipAddressBlock):
    def __init__(self, Addr1=None, Addr2=None, Addr3=None, Addr4=None, Addr5=None):
        super(ShipAddressBlock, self).__init__(Addr1, Addr2, Addr3, Addr4, Addr5, )
supermod.ShipAddressBlock.subclass = ShipAddressBlock
# end class ShipAddressBlock


class LegalAddress(supermod.LegalAddress):
    def __init__(self, Addr1=None, Addr2=None, Addr3=None, Addr4=None, Addr5=None, City=None, State=None, PostalCode=None, Country=None, Note=None):
        super(LegalAddress, self).__init__(Addr1, Addr2, Addr3, Addr4, Addr5, City, State, PostalCode, Country, Note, )
supermod.LegalAddress.subclass = LegalAddress
# end class LegalAddress


class BillAddress(supermod.BillAddress):
    def __init__(self, Addr1=None, Addr2=None, Addr3=None, Addr4=None, Addr5=None, City=None, State=None, PostalCode=None, Country=None, Note=None):
        super(BillAddress, self).__init__(Addr1, Addr2, Addr3, Addr4, Addr5, City, State, PostalCode, Country, Note, )
supermod.BillAddress.subclass = BillAddress
# end class BillAddress


class BillAddressBlock(supermod.BillAddressBlock):
    def __init__(self, Addr1=None, Addr2=None, Addr3=None, Addr4=None, Addr5=None):
        super(BillAddressBlock, self).__init__(Addr1, Addr2, Addr3, Addr4, Addr5, )
supermod.BillAddressBlock.subclass = BillAddressBlock
# end class BillAddressBlock


class CompanyAddressForCustomer(supermod.CompanyAddressForCustomer):
    def __init__(self, Addr1=None, Addr2=None, Addr3=None, Addr4=None, Addr5=None, City=None, State=None, PostalCode=None, Country=None, Note=None):
        super(CompanyAddressForCustomer, self).__init__(Addr1, Addr2, Addr3, Addr4, Addr5, City, State, PostalCode, Country, Note, )
supermod.CompanyAddressForCustomer.subclass = CompanyAddressForCustomer
# end class CompanyAddressForCustomer


class CompanyAddressBlockForCustomer(supermod.CompanyAddressBlockForCustomer):
    def __init__(self, Addr1=None, Addr2=None, Addr3=None, Addr4=None, Addr5=None):
        super(CompanyAddressBlockForCustomer, self).__init__(Addr1, Addr2, Addr3, Addr4, Addr5, )
supermod.CompanyAddressBlockForCustomer.subclass = CompanyAddressBlockForCustomer
# end class CompanyAddressBlockForCustomer


class ShipToAddress(supermod.ShipToAddress):
    def __init__(self, Name=None, Addr1=None, Addr2=None, Addr3=None, Addr4=None, Addr5=None, City=None, State=None, PostalCode=None, Country=None, Note=None, DefaultShipTo=None):
        super(ShipToAddress, self).__init__(Name, Addr1, Addr2, Addr3, Addr4, Addr5, City, State, PostalCode, Country, Note, DefaultShipTo, )
supermod.ShipToAddress.subclass = ShipToAddress
# end class ShipToAddress


class AdditionalContactRef(supermod.AdditionalContactRef):
    def __init__(self, ContactName=None, ContactValue=None):
        super(AdditionalContactRef, self).__init__(ContactName, ContactValue, )
supermod.AdditionalContactRef.subclass = AdditionalContactRef
# end class AdditionalContactRef


class BarCode(supermod.BarCode):
    def __init__(self, BarCodeValue=None, AssignEvenIfUsed=None, AllowOverride=None):
        super(BarCode, self).__init__(BarCodeValue, AssignEvenIfUsed, AllowOverride, )
supermod.BarCode.subclass = BarCode
# end class BarCode


class Contacts(supermod.Contacts):
    def __init__(self, Salutation=None, FirstName=None, MiddleName=None, LastName=None, JobTitle=None, AdditionalContactRef=None):
        super(Contacts, self).__init__(Salutation, FirstName, MiddleName, LastName, JobTitle, AdditionalContactRef, )
supermod.Contacts.subclass = Contacts
# end class Contacts


class ContactsMod(supermod.ContactsMod):
    def __init__(self, ListID=None, EditSequence=None, Salutation=None, FirstName=None, MiddleName=None, LastName=None, JobTitle=None, AdditionalContactRef=None):
        super(ContactsMod, self).__init__(ListID, EditSequence, Salutation, FirstName, MiddleName, LastName, JobTitle, AdditionalContactRef, )
supermod.ContactsMod.subclass = ContactsMod
# end class ContactsMod


class ContactsRet(supermod.ContactsRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Contact=None, Salutation=None, FirstName=None, MiddleName=None, LastName=None, JobTitle=None, AdditionalContactRef=None):
        super(ContactsRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Contact, Salutation, FirstName, MiddleName, LastName, JobTitle, AdditionalContactRef, )
supermod.ContactsRet.subclass = ContactsRet
# end class ContactsRet


class AdditionalNotes(supermod.AdditionalNotes):
    def __init__(self, Note=None):
        super(AdditionalNotes, self).__init__(Note, )
supermod.AdditionalNotes.subclass = AdditionalNotes
# end class AdditionalNotes


class AdditionalNotesMod(supermod.AdditionalNotesMod):
    def __init__(self, NoteID=None, Note=None):
        super(AdditionalNotesMod, self).__init__(NoteID, Note, )
supermod.AdditionalNotesMod.subclass = AdditionalNotesMod
# end class AdditionalNotesMod


class AdditionalNotesRet(supermod.AdditionalNotesRet):
    def __init__(self, NoteID=None, Date=None, Note=None):
        super(AdditionalNotesRet, self).__init__(NoteID, Date, Note, )
supermod.AdditionalNotesRet.subclass = AdditionalNotesRet
# end class AdditionalNotesRet


class CreditCardInfo(supermod.CreditCardInfo):
    def __init__(self, CreditCardNumber=None, ExpirationMonth=None, ExpirationYear=None, NameOnCard=None, CreditCardAddress=None, CreditCardPostalCode=None):
        super(CreditCardInfo, self).__init__(CreditCardNumber, ExpirationMonth, ExpirationYear, NameOnCard, CreditCardAddress, CreditCardPostalCode, )
supermod.CreditCardInfo.subclass = CreditCardInfo
# end class CreditCardInfo


class CreditCardTxnInputInfo(supermod.CreditCardTxnInputInfo):
    def __init__(self, CreditCardNumber=None, ExpirationMonth=None, ExpirationYear=None, NameOnCard=None, CreditCardAddress=None, CreditCardPostalCode=None, CommercialCardCode=None, TransactionMode=None, CreditCardTxnType=None):
        super(CreditCardTxnInputInfo, self).__init__(CreditCardNumber, ExpirationMonth, ExpirationYear, NameOnCard, CreditCardAddress, CreditCardPostalCode, CommercialCardCode, TransactionMode, CreditCardTxnType, )
supermod.CreditCardTxnInputInfo.subclass = CreditCardTxnInputInfo
# end class CreditCardTxnInputInfo


class CreditCardTxnResultInfo(supermod.CreditCardTxnResultInfo):
    def __init__(self, ResultCode=None, ResultMessage=None, CreditCardTransID=None, MerchantAccountNumber=None, AuthorizationCode=None, AVSStreet=None, AVSZip=None, CardSecurityCodeMatch=None, ReconBatchID=None, PaymentGroupingCode=None, PaymentStatus=None, TxnAuthorizationTime=None, TxnAuthorizationStamp=None, ClientTransID=None):
        super(CreditCardTxnResultInfo, self).__init__(ResultCode, ResultMessage, CreditCardTransID, MerchantAccountNumber, AuthorizationCode, AVSStreet, AVSZip, CardSecurityCodeMatch, ReconBatchID, PaymentGroupingCode, PaymentStatus, TxnAuthorizationTime, TxnAuthorizationStamp, ClientTransID, )
supermod.CreditCardTxnResultInfo.subclass = CreditCardTxnResultInfo
# end class CreditCardTxnResultInfo


class CreditCardTxnInfo(supermod.CreditCardTxnInfo):
    def __init__(self, CreditCardTxnInputInfo=None, CreditCardTxnResultInfo=None):
        super(CreditCardTxnInfo, self).__init__(CreditCardTxnInputInfo, CreditCardTxnResultInfo, )
supermod.CreditCardTxnInfo.subclass = CreditCardTxnInfo
# end class CreditCardTxnInfo


class ErrorRecovery(supermod.ErrorRecovery):
    def __init__(self, ListID=None, OwnerID=None, TxnID=None, TxnNumber=None, EditSequence=None, ExternalGUID=None):
        super(ErrorRecovery, self).__init__(ListID, OwnerID, TxnID, TxnNumber, EditSequence, ExternalGUID, )
supermod.ErrorRecovery.subclass = ErrorRecovery
# end class ErrorRecovery


class AccountMetaData(supermod.AccountMetaData):
    def __init__(self, MaxCapacity=None):
        super(AccountMetaData, self).__init__(MaxCapacity, )
supermod.AccountMetaData.subclass = AccountMetaData
# end class AccountMetaData


class BillingRateMetaData(supermod.BillingRateMetaData):
    def __init__(self, MaxCapacity=None):
        super(BillingRateMetaData, self).__init__(MaxCapacity, )
supermod.BillingRateMetaData.subclass = BillingRateMetaData
# end class BillingRateMetaData


class ClassMetaData(supermod.ClassMetaData):
    def __init__(self, MaxCapacity=None):
        super(ClassMetaData, self).__init__(MaxCapacity, )
supermod.ClassMetaData.subclass = ClassMetaData
# end class ClassMetaData


class CustomerMsgMetaData(supermod.CustomerMsgMetaData):
    def __init__(self, MaxCapacity=None):
        super(CustomerMsgMetaData, self).__init__(MaxCapacity, )
supermod.CustomerMsgMetaData.subclass = CustomerMsgMetaData
# end class CustomerMsgMetaData


class CustomerTypeMetaData(supermod.CustomerTypeMetaData):
    def __init__(self, MaxCapacity=None):
        super(CustomerTypeMetaData, self).__init__(MaxCapacity, )
supermod.CustomerTypeMetaData.subclass = CustomerTypeMetaData
# end class CustomerTypeMetaData


class EntityMetaData(supermod.EntityMetaData):
    def __init__(self, MaxCapacity=None):
        super(EntityMetaData, self).__init__(MaxCapacity, )
supermod.EntityMetaData.subclass = EntityMetaData
# end class EntityMetaData


class ItemMetaData(supermod.ItemMetaData):
    def __init__(self, MaxCapacity=None):
        super(ItemMetaData, self).__init__(MaxCapacity, )
supermod.ItemMetaData.subclass = ItemMetaData
# end class ItemMetaData


class JobTypeMetaData(supermod.JobTypeMetaData):
    def __init__(self, MaxCapacity=None):
        super(JobTypeMetaData, self).__init__(MaxCapacity, )
supermod.JobTypeMetaData.subclass = JobTypeMetaData
# end class JobTypeMetaData


class PaymentMethodMetaData(supermod.PaymentMethodMetaData):
    def __init__(self, MaxCapacity=None):
        super(PaymentMethodMetaData, self).__init__(MaxCapacity, )
supermod.PaymentMethodMetaData.subclass = PaymentMethodMetaData
# end class PaymentMethodMetaData


class PayrollItemMetaData(supermod.PayrollItemMetaData):
    def __init__(self, MaxCapacity=None):
        super(PayrollItemMetaData, self).__init__(MaxCapacity, )
supermod.PayrollItemMetaData.subclass = PayrollItemMetaData
# end class PayrollItemMetaData


class PriceLevelMetaData(supermod.PriceLevelMetaData):
    def __init__(self, MaxCapacity=None):
        super(PriceLevelMetaData, self).__init__(MaxCapacity, )
supermod.PriceLevelMetaData.subclass = PriceLevelMetaData
# end class PriceLevelMetaData


class SalesRepMetaData(supermod.SalesRepMetaData):
    def __init__(self, MaxCapacity=None):
        super(SalesRepMetaData, self).__init__(MaxCapacity, )
supermod.SalesRepMetaData.subclass = SalesRepMetaData
# end class SalesRepMetaData


class SalesTaxCodeMetaData(supermod.SalesTaxCodeMetaData):
    def __init__(self, MaxCapacity=None):
        super(SalesTaxCodeMetaData, self).__init__(MaxCapacity, )
supermod.SalesTaxCodeMetaData.subclass = SalesTaxCodeMetaData
# end class SalesTaxCodeMetaData


class ShipMethodMetaData(supermod.ShipMethodMetaData):
    def __init__(self, MaxCapacity=None):
        super(ShipMethodMetaData, self).__init__(MaxCapacity, )
supermod.ShipMethodMetaData.subclass = ShipMethodMetaData
# end class ShipMethodMetaData


class TemplateMetaData(supermod.TemplateMetaData):
    def __init__(self, MaxCapacity=None):
        super(TemplateMetaData, self).__init__(MaxCapacity, )
supermod.TemplateMetaData.subclass = TemplateMetaData
# end class TemplateMetaData


class TermsMetaData(supermod.TermsMetaData):
    def __init__(self, MaxCapacity=None):
        super(TermsMetaData, self).__init__(MaxCapacity, )
supermod.TermsMetaData.subclass = TermsMetaData
# end class TermsMetaData


class ToDoMetaData(supermod.ToDoMetaData):
    def __init__(self, MaxCapacity=None):
        super(ToDoMetaData, self).__init__(MaxCapacity, )
supermod.ToDoMetaData.subclass = ToDoMetaData
# end class ToDoMetaData


class VehicleMetaData(supermod.VehicleMetaData):
    def __init__(self, MaxCapacity=None):
        super(VehicleMetaData, self).__init__(MaxCapacity, )
supermod.VehicleMetaData.subclass = VehicleMetaData
# end class VehicleMetaData


class VendorTypeMetaData(supermod.VendorTypeMetaData):
    def __init__(self, MaxCapacity=None):
        super(VendorTypeMetaData, self).__init__(MaxCapacity, )
supermod.VendorTypeMetaData.subclass = VendorTypeMetaData
# end class VendorTypeMetaData


class ListMetaData(supermod.ListMetaData):
    def __init__(self, AccountMetaData=None, BillingRateMetaData=None, ClassMetaData=None, CustomerMsgMetaData=None, CustomerTypeMetaData=None, EntityMetaData=None, ItemMetaData=None, JobTypeMetaData=None, PaymentMethodMetaData=None, PayrollItemMetaData=None, PriceLevelMetaData=None, SalesRepMetaData=None, SalesTaxCodeMetaData=None, ShipMethodMetaData=None, TemplateMetaData=None, TermsMetaData=None, ToDoMetaData=None, VehicleMetaData=None, VendorTypeMetaData=None):
        super(ListMetaData, self).__init__(AccountMetaData, BillingRateMetaData, ClassMetaData, CustomerMsgMetaData, CustomerTypeMetaData, EntityMetaData, ItemMetaData, JobTypeMetaData, PaymentMethodMetaData, PayrollItemMetaData, PriceLevelMetaData, SalesRepMetaData, SalesTaxCodeMetaData, ShipMethodMetaData, TemplateMetaData, TermsMetaData, ToDoMetaData, VehicleMetaData, VendorTypeMetaData, )
supermod.ListMetaData.subclass = ListMetaData
# end class ListMetaData


class HostRet(supermod.HostRet):
    def __init__(self, ProductName=None, MajorVersion=None, MinorVersion=None, Country=None, SupportedQBXMLVersion=None, IsAutomaticLogin=None, QBFileMode=None, ListMetaData=None):
        super(HostRet, self).__init__(ProductName, MajorVersion, MinorVersion, Country, SupportedQBXMLVersion, IsAutomaticLogin, QBFileMode, ListMetaData, )
supermod.HostRet.subclass = HostRet
# end class HostRet


class Service(supermod.Service):
    def __init__(self, Name=None, Domain=None, ServiceStatus=None):
        super(Service, self).__init__(Name, Domain, ServiceStatus, )
supermod.Service.subclass = Service
# end class Service


class SubscribedServices(supermod.SubscribedServices):
    def __init__(self, Service=None):
        super(SubscribedServices, self).__init__(Service, )
supermod.SubscribedServices.subclass = SubscribedServices
# end class SubscribedServices


class AccountantCopy(supermod.AccountantCopy):
    def __init__(self, AccountantCopyExists=None, DividingDate=None):
        super(AccountantCopy, self).__init__(AccountantCopyExists, DividingDate, )
supermod.AccountantCopy.subclass = AccountantCopy
# end class AccountantCopy


class CompanyRet(supermod.CompanyRet):
    def __init__(self, IsSampleCompany=None, CompanyName=None, LegalCompanyName=None, Address=None, AddressBlock=None, LegalAddress=None, CompanyAddressForCustomer=None, CompanyAddressBlockForCustomer=None, Phone=None, Fax=None, Email=None, CompanyEmailForCustomer=None, CompanyWebSite=None, FirstMonthFiscalYear=None, FirstMonthIncomeTaxYear=None, CompanyType=None, EIN=None, SSN=None, TaxForm=None, SubscribedServices=None, AccountantCopy=None, DataExtRet=None):
        super(CompanyRet, self).__init__(IsSampleCompany, CompanyName, LegalCompanyName, Address, AddressBlock, LegalAddress, CompanyAddressForCustomer, CompanyAddressBlockForCustomer, Phone, Fax, Email, CompanyEmailForCustomer, CompanyWebSite, FirstMonthFiscalYear, FirstMonthIncomeTaxYear, CompanyType, EIN, SSN, TaxForm, SubscribedServices, AccountantCopy, DataExtRet, )
supermod.CompanyRet.subclass = CompanyRet
# end class CompanyRet


class CustomerRet(supermod.CustomerRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Name=None, FullName=None, IsActive=None, ClassRef=None, ParentRef=None, Sublevel=None, CompanyName=None, Salutation=None, FirstName=None, MiddleName=None, LastName=None, Suffix=None, JobTitle=None, BillAddress=None, BillAddressBlock=None, ShipAddress=None, ShipAddressBlock=None, ShipToAddress=None, PrintAs=None, Phone=None, Mobile=None, Pager=None, AltPhone=None, Fax=None, Email=None, Cc=None, Contact=None, AltContact=None, AdditionalContactRef=None, ContactsRet=None, CustomerTypeRef=None, TermsRef=None, SalesRepRef=None, Balance=None, TotalBalance=None, SalesTaxCodeRef=None, ItemSalesTaxRef=None, SalesTaxCountry=None, ResaleNumber=None, AccountNumber=None, CreditLimit=None, PreferredPaymentMethodRef=None, CreditCardInfo=None, JobStatus=None, JobStartDate=None, JobProjectedEndDate=None, JobEndDate=None, JobDesc=None, JobTypeRef=None, Notes=None, AdditionalNotesRet=None, IsStatementWithParent=None, DeliveryMethod=None, PreferredDeliveryMethod=None, PriceLevelRef=None, ExternalGUID=None, TaxRegistrationNumber=None, CurrencyRef=None, DataExtRet=None):
        super(CustomerRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Name, FullName, IsActive, ClassRef, ParentRef, Sublevel, CompanyName, Salutation, FirstName, MiddleName, LastName, Suffix, JobTitle, BillAddress, BillAddressBlock, ShipAddress, ShipAddressBlock, ShipToAddress, PrintAs, Phone, Mobile, Pager, AltPhone, Fax, Email, Cc, Contact, AltContact, AdditionalContactRef, ContactsRet, CustomerTypeRef, TermsRef, SalesRepRef, Balance, TotalBalance, SalesTaxCodeRef, ItemSalesTaxRef, SalesTaxCountry, ResaleNumber, AccountNumber, CreditLimit, PreferredPaymentMethodRef, CreditCardInfo, JobStatus, JobStartDate, JobProjectedEndDate, JobEndDate, JobDesc, JobTypeRef, Notes, AdditionalNotesRet, IsStatementWithParent, DeliveryMethod, PreferredDeliveryMethod, PriceLevelRef, ExternalGUID, TaxRegistrationNumber, CurrencyRef, DataExtRet, )
supermod.CustomerRet.subclass = CustomerRet
# end class CustomerRet


class CustomerAdd(supermod.CustomerAdd):
    def __init__(self, Name=None, IsActive=None, ClassRef=None, ParentRef=None, CompanyName=None, Salutation=None, FirstName=None, MiddleName=None, LastName=None, Suffix=None, JobTitle=None, BillAddress=None, ShipAddress=None, ShipToAddress=None, PrintAs=None, Phone=None, Mobile=None, Pager=None, AltPhone=None, Fax=None, Email=None, Cc=None, Contact=None, AltContact=None, AdditionalContactRef=None, Contacts=None, CustomerTypeRef=None, TermsRef=None, SalesRepRef=None, OpenBalance=None, OpenBalanceDate=None, SalesTaxCodeRef=None, ItemSalesTaxRef=None, SalesTaxCountry=None, ResaleNumber=None, AccountNumber=None, CreditLimit=None, PreferredPaymentMethodRef=None, CreditCardInfo=None, JobStatus=None, JobStartDate=None, JobProjectedEndDate=None, JobEndDate=None, JobDesc=None, JobTypeRef=None, Notes=None, AdditionalNotes=None, IsStatementWithParent=None, DeliveryMethod=None, PreferredDeliveryMethod=None, PriceLevelRef=None, ExternalGUID=None, TaxRegistrationNumber=None, CurrencyRef=None):
        super(CustomerAdd, self).__init__(Name, IsActive, ClassRef, ParentRef, CompanyName, Salutation, FirstName, MiddleName, LastName, Suffix, JobTitle, BillAddress, ShipAddress, ShipToAddress, PrintAs, Phone, Mobile, Pager, AltPhone, Fax, Email, Cc, Contact, AltContact, AdditionalContactRef, Contacts, CustomerTypeRef, TermsRef, SalesRepRef, OpenBalance, OpenBalanceDate, SalesTaxCodeRef, ItemSalesTaxRef, SalesTaxCountry, ResaleNumber, AccountNumber, CreditLimit, PreferredPaymentMethodRef, CreditCardInfo, JobStatus, JobStartDate, JobProjectedEndDate, JobEndDate, JobDesc, JobTypeRef, Notes, AdditionalNotes, IsStatementWithParent, DeliveryMethod, PreferredDeliveryMethod, PriceLevelRef, ExternalGUID, TaxRegistrationNumber, CurrencyRef, )
supermod.CustomerAdd.subclass = CustomerAdd
# end class CustomerAdd


class CustomerMod(supermod.CustomerMod):
    def __init__(self, ListID=None, EditSequence=None, Name=None, IsActive=None, ClassRef=None, ParentRef=None, CompanyName=None, Salutation=None, FirstName=None, MiddleName=None, LastName=None, Suffix=None, JobTitle=None, BillAddress=None, ShipAddress=None, ShipToAddress=None, PrintAs=None, Phone=None, Mobile=None, Pager=None, AltPhone=None, Fax=None, Email=None, Cc=None, Contact=None, AltContact=None, AdditionalContactRef=None, ContactsMod=None, CustomerTypeRef=None, TermsRef=None, SalesRepRef=None, SalesTaxCodeRef=None, ItemSalesTaxRef=None, SalesTaxCountry=None, ResaleNumber=None, AccountNumber=None, CreditLimit=None, PreferredPaymentMethodRef=None, CreditCardInfo=None, JobStatus=None, JobStartDate=None, JobProjectedEndDate=None, JobEndDate=None, JobDesc=None, JobTypeRef=None, Notes=None, AdditionalNotesMod=None, IsStatementWithParent=None, DeliveryMethod=None, PreferredDeliveryMethod=None, PriceLevelRef=None, TaxRegistrationNumber=None, CurrencyRef=None):
        super(CustomerMod, self).__init__(ListID, EditSequence, Name, IsActive, ClassRef, ParentRef, CompanyName, Salutation, FirstName, MiddleName, LastName, Suffix, JobTitle, BillAddress, ShipAddress, ShipToAddress, PrintAs, Phone, Mobile, Pager, AltPhone, Fax, Email, Cc, Contact, AltContact, AdditionalContactRef, ContactsMod, CustomerTypeRef, TermsRef, SalesRepRef, SalesTaxCodeRef, ItemSalesTaxRef, SalesTaxCountry, ResaleNumber, AccountNumber, CreditLimit, PreferredPaymentMethodRef, CreditCardInfo, JobStatus, JobStartDate, JobProjectedEndDate, JobEndDate, JobDesc, JobTypeRef, Notes, AdditionalNotesMod, IsStatementWithParent, DeliveryMethod, PreferredDeliveryMethod, PriceLevelRef, TaxRegistrationNumber, CurrencyRef, )
supermod.CustomerMod.subclass = CustomerMod
# end class CustomerMod


class SalesOrPurchase(supermod.SalesOrPurchase):
    def __init__(self, Desc=None, Price=None, PricePercent=None, AccountRef=None):
        super(SalesOrPurchase, self).__init__(Desc, Price, PricePercent, AccountRef, )
supermod.SalesOrPurchase.subclass = SalesOrPurchase
# end class SalesOrPurchase


class SalesAndPurchase(supermod.SalesAndPurchase):
    def __init__(self, SalesDesc=None, SalesPrice=None, IncomeAccountRef=None, PurchaseDesc=None, PurchaseCost=None, PurchaseTaxCodeRef=None, ExpenseAccountRef=None, PrefVendorRef=None):
        super(SalesAndPurchase, self).__init__(SalesDesc, SalesPrice, IncomeAccountRef, PurchaseDesc, PurchaseCost, PurchaseTaxCodeRef, ExpenseAccountRef, PrefVendorRef, )
supermod.SalesAndPurchase.subclass = SalesAndPurchase
# end class SalesAndPurchase


class ItemServiceRet(supermod.ItemServiceRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Name=None, FullName=None, BarCodeValue=None, IsActive=None, ClassRef=None, ParentRef=None, Sublevel=None, UnitOfMeasureSetRef=None, IsTaxIncluded=None, SalesTaxCodeRef=None, SalesOrPurchase=None, SalesAndPurchase=None, ExternalGUID=None, DataExtRet=None):
        super(ItemServiceRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Name, FullName, BarCodeValue, IsActive, ClassRef, ParentRef, Sublevel, UnitOfMeasureSetRef, IsTaxIncluded, SalesTaxCodeRef, SalesOrPurchase, SalesAndPurchase, ExternalGUID, DataExtRet, )
supermod.ItemServiceRet.subclass = ItemServiceRet
# end class ItemServiceRet


class ItemNonInventoryRet(supermod.ItemNonInventoryRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Name=None, FullName=None, BarCodeValue=None, IsActive=None, ClassRef=None, ParentRef=None, Sublevel=None, ManufacturerPartNumber=None, UnitOfMeasureSetRef=None, IsTaxIncluded=None, SalesTaxCodeRef=None, SalesOrPurchase=None, SalesAndPurchase=None, ExternalGUID=None, DataExtRet=None):
        super(ItemNonInventoryRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Name, FullName, BarCodeValue, IsActive, ClassRef, ParentRef, Sublevel, ManufacturerPartNumber, UnitOfMeasureSetRef, IsTaxIncluded, SalesTaxCodeRef, SalesOrPurchase, SalesAndPurchase, ExternalGUID, DataExtRet, )
supermod.ItemNonInventoryRet.subclass = ItemNonInventoryRet
# end class ItemNonInventoryRet


class ItemOtherChargeRet(supermod.ItemOtherChargeRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Name=None, FullName=None, BarCodeValue=None, IsActive=None, ClassRef=None, ParentRef=None, Sublevel=None, IsTaxIncluded=None, SalesTaxCodeRef=None, SalesOrPurchase=None, SalesAndPurchase=None, SpecialItemType=None, ExternalGUID=None, DataExtRet=None):
        super(ItemOtherChargeRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Name, FullName, BarCodeValue, IsActive, ClassRef, ParentRef, Sublevel, IsTaxIncluded, SalesTaxCodeRef, SalesOrPurchase, SalesAndPurchase, SpecialItemType, ExternalGUID, DataExtRet, )
supermod.ItemOtherChargeRet.subclass = ItemOtherChargeRet
# end class ItemOtherChargeRet


class ItemInventoryRet(supermod.ItemInventoryRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Name=None, FullName=None, BarCodeValue=None, IsActive=None, ClassRef=None, ParentRef=None, Sublevel=None, ManufacturerPartNumber=None, UnitOfMeasureSetRef=None, IsTaxIncluded=None, SalesTaxCodeRef=None, SalesDesc=None, SalesPrice=None, IncomeAccountRef=None, PurchaseDesc=None, PurchaseCost=None, PurchaseTaxCodeRef=None, COGSAccountRef=None, PrefVendorRef=None, AssetAccountRef=None, ReorderPoint=None, QuantityOnHand=None, AverageCost=None, QuantityOnOrder=None, QuantityOnSalesOrder=None, ExternalGUID=None, DataExtRet=None):
        super(ItemInventoryRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Name, FullName, BarCodeValue, IsActive, ClassRef, ParentRef, Sublevel, ManufacturerPartNumber, UnitOfMeasureSetRef, IsTaxIncluded, SalesTaxCodeRef, SalesDesc, SalesPrice, IncomeAccountRef, PurchaseDesc, PurchaseCost, PurchaseTaxCodeRef, COGSAccountRef, PrefVendorRef, AssetAccountRef, ReorderPoint, QuantityOnHand, AverageCost, QuantityOnOrder, QuantityOnSalesOrder, ExternalGUID, DataExtRet, )
supermod.ItemInventoryRet.subclass = ItemInventoryRet
# end class ItemInventoryRet


class ItemInventoryAdd(supermod.ItemInventoryAdd):
    def __init__(self, Name=None, BarCode=None, IsActive=None, ClassRef=None, ParentRef=None, ManufacturerPartNumber=None, UnitOfMeasureSetRef=None, IsTaxIncluded=None, SalesTaxCodeRef=None, SalesDesc=None, SalesPrice=None, IncomeAccountRef=None, PurchaseDesc=None, PurchaseCost=None, PurchaseTaxCodeRef=None, COGSAccountRef=None, PrefVendorRef=None, AssetAccountRef=None, ReorderPoint=None, QuantityOnHand=None, TotalValue=None, InventoryDate=None, ExternalGUID=None):
        super(ItemInventoryAdd, self).__init__(Name, BarCode, IsActive, ClassRef, ParentRef, ManufacturerPartNumber, UnitOfMeasureSetRef, IsTaxIncluded, SalesTaxCodeRef, SalesDesc, SalesPrice, IncomeAccountRef, PurchaseDesc, PurchaseCost, PurchaseTaxCodeRef, COGSAccountRef, PrefVendorRef, AssetAccountRef, ReorderPoint, QuantityOnHand, TotalValue, InventoryDate, ExternalGUID, )
supermod.ItemInventoryAdd.subclass = ItemInventoryAdd
# end class ItemInventoryAdd


class ItemInventoryMod(supermod.ItemInventoryMod):
    def __init__(self, ListID=None, EditSequence=None, Name=None, BarCode=None, IsActive=None, ClassRef=None, ParentRef=None, ManufacturerPartNumber=None, UnitOfMeasureSetRef=None, ForceUOMChange=None, IsTaxIncluded=None, SalesTaxCodeRef=None, SalesDesc=None, SalesPrice=None, IncomeAccountRef=None, ApplyIncomeAccountRefToExistingTxns=None, PurchaseDesc=None, PurchaseCost=None, PurchaseTaxCodeRef=None, COGSAccountRef=None, ApplyCOGSAccountRefToExistingTxns=None, PrefVendorRef=None, AssetAccountRef=None, ReorderPoint=None):
        super(ItemInventoryMod, self).__init__(ListID, EditSequence, Name, BarCode, IsActive, ClassRef, ParentRef, ManufacturerPartNumber, UnitOfMeasureSetRef, ForceUOMChange, IsTaxIncluded, SalesTaxCodeRef, SalesDesc, SalesPrice, IncomeAccountRef, ApplyIncomeAccountRefToExistingTxns, PurchaseDesc, PurchaseCost, PurchaseTaxCodeRef, COGSAccountRef, ApplyCOGSAccountRefToExistingTxns, PrefVendorRef, AssetAccountRef, ReorderPoint, )
supermod.ItemInventoryMod.subclass = ItemInventoryMod
# end class ItemInventoryMod


class ItemInventoryAssemblyLine(supermod.ItemInventoryAssemblyLine):
    def __init__(self, ItemInventoryRef=None, Quantity=None):
        super(ItemInventoryAssemblyLine, self).__init__(ItemInventoryRef, Quantity, )
supermod.ItemInventoryAssemblyLine.subclass = ItemInventoryAssemblyLine
# end class ItemInventoryAssemblyLine


class ItemInventoryAssemblyRet(supermod.ItemInventoryAssemblyRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Name=None, FullName=None, BarCodeValue=None, IsActive=None, ClassRef=None, ParentRef=None, Sublevel=None, ManufacturerPartNumber=None, UnitOfMeasureSetRef=None, IsTaxIncluded=None, SalesTaxCodeRef=None, SalesDesc=None, SalesPrice=None, IncomeAccountRef=None, PurchaseDesc=None, PurchaseCost=None, PurchaseTaxCodeRef=None, COGSAccountRef=None, PrefVendorRef=None, AssetAccountRef=None, BuildPoint=None, QuantityOnHand=None, AverageCost=None, QuantityOnOrder=None, QuantityOnSalesOrder=None, ExternalGUID=None, ItemInventoryAssemblyLine=None, DataExtRet=None):
        super(ItemInventoryAssemblyRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Name, FullName, BarCodeValue, IsActive, ClassRef, ParentRef, Sublevel, ManufacturerPartNumber, UnitOfMeasureSetRef, IsTaxIncluded, SalesTaxCodeRef, SalesDesc, SalesPrice, IncomeAccountRef, PurchaseDesc, PurchaseCost, PurchaseTaxCodeRef, COGSAccountRef, PrefVendorRef, AssetAccountRef, BuildPoint, QuantityOnHand, AverageCost, QuantityOnOrder, QuantityOnSalesOrder, ExternalGUID, ItemInventoryAssemblyLine, DataExtRet, )
supermod.ItemInventoryAssemblyRet.subclass = ItemInventoryAssemblyRet
# end class ItemInventoryAssemblyRet


class FixedAssetSalesInfo(supermod.FixedAssetSalesInfo):
    def __init__(self, SalesDesc=None, SalesDate=None, SalesPrice=None, SalesExpense=None):
        super(FixedAssetSalesInfo, self).__init__(SalesDesc, SalesDate, SalesPrice, SalesExpense, )
supermod.FixedAssetSalesInfo.subclass = FixedAssetSalesInfo
# end class FixedAssetSalesInfo


class ItemFixedAssetRet(supermod.ItemFixedAssetRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Name=None, BarCodeValue=None, IsActive=None, ClassRef=None, AcquiredAs=None, PurchaseDesc=None, PurchaseDate=None, PurchaseCost=None, VendorOrPayeeName=None, AssetAccountRef=None, FixedAssetSalesInfo=None, AssetDesc=None, Location=None, PONumber=None, SerialNumber=None, WarrantyExpDate=None, Notes=None, AssetNumber=None, CostBasis=None, YearEndAccumulatedDepreciation=None, YearEndBookValue=None, ExternalGUID=None, DataExtRet=None):
        super(ItemFixedAssetRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Name, BarCodeValue, IsActive, ClassRef, AcquiredAs, PurchaseDesc, PurchaseDate, PurchaseCost, VendorOrPayeeName, AssetAccountRef, FixedAssetSalesInfo, AssetDesc, Location, PONumber, SerialNumber, WarrantyExpDate, Notes, AssetNumber, CostBasis, YearEndAccumulatedDepreciation, YearEndBookValue, ExternalGUID, DataExtRet, )
supermod.ItemFixedAssetRet.subclass = ItemFixedAssetRet
# end class ItemFixedAssetRet


class ItemSubtotalRet(supermod.ItemSubtotalRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Name=None, BarCodeValue=None, IsActive=None, ItemDesc=None, SpecialItemType=None, ExternalGUID=None, DataExtRet=None):
        super(ItemSubtotalRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Name, BarCodeValue, IsActive, ItemDesc, SpecialItemType, ExternalGUID, DataExtRet, )
supermod.ItemSubtotalRet.subclass = ItemSubtotalRet
# end class ItemSubtotalRet


class ItemDiscountRet(supermod.ItemDiscountRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Name=None, FullName=None, BarCodeValue=None, IsActive=None, ClassRef=None, ParentRef=None, Sublevel=None, ItemDesc=None, SalesTaxCodeRef=None, DiscountRate=None, DiscountRatePercent=None, AccountRef=None, ExternalGUID=None, DataExtRet=None):
        super(ItemDiscountRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Name, FullName, BarCodeValue, IsActive, ClassRef, ParentRef, Sublevel, ItemDesc, SalesTaxCodeRef, DiscountRate, DiscountRatePercent, AccountRef, ExternalGUID, DataExtRet, )
supermod.ItemDiscountRet.subclass = ItemDiscountRet
# end class ItemDiscountRet


class ItemPaymentRet(supermod.ItemPaymentRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Name=None, BarCodeValue=None, IsActive=None, ClassRef=None, ItemDesc=None, DepositToAccountRef=None, PaymentMethodRef=None, ExternalGUID=None, DataExtRet=None):
        super(ItemPaymentRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Name, BarCodeValue, IsActive, ClassRef, ItemDesc, DepositToAccountRef, PaymentMethodRef, ExternalGUID, DataExtRet, )
supermod.ItemPaymentRet.subclass = ItemPaymentRet
# end class ItemPaymentRet


class ItemSalesTaxRet(supermod.ItemSalesTaxRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Name=None, BarCodeValue=None, IsActive=None, ClassRef=None, ItemDesc=None, TaxRate=None, TaxVendorRef=None, SalesTaxReturnLineRef=None, ExternalGUID=None, DataExtRet=None):
        super(ItemSalesTaxRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Name, BarCodeValue, IsActive, ClassRef, ItemDesc, TaxRate, TaxVendorRef, SalesTaxReturnLineRef, ExternalGUID, DataExtRet, )
supermod.ItemSalesTaxRet.subclass = ItemSalesTaxRet
# end class ItemSalesTaxRet


class ItemSalesTaxGroupRet(supermod.ItemSalesTaxGroupRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Name=None, BarCodeValue=None, IsActive=None, ItemDesc=None, ExternalGUID=None, ItemSalesTaxRef=None, DataExtRet=None):
        super(ItemSalesTaxGroupRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Name, BarCodeValue, IsActive, ItemDesc, ExternalGUID, ItemSalesTaxRef, DataExtRet, )
supermod.ItemSalesTaxGroupRet.subclass = ItemSalesTaxGroupRet
# end class ItemSalesTaxGroupRet


class ItemGroupLine(supermod.ItemGroupLine):
    def __init__(self, ItemRef=None, Quantity=None, UnitOfMeasure=None):
        super(ItemGroupLine, self).__init__(ItemRef, Quantity, UnitOfMeasure, )
supermod.ItemGroupLine.subclass = ItemGroupLine
# end class ItemGroupLine


class ItemGroupRet(supermod.ItemGroupRet):
    def __init__(self, ListID=None, TimeCreated=None, TimeModified=None, EditSequence=None, Name=None, BarCodeValue=None, IsActive=None, ItemDesc=None, UnitOfMeasureSetRef=None, IsPrintItemsInGroup=None, SpecialItemType=None, ExternalGUID=None, ItemGroupLine=None, DataExtRet=None):
        super(ItemGroupRet, self).__init__(ListID, TimeCreated, TimeModified, EditSequence, Name, BarCodeValue, IsActive, ItemDesc, UnitOfMeasureSetRef, IsPrintItemsInGroup, SpecialItemType, ExternalGUID, ItemGroupLine, DataExtRet, )
supermod.ItemGroupRet.subclass = ItemGroupRet
# end class ItemGroupRet


class DiscountLineAdd(supermod.DiscountLineAdd):
    def __init__(self, Amount=None, RatePercent=None, IsTaxable=None, AccountRef=None):
        super(DiscountLineAdd, self).__init__(Amount, RatePercent, IsTaxable, AccountRef, )
supermod.DiscountLineAdd.subclass = DiscountLineAdd
# end class DiscountLineAdd


class SalesTaxLineAdd(supermod.SalesTaxLineAdd):
    def __init__(self, Amount=None, RatePercent=None, AccountRef=None):
        super(SalesTaxLineAdd, self).__init__(Amount, RatePercent, AccountRef, )
supermod.SalesTaxLineAdd.subclass = SalesTaxLineAdd
# end class SalesTaxLineAdd


class ShippingLineAdd(supermod.ShippingLineAdd):
    def __init__(self, Amount=None, AccountRef=None):
        super(ShippingLineAdd, self).__init__(Amount, AccountRef, )
supermod.ShippingLineAdd.subclass = ShippingLineAdd
# end class ShippingLineAdd


class DiscountLineRet(supermod.DiscountLineRet):
    def __init__(self, Amount=None, RatePercent=None, IsTaxable=None, AccountRef=None):
        super(DiscountLineRet, self).__init__(Amount, RatePercent, IsTaxable, AccountRef, )
supermod.DiscountLineRet.subclass = DiscountLineRet
# end class DiscountLineRet


class SalesTaxLineRet(supermod.SalesTaxLineRet):
    def __init__(self, Amount=None, RatePercent=None, AccountRef=None):
        super(SalesTaxLineRet, self).__init__(Amount, RatePercent, AccountRef, )
supermod.SalesTaxLineRet.subclass = SalesTaxLineRet
# end class SalesTaxLineRet


class ShippingLineRet(supermod.ShippingLineRet):
    def __init__(self, Amount=None, AccountRef=None):
        super(ShippingLineRet, self).__init__(Amount, AccountRef, )
supermod.ShippingLineRet.subclass = ShippingLineRet
# end class ShippingLineRet


class SalesReceiptLineRet(supermod.SalesReceiptLineRet):
    def __init__(self, TxnLineID=None, ItemRef=None, Desc=None, Quantity=None, UnitOfMeasure=None, OverrideUOMSetRef=None, Rate=None, RatePercent=None, ClassRef=None, Amount=None, TaxAmount=None, InventorySiteRef=None, InventorySiteLocationRef=None, SerialNumber=None, LotNumber=None, ServiceDate=None, SalesTaxCodeRef=None, IsTaxable=None, Other1=None, Other2=None, CreditCardTxnInfo=None, DataExtRet=None):
        super(SalesReceiptLineRet, self).__init__(TxnLineID, ItemRef, Desc, Quantity, UnitOfMeasure, OverrideUOMSetRef, Rate, RatePercent, ClassRef, Amount, TaxAmount, InventorySiteRef, InventorySiteLocationRef, SerialNumber, LotNumber, ServiceDate, SalesTaxCodeRef, IsTaxable, Other1, Other2, CreditCardTxnInfo, DataExtRet, )
supermod.SalesReceiptLineRet.subclass = SalesReceiptLineRet
# end class SalesReceiptLineRet


class SalesReceiptLineAdd(supermod.SalesReceiptLineAdd):
    def __init__(self, defMacro=None, ItemRef=None, Desc=None, Quantity=None, UnitOfMeasure=None, Rate=None, RatePercent=None, PriceLevelRef=None, ClassRef=None, Amount=None, TaxAmount=None, InventorySiteRef=None, InventorySiteLocationRef=None, SerialNumber=None, LotNumber=None, ServiceDate=None, SalesTaxCodeRef=None, IsTaxable=None, OverrideItemAccountRef=None, Other1=None, Other2=None, CreditCardTxnInfo=None, DataExt=None):
        super(SalesReceiptLineAdd, self).__init__(defMacro, ItemRef, Desc, Quantity, UnitOfMeasure, Rate, RatePercent, PriceLevelRef, ClassRef, Amount, TaxAmount, InventorySiteRef, InventorySiteLocationRef, SerialNumber, LotNumber, ServiceDate, SalesTaxCodeRef, IsTaxable, OverrideItemAccountRef, Other1, Other2, CreditCardTxnInfo, DataExt, )
supermod.SalesReceiptLineAdd.subclass = SalesReceiptLineAdd
# end class SalesReceiptLineAdd


class SalesReceiptLineGroupRet(supermod.SalesReceiptLineGroupRet):
    def __init__(self, TxnLineID=None, ItemGroupRef=None, Desc=None, Quantity=None, UnitOfMeasure=None, OverrideUOMSetRef=None, IsPrintItemsInGroup=None, TotalAmount=None, ServiceDate=None, SalesReceiptLineRet=None, DataExtRet=None):
        super(SalesReceiptLineGroupRet, self).__init__(TxnLineID, ItemGroupRef, Desc, Quantity, UnitOfMeasure, OverrideUOMSetRef, IsPrintItemsInGroup, TotalAmount, ServiceDate, SalesReceiptLineRet, DataExtRet, )
supermod.SalesReceiptLineGroupRet.subclass = SalesReceiptLineGroupRet
# end class SalesReceiptLineGroupRet


class SalesReceiptLineGroupAdd(supermod.SalesReceiptLineGroupAdd):
    def __init__(self, ItemGroupRef=None, Desc=None, Quantity=None, UnitOfMeasure=None, ServiceDate=None, InventorySiteRef=None, InventorySiteLocationRef=None, DataExt=None):
        super(SalesReceiptLineGroupAdd, self).__init__(ItemGroupRef, Desc, Quantity, UnitOfMeasure, ServiceDate, InventorySiteRef, InventorySiteLocationRef, DataExt, )
supermod.SalesReceiptLineGroupAdd.subclass = SalesReceiptLineGroupAdd
# end class SalesReceiptLineGroupAdd


class SalesReceiptLineMod(supermod.SalesReceiptLineMod):
    def __init__(self, TxnLineID=None, ItemRef=None, Desc=None, Quantity=None, UnitOfMeasure=None, OverrideUOMSetRef=None, Rate=None, RatePercent=None, PriceLevelRef=None, ClassRef=None, Amount=None, TaxAmount=None, InventorySiteRef=None, InventorySiteLocationRef=None, SerialNumber=None, LotNumber=None, ServiceDate=None, SalesTaxCodeRef=None, OverrideItemAccountRef=None, Other1=None, Other2=None):
        super(SalesReceiptLineMod, self).__init__(TxnLineID, ItemRef, Desc, Quantity, UnitOfMeasure, OverrideUOMSetRef, Rate, RatePercent, PriceLevelRef, ClassRef, Amount, TaxAmount, InventorySiteRef, InventorySiteLocationRef, SerialNumber, LotNumber, ServiceDate, SalesTaxCodeRef, OverrideItemAccountRef, Other1, Other2, )
supermod.SalesReceiptLineMod.subclass = SalesReceiptLineMod
# end class SalesReceiptLineMod


class SalesReceiptLineGroupMod(supermod.SalesReceiptLineGroupMod):
    def __init__(self, TxnLineID=None, ItemGroupRef=None, Quantity=None, UnitOfMeasure=None, OverrideUOMSetRef=None, SalesReceiptLineMod=None):
        super(SalesReceiptLineGroupMod, self).__init__(TxnLineID, ItemGroupRef, Quantity, UnitOfMeasure, OverrideUOMSetRef, SalesReceiptLineMod, )
supermod.SalesReceiptLineGroupMod.subclass = SalesReceiptLineGroupMod
# end class SalesReceiptLineGroupMod


class SalesReceiptRet(supermod.SalesReceiptRet):
    def __init__(self, TxnID=None, TimeCreated=None, TimeModified=None, EditSequence=None, TxnNumber=None, CustomerRef=None, ClassRef=None, TemplateRef=None, TxnDate=None, RefNumber=None, BillAddress=None, BillAddressBlock=None, ShipAddress=None, ShipAddressBlock=None, IsPending=None, CheckNumber=None, PaymentMethodRef=None, DueDate=None, SalesRepRef=None, ShipDate=None, ShipMethodRef=None, FOB=None, Subtotal=None, ItemSalesTaxRef=None, SalesTaxPercentage=None, SalesTaxTotal=None, TotalAmount=None, CurrencyRef=None, ExchangeRate=None, TotalAmountInHomeCurrency=None, Memo=None, CustomerMsgRef=None, IsToBePrinted=None, IsToBeEmailed=None, IsTaxIncluded=None, CustomerSalesTaxCodeRef=None, DepositToAccountRef=None, CreditCardTxnInfo=None, Other=None, ExternalGUID=None, SalesReceiptLineRet=None, SalesReceiptLineGroupRet=None, DiscountLineRet=None, SalesTaxLineRet=None, ShippingLineRet=None, DataExtRet=None):
        super(SalesReceiptRet, self).__init__(TxnID, TimeCreated, TimeModified, EditSequence, TxnNumber, CustomerRef, ClassRef, TemplateRef, TxnDate, RefNumber, BillAddress, BillAddressBlock, ShipAddress, ShipAddressBlock, IsPending, CheckNumber, PaymentMethodRef, DueDate, SalesRepRef, ShipDate, ShipMethodRef, FOB, Subtotal, ItemSalesTaxRef, SalesTaxPercentage, SalesTaxTotal, TotalAmount, CurrencyRef, ExchangeRate, TotalAmountInHomeCurrency, Memo, CustomerMsgRef, IsToBePrinted, IsToBeEmailed, IsTaxIncluded, CustomerSalesTaxCodeRef, DepositToAccountRef, CreditCardTxnInfo, Other, ExternalGUID, SalesReceiptLineRet, SalesReceiptLineGroupRet, DiscountLineRet, SalesTaxLineRet, ShippingLineRet, DataExtRet, )
supermod.SalesReceiptRet.subclass = SalesReceiptRet
# end class SalesReceiptRet


class SalesReceiptAdd(supermod.SalesReceiptAdd):
    def __init__(self, defMacro=None, CustomerRef=None, ClassRef=None, TemplateRef=None, TxnDate=None, RefNumber=None, BillAddress=None, ShipAddress=None, IsPending=None, CheckNumber=None, PaymentMethodRef=None, DueDate=None, SalesRepRef=None, ShipDate=None, ShipMethodRef=None, FOB=None, ItemSalesTaxRef=None, Memo=None, CustomerMsgRef=None, IsToBePrinted=None, IsToBeEmailed=None, IsTaxIncluded=None, CustomerSalesTaxCodeRef=None, DepositToAccountRef=None, CreditCardTxnInfo=None, Other=None, ExchangeRate=None, ExternalGUID=None, SalesReceiptLineAdd=None, SalesReceiptLineGroupAdd=None, DiscountLineAdd=None, SalesTaxLineAdd=None, ShippingLineAdd=None):
        super(SalesReceiptAdd, self).__init__(defMacro, CustomerRef, ClassRef, TemplateRef, TxnDate, RefNumber, BillAddress, ShipAddress, IsPending, CheckNumber, PaymentMethodRef, DueDate, SalesRepRef, ShipDate, ShipMethodRef, FOB, ItemSalesTaxRef, Memo, CustomerMsgRef, IsToBePrinted, IsToBeEmailed, IsTaxIncluded, CustomerSalesTaxCodeRef, DepositToAccountRef, CreditCardTxnInfo, Other, ExchangeRate, ExternalGUID, SalesReceiptLineAdd, SalesReceiptLineGroupAdd, DiscountLineAdd, SalesTaxLineAdd, ShippingLineAdd, )
supermod.SalesReceiptAdd.subclass = SalesReceiptAdd
# end class SalesReceiptAdd


class SalesReceiptMod(supermod.SalesReceiptMod):
    def __init__(self, TxnID=None, EditSequence=None, CustomerRef=None, ClassRef=None, TemplateRef=None, TxnDate=None, RefNumber=None, BillAddress=None, ShipAddress=None, IsPending=None, CheckNumber=None, PaymentMethodRef=None, DueDate=None, SalesRepRef=None, ShipDate=None, ShipMethodRef=None, FOB=None, ItemSalesTaxRef=None, Memo=None, CustomerMsgRef=None, IsToBePrinted=None, IsToBeEmailed=None, IsTaxIncluded=None, CustomerSalesTaxCodeRef=None, DepositToAccountRef=None, Other=None, ExchangeRate=None, SalesReceiptLineMod=None, SalesReceiptLineGroupMod=None):
        super(SalesReceiptMod, self).__init__(TxnID, EditSequence, CustomerRef, ClassRef, TemplateRef, TxnDate, RefNumber, BillAddress, ShipAddress, IsPending, CheckNumber, PaymentMethodRef, DueDate, SalesRepRef, ShipDate, ShipMethodRef, FOB, ItemSalesTaxRef, Memo, CustomerMsgRef, IsToBePrinted, IsToBeEmailed, IsTaxIncluded, CustomerSalesTaxCodeRef, DepositToAccountRef, Other, ExchangeRate, SalesReceiptLineMod, SalesReceiptLineGroupMod, )
supermod.SalesReceiptMod.subclass = SalesReceiptMod
# end class SalesReceiptMod


class DataExt(supermod.DataExt):
    def __init__(self, OwnerID=None, DataExtName=None, DataExtValue=None):
        super(DataExt, self).__init__(OwnerID, DataExtName, DataExtValue, )
supermod.DataExt.subclass = DataExt
# end class DataExt


class DataExtRet(supermod.DataExtRet):
    def __init__(self, OwnerID=None, DataExtName=None, DataExtType=None, DataExtValue=None):
        super(DataExtRet, self).__init__(OwnerID, DataExtName, DataExtType, DataExtValue, )
supermod.DataExtRet.subclass = DataExtRet
# end class DataExtRet


class SignonMsgsRq(supermod.SignonMsgsRq):
    def __init__(self, SignonAppCertRq=None, SignonDesktopRq=None, SignonTicketRq=None):
        super(SignonMsgsRq, self).__init__(SignonAppCertRq, SignonDesktopRq, SignonTicketRq, )
supermod.SignonMsgsRq.subclass = SignonMsgsRq
# end class SignonMsgsRq


class SignonMsgsRs(supermod.SignonMsgsRs):
    def __init__(self, SignonAppCertRs=None, SignonDesktopRs=None, SignonTicketRs=None):
        super(SignonMsgsRs, self).__init__(SignonAppCertRs, SignonDesktopRs, SignonTicketRs, )
supermod.SignonMsgsRs.subclass = SignonMsgsRs
# end class SignonMsgsRs


class SignonAppCertRqType(supermod.SignonAppCertRqType):
    def __init__(self, requestID=None, ClientDateTime=None, ApplicationLogin=None, ConnectionTicket=None, InstallationID=None, Language=None, AppID=None, AppVer=None):
        super(SignonAppCertRqType, self).__init__(requestID, ClientDateTime, ApplicationLogin, ConnectionTicket, InstallationID, Language, AppID, AppVer, )
supermod.SignonAppCertRqType.subclass = SignonAppCertRqType
# end class SignonAppCertRqType


class SignonDesktopRqType(supermod.SignonDesktopRqType):
    def __init__(self, requestID=None, ClientDateTime=None, ApplicationLogin=None, ConnectionTicket=None, InstallationID=None, Language=None, AppID=None, AppVer=None):
        super(SignonDesktopRqType, self).__init__(requestID, ClientDateTime, ApplicationLogin, ConnectionTicket, InstallationID, Language, AppID, AppVer, )
supermod.SignonDesktopRqType.subclass = SignonDesktopRqType
# end class SignonDesktopRqType


class SignonTicketRqType(supermod.SignonTicketRqType):
    def __init__(self, requestID=None, ClientDateTime=None, SessionTicket=None, AuthID=None, InstallationID=None, Language=None, AppID=None, AppVer=None):
        super(SignonTicketRqType, self).__init__(requestID, ClientDateTime, SessionTicket, AuthID, InstallationID, Language, AppID, AppVer, )
supermod.SignonTicketRqType.subclass = SignonTicketRqType
# end class SignonTicketRqType


class SignonAppCertRsType(supermod.SignonAppCertRsType):
    def __init__(self, statusSeverity=None, requestID=None, statusMessage=None, statusCode=None, ServerDateTime=None, SessionTicket=None):
        super(SignonAppCertRsType, self).__init__(statusSeverity, requestID, statusMessage, statusCode, ServerDateTime, SessionTicket, )
supermod.SignonAppCertRsType.subclass = SignonAppCertRsType
# end class SignonAppCertRsType


class SignonDesktopRsType(supermod.SignonDesktopRsType):
    def __init__(self, statusSeverity=None, requestID=None, statusMessage=None, statusCode=None, ServerDateTime=None, SessionTicket=None):
        super(SignonDesktopRsType, self).__init__(statusSeverity, requestID, statusMessage, statusCode, ServerDateTime, SessionTicket, )
supermod.SignonDesktopRsType.subclass = SignonDesktopRsType
# end class SignonDesktopRsType


class SignonTicketRsType(supermod.SignonTicketRsType):
    def __init__(self, statusSeverity=None, requestID=None, statusMessage=None, statusCode=None, ServerDateTime=None, SessionTicket=None):
        super(SignonTicketRsType, self).__init__(statusSeverity, requestID, statusMessage, statusCode, ServerDateTime, SessionTicket, )
supermod.SignonTicketRsType.subclass = SignonTicketRsType
# end class SignonTicketRsType


class PaymentTxnIDType(supermod.PaymentTxnIDType):
    def __init__(self, useMacro=None, valueOf_=None):
        super(PaymentTxnIDType, self).__init__(useMacro, valueOf_, )
supermod.PaymentTxnIDType.subclass = PaymentTxnIDType
# end class PaymentTxnIDType


class PaymentTxnLineIDType(supermod.PaymentTxnLineIDType):
    def __init__(self, useMacro=None, valueOf_=None):
        super(PaymentTxnLineIDType, self).__init__(useMacro, valueOf_, )
supermod.PaymentTxnLineIDType.subclass = PaymentTxnLineIDType
# end class PaymentTxnLineIDType


class TxnIDType(supermod.TxnIDType):
    def __init__(self, useMacro=None, valueOf_=None):
        super(TxnIDType, self).__init__(useMacro, valueOf_, )
supermod.TxnIDType.subclass = TxnIDType
# end class TxnIDType


class TxnLineIDType(supermod.TxnLineIDType):
    def __init__(self, useMacro=None, valueOf_=None):
        super(TxnLineIDType, self).__init__(useMacro, valueOf_, )
supermod.TxnLineIDType.subclass = TxnLineIDType
# end class TxnLineIDType


class TxnLineIDType1(supermod.TxnLineIDType1):
    def __init__(self, useMacro=None, valueOf_=None):
        super(TxnLineIDType1, self).__init__(useMacro, valueOf_, )
supermod.TxnLineIDType1.subclass = TxnLineIDType1
# end class TxnLineIDType1


class TxnIDType1(supermod.TxnIDType1):
    def __init__(self, useMacro=None, valueOf_=None):
        super(TxnIDType1, self).__init__(useMacro, valueOf_, )
supermod.TxnIDType1.subclass = TxnIDType1
# end class TxnIDType1



def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    if hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'QBXMLMsgsRq'
        rootClass = supermod.QBXML
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='http://developer.intuit.com/',
        pretty_print=True)
    doc = None
    return rootObj


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'QBXMLMsgsRq'
        rootClass = supermod.QBXML
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='http://developer.intuit.com/')
    return rootObj


def parseLiteral(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'QBXMLMsgsRq'
        rootClass = supermod.QBXML
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from qbxmlops120 import *\n\n')
    sys.stdout.write('import qbxmlops120 as model_\n\n')
    sys.stdout.write('rootObj = model_.QBXMLMsgsRq(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="QBXMLMsgsRq")
    sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    root = parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


