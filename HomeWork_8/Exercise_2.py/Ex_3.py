import csv
import json
from pprint import pprint

__all__ = ["convert_users_data_to_csv"]


def convert_users_data_to_csv(input_json: str, output_csv: str) -> None:
    with open(input_json, "r", encoding="utf-8") as f:
        users_data_dict = json.load(f)

    pprint(users_data_dict)
    fieldnames = ["id", "name", "level"]
    users_data_rows = [{fieldnames[0]: int(id_), fieldnames[1]: name, fieldnames[2]: int(level)}
                       for level, users in users_data_dict.items()
                       for id_, name in users.items()]
    pprint(users_data_rows)

    with open(output_csv, "w", encoding="utf-8", newline="") as f:
        csv_write = csv.DictWriter(f, fieldnames=fieldnames, restval="None", quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(users_data_rows)


if __name__ == '__main__':
    convert_users_data_to_csv("Exercise_2.json", "Exercise_3.csv")