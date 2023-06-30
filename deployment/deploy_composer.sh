PROJECT_ID="$1"
LOCATION="$2"
IMAGE_VERSION="$3"
ZONE="$4"
COMPOSER_ENV_NAME="$5"
MACHINE_TYPE="$6"
NODE_COUNT="$7"
SERVICE_ACCOUNT="$8"

gcloud config set project "$PROJECT_ID"
gcloud composer environments create "$COMPOSER_ENV_NAME" \
  --location "$LOCATION" \
  --image-version "$IMAGE_VERSION" \
  --zone "$ZONE" \
  --machine-type "$MACHINE_TYPE" \
  --node-count "$NODE_COUNT" \
  --service-account "$SERVICE_ACCOUNT"
