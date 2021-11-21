# Installation guide
After cloning the repo, enter the `analytics_dashboard` folder and run
```bash
npm i
```
To install all the dependencies of cube.js.

You then need to create the file `.env`, putting your configuration specific parameters in place of the cury bracketed ones.
```
# Cube.js environment variables: https://cube.dev/docs/reference/environment-variables
CUBEJS_DEV_MODE=true
CUBEJS_DB_TYPE=mysql
CUBEJS_API_SECRET=96869e519f552e3912637facfd08193715472f142519f12f29db221f34206969127656cb20cb6679c0d5dcca7e10e2df65fa7ee589e4f7087e6a179938f13336
CUBEJS_EXTERNAL_DEFAULT=true
CUBEJS_SCHEDULED_REFRESH_DEFAULT=true
CUBEJS_WEB_SOCKETS=true
CUBEJS_DB_HOST={db_host}
CUBEJS_DB_USER={user}
CUBEJS_DB_PASS={password}
CUBEJS_DB_NAME={database_name}
```