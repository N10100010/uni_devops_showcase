import urllib.request


###########################
# TEST THE ACTIVE CONTAINER
###########################
def test_active_container():
    # docker-compose up before that
    contents = urllib.request.urlopen("http://localhost:10000/").read()
    assert b"Feel welcomed to the greatest of all FizzBuzzes" in contents
