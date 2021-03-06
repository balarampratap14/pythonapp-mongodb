import datetime
from bson import ObjectId
import pymongo
def documents():
	list_of_doc = [{'_id': '78061813',
	 'debtorDetails': {'addresses': [], 'name': 'Lachelle Jones_Mcgill'},
	 'contactDetails': {'phones': [{'number': '4076169540',
		'type': None,
		'isCellular': None,
		'status': None}],
	  'emailAddresses': []},
	 'account': '78061813',
	 'callRecords': [{'_id': '464919ec-e1de-410f-9dea-fa7d9db51ecd',
	   'title': 'Non-Contact',
	   'result': 'AGENT - No Message Left on AM',
	   'phoneNumber': '4076169540',
	   'timestamp': datetime.datetime(2020, 5, 7, 13, 45, 24),
	   'timeslot': {'day': 4, 'hour': 9},
	   'sessionId': 'U9B45FT5EB410F1@10.40.88.11',
	   'duration': 92.16,
	   'isContact': 'N'},
	  {'_id': '06e29a7a-eb8c-429d-9bab-e249bcaacece',
	   'title': 'Non-Contact',
	   'result': 'AGENT - Left Message Machine',
	   'phoneNumber': '4076169540',
	   'timestamp': datetime.datetime(2020, 5, 11, 12, 2, 14),
	   'timeslot': {'day': 1, 'hour': 8},
	   'sessionId': 'U6E2ET5EB93EBF@10.40.88.155',
	   'duration': 80.352,
	   'isContact': 'N'},
	  {'_id': 'f9fad33c-f239-4eac-8b94-0f1cd22b54a7',
	   'title': '',
	   'result': 'Operator Transfer',
	   'phoneNumber': '4076169540',
	   'timestamp': datetime.datetime(2020, 5, 19, 13, 17, 13),
	   'timeslot': {'day': 2, 'hour': 9},
	   'sessionId': 'U3BFA7T5EC3DC30@10.40.88.98',
	   'duration': 76.464,
	   'isContact': 'N'}],
	 'state': None,
	 'isActive': True,
	 'amount_due': 0.0,
	 'last_worked': datetime.datetime(2020, 5, 19, 13, 17, 13),
	 'latest_agent_disposition': 'Operator Transfer'} ,
	{'_id': ObjectId('5eb55a95a2fb35f5ff570367'),
	 'person': {'firstName': 'Lachelle',
	  'lastName': 'Jones Mcgill',
	  'email': '',
	  'ssn': '',
	  'zipCode': ''},
	 'guarantor': {'firstName': '', 'lastName': ''},
	 'phone': [{'phone': '4076169540',
	   'ordinal': 1,
	   'phoneBlock': 'NONE',
	   'smsConsent': False,
	   'cellConsent': False}],
	 'account': '78061813',
	 'active': True,
	 'balance': 0.0,
	 'accountBlock': 'NONE',
	 'accountSMSBlock': False,
	 'accountEmailBlock': False,
	 'accountToSpeak': '78061813',
	 'originalAccountNumber': '',
	 'address1': '',
	 'address2': '',
	 'city': '',
	 'state': '',
	 'amountToSpeak': 0.0,
	 'groupId': 0,
	 'primaryEmailConsent': False,
	 'primarySMSConsent': False,
	 'callAttemptsToday': 0,
	 'callAttemptsTotal': 1,
	 'initialLoad': 1588841194000,
	 'lastLoad': 1588841194000,
	 'createDate': 1588841194000,
	 'modifyDate': 1588844721000} ,
	{'_id': 15454,
	 'serviceId': 15454,
	 'name': '15454_Office 1_AG (1)',
	 'callCenterId': 881,
	 'abbreviation': '1',
	 'unattended': False,
	 'termCodeEnabled': True,
	 'acdFeatureCode': 'AGENT_AT_READY_IN',
	 'callDirection': 'OUTBOUND',
	 'previewMode': 'NONE',
	 'phone': {'callerId': ['8883564495', '8882623446'],
	  'serviceId': 15454,
	  'name': '15454_Office 1_AG (1)',
	  'callCenterId': 881,
	  'operatorPhone': '6785781020',
	  'callbackPhone': '8882623446',
	  'agentCallInNumber': '4046316512',
	  'defaultCallerId': '8882623446'},
	 'screenPopId': 34300,
	 'cycleSortDaily': False,
	 'serviceLevelSeconds': 20,
	 'contactMaxAttemptsPerDay': 0,
	 'accountMaxAttemptsPerDay': 0,
	 'dialingProfileId': 17854,
	 'dialingRestriction': 1,
	 'dialingSort': 'DEFAULT',
	 'zipAreaMismatch': 'DIALTIME_OVERLAY',
	 'scrubOption': 'NONE',
	 'isCrossRequeueable': True,
	 'crossRequeueable': True,
	 'volumeControlEnabled': False,
	 'acdScheduledCallbackPhReadonly': False,
	 'acdScheduledCallback': 'DISABLED',
	 'acdPtpEnabled': True,
	 'previewManualAllowed': False,
	 'previewSkipAllowed': True,
	 'previewConfirmDial': False,
	 'previewTimeout': 30,
	 'callRecordingEnabled': True,
	 'leaveNoMessages': False,
	 'leaveMessages': False,
	 'callerIdSourceId': 0,
	 'callbackPhoneSourceId': 0,
	 'operatorPhoneSourceId': 0,
	 'callAcceptanceEnabled': False,
	 'callAcceptanceTimeout': 0} ,
	{'_id': 'A0017', 'name': 'Angel Hodo Atlanta', 'alias': 'ANGEL.HODO'} ,
	{'_id': 'U8F6ET5EA7039F@10.40.96.56',
	 'account': '019813196',
	 'service': 'Nissan Rollover2',
	 'name': '',
	 'phone': '5162216511',
	 'agent': 'TCOLLINS',
	 'session': 'U8F6ET5EA7039F@10.40.96.56',
	 'transferConnect': 1588003743000,
	 'transferEnd': 1588004182000,
	 'transferDuration': 438,
	 'campaign': '116825_CALLBACK_CALLS_04-27-2020',
	 'termCode': 'AGENT - PTP Arranged',
	 'serviceId': 116825,
	 'callCenterId': 8685,
	 'recordingId': '4e270fff-1937-b158-f0d5-0171bc6626d9',
	 'downloadFailed': False,
	 'downloadFile': '20200427120903_019813196_5162216511.mp3'} ,
	{'_id': 82325,
	 'name': 'Retained Attorney',
	 'serviceId': 15454,
	 'termCategoryId': 14390,
	 'lvResultId': 723,
	 'action': 'DISCONNECT_CALL',
	 'reportOrder': 7,
	 'previewDialEnabled': False,
	 'termCategoryName': 'Right Party',
	 'resultName': 'AGENT - Attorney Handling',
	 'id': 82325} ]
	  
	return list_of_doc
	  
	  


