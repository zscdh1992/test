import pytest




@pytest.fixture(scope='package',autouse=True)
def couse2(request):
    print("*** !!! couse2 setting up ***")

    def teardown():
        print("*** !!! couse2 tear down ***")
 
    request.addfinalizer(teardown)