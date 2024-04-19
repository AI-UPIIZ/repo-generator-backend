import os
import requests

from fastapi import HTTPException

from consts.consts import URL_API_GITHUB
from app.core.config import GITHUB_ORG_NAME, GITHUB_ACCESS_TOKEN


def create_github_repo(project_dir, project_name, project_description):
	url = f'{URL_API_GITHUB}/{GITHUB_ORG_NAME}/repos'
	payload = {
		'name': project_name,
		'description': project_description,
		'private': False,
	}
	headers = {
		'Authorization': f'token {GITHUB_ACCESS_TOKEN}',
		'Accept': 'application/vnd.github.v3+json',
	}

	response = requests.post(url, json=payload, headers=headers)

	create_first_commit(project_dir, project_name)

	if response.status_code not in {200, 201}:
		raise HTTPException(
			status_code=500,
			detail=f"Failed to create GitHub repository: {response.json()['message']}",
		)
	else:
		print('Repository created successfully')


def create_first_commit(project_dir, project_name):
	os.chdir(project_dir)
	os.system('git init')
	os.system('git add .')
	os.system("git commit -m 'Initial commit'")
	os.system(
		f'git remote add origin https://{GITHUB_ACCESS_TOKEN}@github.com/{GITHUB_ORG_NAME}/{project_name}.git'
	)
	os.system('git push -u origin master')
