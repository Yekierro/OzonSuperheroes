import pytest
from main import get_tallest_hero


def test_male_with_job():
    hero = get_tallest_hero("Male", True)
    assert hero is not None
    assert hero["appearance"]["gender"].lower() == "male"
    assert hero["work"]["occupation"].strip() != ""
    assert "cm" in hero["appearance"]["height"][1]
    assert int(hero["appearance"]["height"][1].replace("cm", "").strip()) > 0


def test_male_without_job():
    hero = get_tallest_hero("Male", False)
    assert hero is None or (
        hero["appearance"]["gender"].lower() == "male" and
        hero["work"]["occupation"].strip() == ""
    )


def test_female_with_job():
    hero = get_tallest_hero("Female", True)
    assert hero is not None
    assert hero["appearance"]["gender"].lower() == "female"
    assert hero["work"]["occupation"].strip() != ""


def test_female_without_job():
    hero = get_tallest_hero("Female", False)
    assert hero is None or (
        hero["appearance"]["gender"].lower() == "female" and
        hero["work"]["occupation"].strip() == ""
    )


def test_unknown_gender():
    hero = get_tallest_hero("Unknown", True)
    assert hero is None or hero["appearance"]["gender"].lower() == "unknown"


def test_case_insensitivity():
    hero_lower = get_tallest_hero("female", True)
    hero_upper = get_tallest_hero("FEMALE", True)
    assert hero_lower and hero_upper
    assert hero_lower["name"] == hero_upper["name"]


def test_output_structure():
    hero = get_tallest_hero("Male", True)
    assert "name" in hero
    assert "appearance" in hero
    assert "work" in hero


def test_return_none_when_no_match():
    hero = get_tallest_hero("Alien", False)
    assert hero is None

def test_result_is_dict():
    hero = get_tallest_hero("Male", True)
    assert isinstance(hero, dict)


def test_height_is_valid_number():
    hero = get_tallest_hero("Male", True)
    height = hero["appearance"]["height"][1]
    assert "cm" in height
    assert int(height.replace("cm", "").strip()) > 0


def test_hero_has_image():
    hero = get_tallest_hero("Male", True)
    assert "images" in hero
    assert "lg" in hero["images"]
    assert hero["images"]["lg"].startswith("http")


def test_different_filters_return_different_heroes():
    hero1 = get_tallest_hero("Male", True)
    hero2 = get_tallest_hero("Female", True)
    if hero1 and hero2:
        assert hero1["name"] != hero2["name"]


def test_gender_with_typo_returns_none():
    hero = get_tallest_hero("Femlae", True)
    assert hero is None
