# sipgate_backup
Backup script to export the event history of a Sipgate user. Exports the events as a csv list and downloads the faxes, voice mail recordings etc. See Script for use. 
Tested with 
- sipgate team account in feb 2018
- Python 3.6.3
- Ubuntu 17.10

Install wget before use:
pip install wget

Before You start, put Your userid, credentials and settings in the first some lines. 
The userid can be retrieved from sipgate URL, i.e. last two letters of https://secure.live.sipgate.de/settings/phone/index/webuser/1234567w0 if logged in and switched to another account. I think, You must be admin to do it.

The script doesn't check, whether the userid and the credentials are correct. You can check both (in this example userid w3) with the following line from command promt:
curl -u sipgate_username:sipgate_password --request GET --url https://api.sipgate.com/v1/users/w3
(assuming curl is installed)
If everything is ok, it replies with a json answer like:
{"id":"w3","firstname":"John","lastname":"Doe","email":"johndoe@example.com","defaultDevice":"x12","admin":false}
If not, it gives no response on command line. Check Your credentials on the website and look for the right userid.
