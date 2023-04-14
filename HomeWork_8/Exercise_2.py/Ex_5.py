import csv
import pickle
from pprint import pprint

__all__ = ["pickle_to_csv"]


def pickle_to_csv(input_pickle, output_csv):
    with open(input_pickle, "rb") as f:
        data = pickle.load(f)

    headers_set = set({})
    for d in data:
        k = set(d.keys())
        headers_set = headers_set | k

    with open(output_csv, "w", encoding="utf-8", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=list(headers_set), restval="Empty", extrasaction="ignore",
                                    quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data)


if __name__ == '__main__':
    pickle_to_csv("Exercise_4.pickle", "Exercise_6.csv")