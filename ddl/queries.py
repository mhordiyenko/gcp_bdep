def create_or_replace_artists(table_path):
    return f'''CREATE OR REPLACE TABLE `{table_path}`
    (
      id STRING,
      followers INT64,
      genres ARRAY<STRING>,
      name STRING,
      popularity INT64
    )
    CLUSTER BY id
    ;'''


def create_or_replace_tracks(table_path):
    return f'''CREATE OR REPLACE TABLE `{table_path}`(
      id STRING,
      name STRING,
      popularity INT64,
      duration_ms INT64,
      explicit BOOL,
      artists ARRAY<STRING>,
      id_artists ARRAY<STRING>,
      release_date DATE,
      danceability FLOAT64,
      energy FLOAT64,
      key INT64,
      loudness FLOAT64,
      mode BOOL,
      speechiness FLOAT64,
      acousticness FLOAT64,
      instrumentalness FLOAT64,
      liveness FLOAT64,
      valence FLOAT64,
      tempo FLOAT64,
      time_signature INT64
    )
    PARTITION BY release_date
    CLUSTER BY id
    ;
    '''
