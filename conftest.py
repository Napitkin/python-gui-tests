
import pytest

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Users\\napit\\OneDrive\\Рабочий стол\\ПРОГРАММИРОВАНИЕ НА PYTHON ДЛЯ ТЕСТИРОВЩИКОВ\\Portable_version_AddressBook\\AddressBook.exe")
    #"C:\Portable_version_AddressBook\AddressBook.exe"
    request.addfinalizer(fixture.destroy)
    return fixture