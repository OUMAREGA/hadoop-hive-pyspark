DROP TABLE IF EXISTS air;

CREATE TABLE air(
`iso3` string,
`country` string,
`city` string,
`pm10` int,
`pm25` int,
`Year` string,
`population` int)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
with serdeproperties (
   "separatorChar" = ",",
   "quoteChar"     = "\"",
   "escapeChar"    = "\\"
  )
STORED AS TEXTFILE LOCATION '/user/hadoop/data/';