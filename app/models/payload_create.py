from typing import List
from pydantic import BaseModel


class Payload(BaseModel):
	project_name: str
	project_description: str


def payload_to_list(payload: Payload) -> List:
	payload_list = [
		payload.project_name,
		payload.project_description,
	]

	return payload_list
