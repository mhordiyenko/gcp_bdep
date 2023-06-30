PROJECT_ID="$1"
COMPOSER_ENV_NAME="$2"
LOCATION="$3"

gcloud config set project "$PROJECT_ID"

BUCKET_NAME=$(gcloud composer environments describe "$COMPOSER_ENV_NAME" --location="$LOCATION" --format="value(config.dagGcsPrefix)")

gcloud composer environments delete "$COMPOSER_ENV_NAME" \
  --location "$LOCATION"

gsutil rm -r gs://"$BUCKET_NAME"
