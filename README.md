# vra8-phpIpamIntegration
vRealize Automaion 8.x - PHP Ipam Integration using 3rd Party SDK

This was developped to learn how to use the vRealize Automation 8 - Third Party Ipam Integration SDK
The sdk version 1.1 was used.
https://code.vmware.com/web/sdk/1.1.0/vmware-vrealize-automation-third-party-ipam-sdk

Documentation references :
https://docs.vmware.com/en/vRealize-Automation/8.2/Using-and-Managing-Cloud-Assembly/GUID-ADD9C0D7-328C-4DAD-BC83-9C0F5656FE98.html
https://docs.vmware.com/en/vRealize-Automation/8.2/Using-and-Managing-Cloud-Assembly/GUID-4A5A481C-FC45-47FB-A120-56B73EB28F01.html


Files that were modified from original sdk:

\phpIpam-sdk-v1.1\tango-ipam-sdk\
  - pom.xml 
    added the name, description and details of the integration

\phpIpam-sdk-v1.1\tango-ipam-sdk\src\main\resources\
 - logo.png
   changed for the php-ipam logo
   
 - endpoint-schema.json
   Added the application id field
   
 \phpIpam-sdk-v1.1\tango-ipam-sdk\src\main\python\commons
  - ipam_connector.py
    New module file, used to call function that are commonly used to access the phpIpam Api
  
 \phpIpam-sdk-v1.1\tango-ipam-sdk\src\main\python\validate_endpoint
 - source.py
   Added code required to validate the enpoint as described in the documentation.
  
 \phpIpam-sdk-v1.1\tango-ipam-sdk\src\main\python\get_ip_ranges
 - source.py
   Added code required to get ip ranges from the enpoint as described in the documentation.
 
 \phpIpam-sdk-v1.1\tango-ipam-sdk\src\main\python\allocate_ip
  - source.py
   Added code required to allocate ip in a range from the enpoint as described in the documentation.
   Added code required to rollback allocated ip from range from the enpoint as described in the documentation.
 
 \phpIpam-sdk-v1.1\tango-ipam-sdk\src\main\python\deallocate_ip
  - source.py
   Added code required to deallocate ip in a range from the enpoint as described in the documentation.
   
 

   
   

