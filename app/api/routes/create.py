from fastapi import APIRouter, Depends
from starlette.requests import Request
from fastapi.responses import JSONResponse

from app.services.generate_project import generate_project
from app.services.create_repo import create_github_repo
from app.models.payload_create import Payload
from app.core import security


router = APIRouter()


@router.post('/create', name='Create')
async def create_project(
	request: Request,
	authenticated: bool = Depends(security.validate_request),
	block_data: Payload = None,
):
	try:
		if not authenticated:
			return JSONResponse(status_code=401, content={'message': 'Unauthorized'})

		project_name = block_data.project_name
		project_description = block_data.project_description
		project_dir = generate_project(project_name, project_description)

		create_github_repo(project_dir, project_name, project_description)

		return JSONResponse(
			status_code=200,
			content={
				'message': 'Project created successfully',
				'github_repo_url': project_dir,
			},
		)
	except Exception as e:
		return JSONResponse(
			status_code=500,
			content={
				'message': 'An error occurred while creating the project: {}'.format(
					str(e)
				)
			},
		)
