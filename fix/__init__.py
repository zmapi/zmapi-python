from enum import IntEnum

class AggressorSide:
    Buy = "1"
    Sell = "2"
    Undisclosed = "7"

class BusinessRejectReason(IntEnum):
    Other = 0
    UnknownID = 1
    UnknownSecurity = 2
    UnsupportedMessageType = 3
    ConditionallyRequiredFieldMissing = 4
    NotAuthorized = 5
    InvalidPriceIncrement = 18
    ZMGenericError = 99

class HaltReason(IntEnum):
    NewsDissemination = 0
    OrderInflux = 1
    OrderImbalance = 2
    AdditionalInformation = 3
    NewsPending = 4
    EquipmentChangeover = 5
    SurveillanceIntervention = 101

class MarketCondition(IntEnum):
    Normal = 0
    Stressed = 1
    Exceptional = 2

class MarketDepth(IntEnum):
    FullBookDepth = 0
    TopOfBook = 1

class MDBookType(IntEnum):
    TopOfBook = 1
    PriceDepth = 2
    OrderDepth = 3

class MDEntryType:
    Bid = "0"
    Offer = "1"
    Trade = "2"
    IndexValue = "3"
    OpeningPrice = "4"
    ClosingPrice = "5"
    SettlementPrice = "6"
    TradingSessionHighPrice = "7"
    TradingSessionLowPrice = "8"
    TradingSessionVWAPPrice = "9"
    Imbalance = "A"
    TradingSessionTradeVolume = "B"
    OpenInterest = "C"
    CompositeUnderlyingPrice = "D"
    SimulatedSellPrice = "E"
    SimulatedBuyPrice = "F"
    EmptyBook = "J"
    PriorSettlePrice = "M"
    TradingSessionHighBid = "N"
    TradingSessionLowOffer = "O"
    AuctionClearingPrice = "Q"
    PreviousClosingPrice = "e"

class MDReqRejReason:
    UnknownSymbol = "0"
    DuplicateMDReqID = "1"
    InsufficientBandwidth = "2"
    InsufficientPermissions = "3"
    UnsupportedSubscriptionRequestType = "4"
    UnsupportedMarketDepth = "5"
    UnsupportedMDUpdateType = "6"
    UnsupportedAggregatedBook = "7"
    UnsupportedMDEntryType = "8"
    UnsupportedTradingSessionID = "9"
    UnsupportedScope = "A"
    UnsupportedOpenCloseSettleFlag = "B"
    UnsupportedMDImplicitDelete = "C"
    InsufficientCredit = "D"
    ZMGenericError = "z"

class MDUpdateAction:
    New = "0"
    Change = "1"
    Delete = "2"
    DeleteThru = "3"
    DeleteFrom = "4"
    Overlay = "5"

class MDUpdateType(IntEnum):
    FullRefresh = 0
    IncrementalRefresh = 1

class MsgType:
    Heartbeat = "0"
    TestRequest = "1"
    ResendRequest = "2"
    Reject = "3"
    Logout = "5"
    IOI = "6"
    Advertisement = "7"
    ExecutionReport = "8"
    OrderCancelReject = "9"
    Logon = "A"
    News = "B"
    MarketDefinitionRequest = "BT"
    MarketDefinition = "BU"
    UserNotification = "CB"
    DontKnowTrade = "Q"
    QuoteRequest = "R"
    Quote = "S"
    MarketDataRequest = "V"
    MarketDataSnapshotFullRefresh = "W"
    MarketDataIncrementalRefresh = "X"
    MarketDataRequestReject = "Y"
    QuoteCancel = "Z"
    ZMResendRequestResponse = "ZM2"
    ZMReject = "ZM3"
    ZMMarketDefinitionRequestResponse = "ZMB"
    ZMListCapabilities = "ZMc"
    ZMListCapabilitiesResponse = "ZMC"
    ZMListDirectory = "ZMd"
    ZMListDirectoryResponse = "ZMD"
    ZMListEndpoints = "ZMe"
    ZMListEndpointsResponse = "ZME"
    ZMGetInstrumentFields = "ZMf"
    ZMGetInstrumentFieldsResponse = "ZMF"
    ZMTradingSessionStatusRequestResponse = "ZMH"
    ZMGetValidReqID = "ZMi"
    ZMGetValidReqIDResponse = "ZMI"
    ZMListCommonInstruments = "ZMl"
    ZMListCommonInstrumentsResponse = "ZML"
    ZMMarketDataRequestResponse = "ZMM"
    ZMGetConnectorFeatures = "ZMo"
    ZMGetConnectorFeaturesResponse = "ZMO"
    ZMGetSessionID = "ZMs"
    ZMGetSessionIDResponse = "ZMS"
    ZMSecurityDefinitionRequestResponse = "ZMSD"
    ZMSecurityStatusRequestResponse = "ZMSS"
    ZMSecurityListRequestResponse = "ZMY"
#     ZMGetStatus = "ZMs"
#     ZMGetStatusResponse = "ZMS"
#     ZMGetSubscriptions = "ZMv"
#     ZMGetSubscriptionsResponse = "ZMV"
    SecurityDefinitionRequest = "c"
    SecurityDefinition = "d"
    SecurityStatusRequest = "e"
    SecurityStatus = "f"
    TradingSessionStatusRequest = "g"
    TradingSessionStatus = "h"
    BusinessMessageReject = "j"
    BidRequest = "k"
    BidResponse = "l"
    SecurityListRequest = "x"
    SecurityList = "y"


class QuoteCondition:
    Open = "A"
    Closed = "B"
    OutrightPrice = "J"
    ImpliedPrice ="K"
    Closing = "O"

class SecurityRequestResult(IntEnum):
    ValidRequest = 0
    InvalidOrUnsupportedRequest = 1
    NoInstrumentsFound = 2
    NotAuthorizedToRetrieveInstrumentData = 3
    InstrumentDataTemporarilyUnavailable = 4
    # InvalidInstrumentRequested = 1
    # InstrumentAlreadyExists = 2
    # RequestTypeNotSupported = 3
    # InvalidInstrumentStructureSpecified = 12


class SessionRejectReason(IntEnum):
    InvalidTagNumber = 0
    RequiredTagMissing = 1
    TagNotDefinedForThisMessageType = 2
    UndefinedTag = 3
    TagSpecifiedWithoutValue = 4
    ValueIsIncorrect = 5
    IncorrectDataFormatForValue = 6
    DecryptionProblem = 7
    SignatureProblem = 8
    SendingTimeAccuracyProblem = 10
    InvalidMsgType = 11
    IncorrectNumInGroupCountForRepeatingGroup = 16
    Other = 99


class SecurityTradingStatus(IntEnum):
    OpeningDelay = 1
    TradingHalt = 2
    Resume = 3
    NoOpen = 4
    ReadyToTrade = 17
    UnknownOrInvalid = 20
    PreOpen = 21
    PostClose = 26
    PreClose = 51
    RestrictedOpen = 52
    Failed = 53


class SubscriptionRequestType:
    Snapshot = "0"
    SnapshotAndUpdates = "1"
    Unsubscribe = "2"

class TimeInForce:
    Day = "0"
    GoodTillCancel = "1"
    AtTheOpening = "2"
    ImmediateOrCancel = "3"
    FillOrKill = "4"
    GoodTillDate = "6"
    AtTheClose = "7"

class TradeCondition:
    OpeningPrice = "R"
    HighPrice = "AX"
    LowPrice = "AY"


class TradSesStatus(IntEnum):
    Unknown = 0
    Halted = 1
    Open = 2
    Closed = 3
    PreOpen = 4
    PreClose = 5
    RequestRejected = 6


class UserStatus(IntEnum):
    Other = 6
    ForcedUserLogoutByExchange = 7
    SessionShutdownWarning = 8
    Disconnected = 9


class ZMCap(IntEnum):
    GetInstrumentFields = 0
    ListEndpoints = 2
    SecurityDefinitionOOBSnapshot = 5
    SecurityDefinitionSubscribe = 6
    SecurityListOOBSnapshot = 10
    SecurityListSubscribe = 11
    MarketDefinitionOOBSnapshot = 15
    MarketDefinitionSubscribe = 16
    TradingSessionStatusOOBSnapshot = 20
    TradingSessionStatusSubscribe = 21
    SecurityStatusOOBSnapshot = 25
    SecurityStatusSubscribe = 26
    ListDirectoryOOBSnapshot = 30
    ListDirectorySubscribe = 31
    MDOOBSnapshot = 50
    MDSubscribe = 51
    MDSnapshot = 52
    MDMBP = 53
    MDMBPIncremental = 54
    MDMBPExplicitDelete = 55
    MDBBO = 56
    MDMBO = 60
    MDMBPPlusMBO = 61
    MDSaneMBO = 62




class ZMRejectReason(IntEnum):
    Other = 0
    InvalidValue = 1
    InvalidMsgType = 3
    UnknownInstrument = 4
    InsufficientPermissions = 5
    RequiredFieldMissing = 6
    ConditionallyRequiredFieldMissing = 7
    InvalidPriceIncrement = 8
    UnsupportedMsgType = 9
    InvalidField = 10
    NoData = 11
