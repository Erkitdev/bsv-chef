import pytest
import unittest.mock as mock
from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet

@pytest.fixture
def sut():
    mockedController = mock.MagicMock()
    return mockedController

@pytest.mark.unit
def test_getRecipe_compliant_strategy_true(sut = mock.MagicMock()):
    sut.get_readiness_of_recipes.return_value = {
        "Normal": 0.1
    }
    result = RecipeController.get_recipe(sut, diet=Diet.NORMAL, take_best=True)
    assert result == "Normal"

@pytest.mark.unit
def test_getRecipe_compliant_strategy_false(sut = mock.MagicMock()):
    sut.get_readiness_of_recipes.return_value = {
        "Recipe1": 0.1
    }
    result = RecipeController.get_recipe(sut, diet=Diet.NORMAL, take_best=False)
    assert result == "Recipe1"

@pytest.mark.unit
def test_getRecipe_notcompliant(sut = mock.MagicMock()):
    sut.get_readiness_of_recipes.return_value = {}
    result = RecipeController.get_recipe(sut, diet="not compliant", take_best=True)
    assert result == None

@pytest.mark.unit
def test_getRecipe_low_readiness(sut = mock.MagicMock()):
    sut.get_readiness_of_recipes.return_value = {
        "Recipe1": 0.09
    }
    result = RecipeController.get_recipe(sut, diet=Diet.NORMAL, take_best=True)
    assert result == None