import cookiecutter.main as cookiecutter

from consts.paths import PROJECT_PATH, COOKIECUTTER_CONFIG_PATH


def generate_project(
	project_name, project_description
):
	# Define project directory
	project_dir = f'./{project_name}'

	# Define context for the template
	context = {
		'project_name': project_name,
		'project_description': project_description,
	}
	# Generate project using Cookiecutter
	cookiecutter.cookiecutter(
		PROJECT_PATH,
		project_dir,
		no_input=True,
		extra_context=context,
		config_file=COOKIECUTTER_CONFIG_PATH,
	)

	return project_dir
