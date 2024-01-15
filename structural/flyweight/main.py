from os import getcwd
import datetime
from enum import StrEnum, auto
from typing import Dict, List


def current_year():
    today = datetime.date.today()
    return today.year


class LicenseType(StrEnum):
    MIT = auto()
    ISC = auto()
    GNU = auto()


class License:
    def __init__(self, license_type: LicenseType):
        self.license_type = license_type
        with open(f"{getcwd()}/licenses/{self.license_type.upper()}.txt", "r") as f:
            self.description = "".join(f.readlines())


class Repository:
    def __init__(self, author: str, license: License) -> None:
        self.author = author
        self.year = current_year()
        self.license = license

    def show_license(self) -> None:
        with_author = self.license.description.replace("<author>", self.author)
        with_author_and_year = with_author.replace("<year>", str(self.year))
        print(with_author_and_year)


class LicenseFactory:
    _licenses: Dict[int, License] = {}

    def __init__(self, licenses: List[License]) -> None:
        for license in licenses:
            self._licenses[self.get_key(license.license_type)] = license

    @staticmethod
    def get_key(license_type: LicenseType) -> int:
        return hash(license_type)

    def get_license(self, license_type: LicenseType) -> License:
        key = self.get_key(license_type)
        if not self._licenses.get(key):
            print("Creating new flyweight license\n")
            license = License(license_type)
        else:
            print("Get existing flyweight license\n")
            license = self._licenses.get(key)
        return license


def create_repository(f: LicenseFactory, author: str, license_type: LicenseType):
    license = f.get_license(license_type)
    repository = Repository(author, license)
    repository.show_license()


if __name__ == "__main__":
    mit = License(LicenseType.MIT)
    # isc = License(LicenseType.ISC)
    gnu = License(LicenseType.GNU)

    factory = LicenseFactory([mit, gnu])

    create_repository(factory, author="Artem Vladimirov", license_type=LicenseType.MIT)
    print("\n")
    create_repository(factory, author="Pavlo Tsaruk", license_type=LicenseType.ISC)
