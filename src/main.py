import os, uuid, time, json
from datetime import datetime, timedelta

from log import Log
from manifest import Manifest
from batch import Batch

# Get data folder from ENV
data_dir: str = os.environ.get("DATA_DIR")
if(data_dir == None):
	data_dir = "./data"
Log.message(f"Data output dir: {data_dir}")


def load_manifest() -> dict:
	try:
		with open(f"{data_dir}/manifest.json", "r") as file:
			return json.load(file)
	except FileNotFoundError:
		Log.warning("Manifest file does not exist, creating it...")
	return None


def get_manifest_data() -> dict:
	current_manifest = load_manifest()
	if current_manifest == None:
		return {
			"batches": [],
			"final_run_id": 0
		}
	return current_manifest
	

def main():
	Log.message("Starting generator")

	# Load manifest
	manifest_data: dict = get_manifest_data()

	# Create new batch
	batch = Batch(manifest_data["final_run_id"] + 1)

	# Get batch list and add new batch to it.
	batch_list: list[str] = manifest_data["batches"]
	batch_list.append(batch.get_batch_name())

	# Create updated manifest
	manifest = Manifest(
		batch_list,
		batch.get_final_run_id()
	)

	# Write files
	batch.write_file(data_dir)
	manifest.write_file(data_dir)
 
if __name__ == "__main__":
	main()