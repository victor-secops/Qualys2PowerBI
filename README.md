# Qualys2PowerBI
Simple Script to Integrate Qualys With PowerBI using API

# Available Endpoints
Vulnerability API Format xml
https://qualysapi.qg3.apps.qualys.com/api/2.0/fo/asset/host/vm/detection/

Report API format csv string
https://qualysapi.qg3.apps.qualys.com/api/2.0/fo/report/?action=fetch&id=4337431

List knowledge by date API format xml
https://qualysapi.qg3.apps.qualys.com/api/2.0/fo/knowledge_base/vuln/?action=list&published_after=<AAAA-MM-DD>

# How to Use
install the necessary libraries and change the Authorization field of the header, to your username and password encoded to Base64. The format for documentation is username:password.

Example:
'Authorization': 'Basic dXN1YXJpbzpzZW5oYTEyMw=='

