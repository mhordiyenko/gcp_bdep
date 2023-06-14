CREATE OR REPLACE TABLE `{table_path}`
(
  id STRING,
  followers INT64,
  genres ARRAY<STRING>,
  name STRING,
  popularity INT64
)
CLUSTER BY id
;

--`possible-stock-389114.spotify_data.artists`