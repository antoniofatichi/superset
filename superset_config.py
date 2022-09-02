# This is an important setting, and should be lower than your
# [load balancer / proxy / envoy / kong / ...] timeout settings.
# You should also make sure to configure your WSGI server
# (gunicorn, nginx, apache, ...) timeout setting to be <= to this setting
# SUPERSET_WEBSERVER_TIMEOUT = int(timedelta(minutes=1).total_seconds())
SUPERSET_WEBSERVER_TIMEOUT = 3600

# Timeout duration for SQL Lab synchronous queries
# SQLLAB_TIMEOUT = int(timedelta(seconds=30).total_seconds())
SQLLAB_TIMEOUT = 1800

# Timeout duration for SQL Lab query validation
# SQLLAB_VALIDATION_TIMEOUT = int(timedelta(seconds=10).total_seconds())
SQLLAB_VALIDATION_TIMEOUT = 60

# The MAX duration a query can run for before being killed by celery.
# SQLLAB_ASYNC_TIME_LIMIT_SEC = int(timedelta(hours=6).total_seconds())
SQLLAB_ASYNC_TIME_LIMIT_SEC = 216000

# Some databases support running EXPLAIN queries that allow users to estimate
# query costs before they run. These EXPLAIN queries should have a small
# timeout.
# SQLLAB_QUERY_COST_ESTIMATE_TIMEOUT = int(timedelta(seconds=10).total_seconds())
SQLLAB_QUERY_COST_ESTIMATE_TIMEOUT = 60

# default row limit when requesting chart data
# ROW_LIMIT = 50000
ROW_LIMIT = 1000000
