def myAssert(r, verifycode, expection="", contain=""):
    try:
        assert r.status_code == 200
        # print(info.text)
        if verifycode == 1:
            pass
            # logging.debug(str(info.json()))
        elif verifycode == 5:
            # logging.debug(str(info.text))
            assert r.json()["succeed"] == True
            assert type(r.json()["result"]) == dict
        # except:
        elif verifycode == 4:
            assert r.json()["isSuccess"] == True
            assert type(r.json()["data"]) == dict
        elif verifycode == 7:
            assert r.json()["isSuccess"] == True
            assert type(r.json()["data"]) == list
        elif verifycode == 3:
            assert r.json()["resultCode"] == 1
            assert type(r.json()["data"]) == dict
        elif verifycode == 2:
            assert r.json()["resultCode"] == 1
            assert type(r.json()["data"]) == list
        elif verifycode == 6:
            # logging.debug(str(info.text))
            assert r.json()["succeed"] == True
            assert type(r.json()["result"]) == str
        if expection:
            assert r.text == expection
        if contain:
            containstr = contain.split(",")
            for i in containstr:
                assert i in r.text
        return True
    except:
        return False
