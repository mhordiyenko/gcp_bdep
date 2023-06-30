PROJECT_ID="$1"
LOCATION="$2"
COMPOSER_ENV_NAME="$3"

DATE_START="$4"
GCP_PROJECT_ID="$5"
BQ_PROJECT_ID="$6"
BQ_WORKING_DATASET_NAME="$7"



gcloud config set project $PROJECT_ID

gcloud composer environments update $COMPOSER_ENV_NAME \
  --update-env-variables=DATE_START=$DATE_START \
  --update-env-variables=GCP_PROJECT_ID=$GCP_PROJECT_ID \
  --update-env-variables=BQ_PROJECT_ID=$BQ_PROJECT_ID \
  --update-env-variables=BQ_WORKING_DATASET_NAME=$BQ_WORKING_DATASET_NAME \
  --location $LOCATION
