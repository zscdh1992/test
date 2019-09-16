import pytest




@pytest.fixture(scope='package',autouse=True)
def couse1(request):
    print("*** !!! couse1 setting up ***")

    def teardown():
        print("*** !!! couse1 tear down ***")
 
    request.addfinalizer(teardown)