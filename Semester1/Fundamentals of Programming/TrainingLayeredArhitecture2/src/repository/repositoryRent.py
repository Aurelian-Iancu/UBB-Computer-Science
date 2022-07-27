from src.domain.rent import Rent
from datetime import datetime


class RentRepoTextFile:
    def __init__(self, file_path):
        self._file_path = file_path
        self._list_of_rents = []
        self._read_all_from_file()

    def _read_all_from_file(self):
        self._list_of_rents.clear()
        with open(self._file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    line = line.split(",")
                    rent = Rent(int(line[0]), line[1],
                                datetime.fromisoformat(line[2]).date(), int(line[3]))
                    self._list_of_rents.append(rent)

    def __len__(self):
        return len(self._list_of_rents)

    def get_all_rents(self):
        return self._list_of_rents

