import logging
import requests
from vra_ipam_utils.exceptions import InvalidCertificateException
import json


def get_base_url(endpointProperties):
    
    logging.info("Generating BaseUrl for endpoint :" + endpointProperties["hostName"])

    try:
        baseUrl = "https://" + endpointProperties["hostName"] + "/api/" + endpointProperties["appId"] + "/"
        logging.info(f"Base Url = '{baseUrl}'")
        return baseUrl
    except Exception as e:
        logging.error("Error Generating baseUrl.")
        logging.error(e)
    
def get_bearer_token(baseUrl,auth_credentials,cert):
    
    logging.info("Retrieving the bearer token from phpIpam endpoit.")

    username = auth_credentials["privateKeyId"]
    password = auth_credentials["privateKey"]
    
    try:

        response = requests.post(baseUrl + "/user", verify=cert, auth=(username, password))

        if response.status_code == 200:
            
            logging.info("Successfully Retrieved Token.")
            
            #get the response
            body = response.json()

            #get the token from response
            token = body["data"]["token"]
            expires =  body["data"]["expires"]
            
            logging.info(f"Token Expires : {expires}")

            return {
                "token": token,
                "expires": expires
            }

        elif response.status_code == 401:
            logging.error(f"Invalid credentials error: {str(response.content)}")
            raise Exception(f"Invalid credentials error: {str(response.content)}")
        else:
            raise Exception(f"Failed to connect: {str(response.content)}")
    except Exception as e:
        """ In case of SSL validation error, a InvalidCertificateException is raised.
            So that the IPAM SDK can go ahead and fetch the server certificate
            and display it to the user for manual acceptance.
        """
        if "SSLCertVerificationError" in str(e) or "CERTIFICATE_VERIFY_FAILED" in str(e) or 'certificate verify failed' in str(e):
            raise InvalidCertificateException("certificate verify failed", self.inputs["endpointProperties"]["hostName"], 443) from e

        raise e
