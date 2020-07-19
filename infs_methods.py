
Suds ( https://github.com/cackharot/suds-py3 )  version: 1.4.1.0 IN  build: 20200421

Service ( SpService ) tns="http://np.systor.st/sp"
   Prefixes (2)
      ns0 = "http://np.systor.st/commontypes"
      ns1 = "http://np.systor.st/sp"
   Ports (1):
      (SpSoap)
         Methods (15):
            HandleErrorNotification(ns0:MessageCode MessageCode, ns0:PortID PortID, ns0:MessageCode RejectedMessageCode, ns0:ErrorCode ErrorCode, xs:string Comments, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpBillingResolution(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID SubscriptionNetworkID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpBillingResolutionAlert(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID SubscriptionNetworkID, ns0:ResolutionLevel ResolutionLevel, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpBillingResolutionAlertReceived(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID SubscriptionNetworkID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpBillingResolutionEnd(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID SubscriptionNetworkID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpBillingResolutionReceived(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID SubscriptionNetworkID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpDeactivateBroadcast(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID SubscriptionNetworkID, ns0:OperatorID BlockID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpDeactivateComplete(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID SubscriptionNetworkID, ns0:OperatorID BlockID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpExecuteBroadcast(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID RecipientID, ns0:RoutingNumber NewRoute, xs:dateTime PortingDatetime, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpExecuteComplete(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:OperatorID DonorID, ns0:OperatorID RecipientID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpQueryComplete(ns0:MessageCode MessageCode, xs:string Comments, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpRequest(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:SubmissionID SubmissionID, ns0:OperatorID DonorID, ns0:OperatorID RecipientID, ns0:SimCardNumber SimCardNumber, ns0:CompanyFlag CompanyFlag, ns0:CPR CPR, ns0:CommercialRegNumber CommercialRegNumber, ns0:PassportNumber PassportNumber, ns0:GCCID GCCID, xs:string Comments, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpRequestAccept(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:SubmissionID SubmissionID, ns0:OperatorID DonorID, ns0:OperatorID RecipientID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpRequestCancel(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:SubmissionID SubmissionID, ns0:OperatorID DonorID, ns0:OperatorID RecipientID, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
            HandleNpRequestReject(ns0:ServiceType ServiceType, ns0:MessageCode MessageCode, ns0:Number Number, ns0:PortID PortID, ns0:SubmissionID SubmissionID, ns0:OperatorID DonorID, ns0:OperatorID RecipientID, ns0:RejectCode RejectCode, xs:string Comments, ns0:OperatorID OriginationID, ns0:OperatorID DestinationID, )
         Types (37):
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
            NpDeactivateBroadcast_Type
            ns0:NpDeactivateComplete_Type
            NpExecuteBroadcast_Type
            ns0:NpExecuteComplete_Type
            NpQueryComplete_Type
            ns0:NpRequestAccept_Type
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
