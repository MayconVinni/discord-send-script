import re
import requests
from requests import Response
from typing import Final, Union, List, Any

def script_to_list(script: str) -> List[str]:
	list_result: List[str] = re.split(r'[\n\t]+', script)
	size: int = len(list_result)
	
	if not list_result[0].strip():
		del list_result[0]
	
	if not list_result[size - 1].strip():
		del list_result[size - 1]
	
	return list_result

def send_script(token: str, channel_id: Union[int, str], script: List[str]) -> Response:
	URL: Final[str] = f'https://discord.com/api/v9/channels/{channel_id}/messages'
	HEADERS: Final[dict[str, Any]] = {
		'Authorization': token,
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
	}
	body: dict[str, str] = {}
	
	for index, line in enumerate(script):
		body['content'] = line
		
		response: Response = requests.post(
			URL,
			headers=HEADERS,
			json=body
		)
		
		yield response
