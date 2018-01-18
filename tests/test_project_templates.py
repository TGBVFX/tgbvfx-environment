from tgbvfx_environment import utils
import lib


def get_project():
    return utils.mock_entity(
        ("disk", {"windows": "//10.11.0.184", "unix": "//10.11.0.184"}),
        ("root", "171001_ftrack"),
        ("name", "pipeline_test"),
        entity_type="Project"
    )


def test_project():
    lib.assert_entity(get_project())


def get_project_task():
    project = get_project()

    return utils.mock_entity(
        ("parent", project),
        ("project", project),
        ("name", "editing"),
        entity_type="Task"
    )


def test_project_task():
    lib.assert_entity(get_project_task())


def get_project_task_workfiles():
    entities = []
    task = get_project_task()
    for ext in lib.get_workfile_extensions():
        task = utils.mock_entity(
            ("project", task["project"]),
            ("parent", task["parent"]),
            ("version", 1),
            ("file_type", ext),
            ("name", "editing"),
            entity_type="Task"
        )
        entities.append(task)
    return entities


def test_project_task_workfiles():
    for entity in get_project_task_workfiles():
        lib.assert_entity(entity)


def get_entities():
    entities = []

    entities.append(get_project())
    entities.append(get_project_task())
    entities.extend(get_project_task_workfiles())

    return entities
