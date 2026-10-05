from khmer_ua import map_sequence, render_ipa_profile

def test_public_api_exports_research_functions():
    assert map_sequence(["kʰ", "a"]) == "ка"
    assert render_ipa_profile("krɑː", "careful_standard") == "krɑː"
