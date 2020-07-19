
Suds ( https://github.com/cackharot/suds-py3 )  version: 1.4.1.0 IN  build: 20200421

Service ( NpcdbService ) tns="http://np.systor.st/npcdb"
   Prefixes (2)
      ns0 = "http://np.systor.st/commontypes"
      ns1 = "http://np.systor.st/npcdb"
   Ports (1):
      (NpcdbSoap)
         Methods (14):
            SendNpBillingResolution(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID SubscriptionNetworkID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            SendNpBillingResolutionAlert(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID SubscriptionNetworkID, ns0:ResolutionLevel ResolutionLevel, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            SendNpBillingResolutionAlertReceived(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID SubscriptionNetworkID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            SendNpBillingResolutionEnd(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID SubscriptionNetworkID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            SendNpBillingResolutionReceived(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID SubscriptionNetworkID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            SendNpDeactivate(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:OperatorID SubscriptionNetworkID, ns0:OperatorID BlockID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            SendNpDeactivateComplete(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID SubscriptionNetworkID, ns0:OperatorID BlockID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            SendNpExecute(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID RecipientID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            SendNpExecuteComplete(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID RecipientID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            SendNpQuery(ns0:MessageCode MessageCode, xs:dateTime DateFrom, xs:dateTime DateTo, ns0:Number NumberFrom, ns0:Number NumberTo, ns0:OperatorID OperatorID, xs:string Comments, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            SendNpRequest(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:SubmissionID SubmissionID, ns0:OperatorID DonorID, ns0:OperatorID RecipientID, ns0:SimCardNumber SimCardNumber, ns0:CompanyFlag CompanyFlag, ns0:CPR CPR, ns0:CommercialRegNumber CommercialRegNumber, ns0:PassportNumber PassportNumber, ns0:GCCID GCCID, xs:string Comments, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            SendNpRequestAccept(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:SubmissionID SubmissionID, ns0:OperatorID DonorID, ns0:OperatorID RecipientID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            SendNpRequestCancel(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:SubmissionID SubmissionID, ns0:OperatorID DonorID, ns0:OperatorID RecipientID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            SendNpRequestReject(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:SubmissionID SubmissionID, ns0:OperatorID DonorID, ns0:OperatorID RecipientID, ns0:RejectCode RejectCode, xs:string Comments, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
         Types (39):
            ns0:AccessFault_Type
            ns0:CPR
            ns0:Comments
            ns0:CommercialRegNumber
            ns0:CompanyFlag
            ns0:CountryCode
            ns0:ErrorCode
            ns0:ErrorNotification_Type
            ns0:GCCID
            ns0:GCCIDNumber
            ns0:MessageAck_Type
            ns0:MessageCode
            ns0:NpBillingResolutionAlertReceived_Type
            ns0:NpBillingResolutionAlert_Type
            ns0:NpBillingResolutionEnd_Type
            ns0:NpBillingResolutionReceived_Type
            ns0:NpBillingResolution_Type
            NpDeactivateAck_Type
            ns0:NpDeactivateComplete_Type
            NpDeactivate_Type
            ns0:NpExecuteComplete_Type
            NpExecute_Type
            NpQuery_Type
            ns0:NpRequestAccept_Type
            NpRequestAck_Type
            ns0:NpRequestCancel_Type
            ns0:NpRequestReject_Type
            ns0:NpRequest_Type
            ns0:Number
            ns0:OperatorID
            ns0:PassportNumber
            ns0:PortID
            ns0:RejectCode
            ns0:ResolutionLevel
            ns0:RoutingNumber
            ns0:ServiceType
            ns0:SimCardNumber
            ns0:SubmissionID
            ns0:TechnicalFault_Type
--------------------------------------------------------------------------------
