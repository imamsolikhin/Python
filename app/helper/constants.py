"""
Constants used by apps.
"""

# local imports
from ..config import settings

# ------------ General Constants -----------------
TEXT_SUCCESS_DATA = "Data successfully"
TEXT_ERORR_DATA = "Data unsuccessfully"
TEXT_FAILED_CONNECT = "Connection Fail"
TEXT_SUCCESS_CONNECT = "Connection Success"
TEXT_ALREADY_EXISTS = "Already Exists"
TEXT_DOES_NOT_EXISTS = "Does Not Exists"
TEXT_OPERATION_SUCCESSFUL = "Data successfully saved"
TEXT_OPERATION_UNSUCCESSFUL = "Operation Unsuccessful"
TEXT_MISSING_PARAMS = "Params are missing"
INVALID_DATA = "Invalid data"

# ------------ OpenExchangeRates Api Url -----------------
OPEN_EXCHANGE_RATES_API_URL = 'https://openexchangerates.org/api/latest.json?app_id='+settings.APP_ID  #pylint: disable=line-too-long
