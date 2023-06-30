# gcp_bde


## Pipeline deployment
All commands should be run from the project's root

### 1. Set up configuration variables

#### For Dev/Test environment
```
PROJECT_ID=possible-stock-389114
LOCATION=us-central1
ZONE=us-central1-c
COMPOSER_ENV_NAME=composer-1-20-12-airflow-2-4-3
IMAGE_VERSION=composer-1.20.12-airflow-2.4.3
MACHINE_TYPE=n1-standard-1
NODE_COUNT=3
SERVICE_ACCOUNT=gbdep-composer@possible-stock-389114.iam.gserviceaccount.com

DATE_START='2017-06-01'
GCP_PROJECT_ID='possible-stock-389114'
BQ_PROJECT_ID='possible-stock-389114'
BQ_WORKING_DATASET_NAME='spotify_data_test'
```

### 2. Create Composer environment
By default, it includes 3 VMs of `n1-standard-1` type. The command to create Composer environment:
```
./deployment/deploy_composer.sh \
    $PROJECT_ID \
    $LOCATION \
    $IMAGE_VERSION \
    $ZONE \
    $COMPOSER_ENV_NAME \
    $MACHINE_TYPE \
    $NODE_COUNT \
    $SERVICE_ACCOUNT
```
### 3. Set up Airflow environment variables
```
./deployment/set_airflow_env_vars.sh \
    $PROJECT_ID \
    $LOCATION \
    $COMPOSER_ENV_NAME \
    $DATE_START \
    $GCP_PROJECT_ID \
    $BQ_PROJECT_ID \
    $BQ_WORKING_DATASET_NAME \
```
### 4. Delete Composer environment
```
./deployment/delete_composer.sh \
    $PROJECT_ID \
    $COMPOSER_ENV_NAME \
    $LOCATION    
```
