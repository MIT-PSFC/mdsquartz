import tempfile
import quartz
run_id = "8eed82c5-bec8-430f-8451-665631214fc6"
dataset = "test-dataset"
data_access_client = quartz.DataAccessClient(quartz.PRODUCTION_DATA_ACCESS_URL)

with tempfile.NamedTemporaryFile() as f:
    data_access_client.upload_file(run_id, f.name)

