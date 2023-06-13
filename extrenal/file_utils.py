import os
import yaml
import datetime
from airflow.models import Variable

def read_yaml(address: str) -> dict:
    """Reads yaml files

    Args:
        address (str): address of the file/query to read

    Returns:
        dict: yaml dictionary
    """

    with open(address) as file:
        yaml_text = yaml.load(file, Loader=yaml.FullLoader)


def create_file_name_with_timestamp(base_file_name, timestamped_dir=True):
    """Creates date based folders to store files in destination

    Args:
        base_file_name (str): _description_
        timestamped_dir (bool, optional): _description_. Defaults to True.

    Returns:
         str: new_file_path returns updated file path
    """
    
    now_datetime = datetime.datetime.utcnow()
    now_datetime_formatted = now_datetime.strftime("%Y-%m-%d %H:%M")

    file_name_main_part = base_file_name.split('.')[0]
    file_name_main_part_with_time = f'{file_name_main_part}_{now_datetime_formatted}'

    new_file_name = base_file_name.replace(file_name_main_part, file_name_main_part_with_time)

    if timestamped_dir:
        new_file_name = f'{now_datetime.year}/{now_datetime.month}/{now_datetime.day}/{new_file_name}'
    new_file_path = base_file_name.replace(base_file_name, new_file_name)
    return new_file_path



def get_airflow_var(name, from_env_var=True):
    if from_env_var:
        airflow_var = os.getenv(name)
    else:
        airflow_var = Variable.get(name)
    if not airflow_var:
        raise ValueError(f"Please specify {name} variable")
    return airflow_var

# def get_dag_path():
#     return '/home/airflow/gcs/dags/'
