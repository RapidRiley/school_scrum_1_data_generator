import random, hashlib, os, uuid, time, json
from datetime import datetime

def generate_file_timestamp() -> str:
    return datetime.now().strftime("%Y-%h-%d_%H-%M-%S")

def generate_manifest_timestamp() -> str:
    return datetime.now().strftime("%Y-%h-%d %H:%M:%S")


def log_error(log_text: str):
    log_string = "[Error!] " + generate_manifest_timestamp() + ": " + log_text + "\n"
    print(log_string)
    with open("./log.txt", "w") as file:
        file.write(log_string)

def log_warning(log_text: str):
    log_string = "[Warning] " + generate_manifest_timestamp() + ": " + log_text + "\n"
    print(log_string)
    with open("./log.txt", "w") as file:
        file.write(log_string)

def log_message(log_text: str):
    log_string = "[Message] " + generate_manifest_timestamp() + ": " + log_text + "\n"
    print(log_string)
    with open("./log.txt", "w") as file:
        file.write(log_string)


# Get data folder from ENV
data_dir: str = os.environ.get("DATA_DIR")
if(data_dir == None):
    data_dir = "./data"
data_dir += "/"
log_message(f"Data output dir: {data_dir}")

def generate_data_row(column_count: int, range_max: int = 10000, range_min: int = 0) -> str:
    # Catch edge cases
    if column_count < 1: return ""
    if column_count == 1: return str(random.randranage(range_min, range_max))

    content =""
    for i in range(0, column_count):
        content += str(random.randrange(range_min, range_max)) + ", "

        # If the current column is the last one, append the timestamp
        if i == column_count - 1: 
            content += datetime.now().strftime("%Y-%h-%d_%H:%M:%S:%f")
    content += "\n"

    return content

def generate_csv_content(row_count: int) -> str:
    content: str = "COL_1, COL_2, COL_3, TIMESTAMP\n"
    for i in range(0, row_count): content += generate_data_row(3)
    return content


def generate_hash(content: str) -> str:
    hash = hashlib.md5(content.encode("utf8"))
    return str(hash.hexdigest())




def generate_manifest(files: list[str]) -> dict:
    return {
        "uuid": str(uuid.uuid4()),
        "generated_on": generate_manifest_timestamp(),
        "batches": files
    }


def write_data(base_file_name: str, content: str) -> None:
    with open(data_dir + base_file_name + ".csv", "x") as file:
        file.write(content)


def write_hash(base_file_name: str, hash: str) -> None:
    with open(data_dir + base_file_name + ".md5", "x") as file:
        file.write(hash)


def write_manifest(file_list: list[str]) -> None:
    with open(data_dir + "manifest.json", "w") as file:
        file.write(json.dumps(generate_manifest(file_list)))


def loop():
    file_list: list[str] = []

    while True:
        random.seed()

        # Generate File contents
        content = generate_csv_content(random.randrange(1, 15))
        hash = generate_hash(content)

        file_name = "cern_data_" + generate_file_timestamp()
        file_list.append(file_name)

        # Write data, hash and manifest files
        write_data(file_name, content)
        write_hash(file_name, hash)
        write_manifest(file_list)

        sleep_timer = random.randrange(1, 3600)
        log_message(f"Generating next batch in {sleep_timer} seconds.")
        time.sleep(sleep_timer)

def main():
    try:
        log_message("Starting generator")
        loop()
    except KeyboardInterrupt:
        log_message("Exitting...")
        return 0

if __name__ == "__main__":
    main()