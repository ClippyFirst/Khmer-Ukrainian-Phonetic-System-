from khmer_ua.practical import map_segment

def test_unknown_segment_is_not_silently_deleted():
    try:
        map_segment("UNKNOWN")
    except ValueError:
        pass
    else:
        raise AssertionError("unknown segment must not be silently deleted")
