import pytest
from app.processors.food_analyzer import OptimizedFoodAnalyzer
from app.processors.nutrition_manager import NutritionManager

def test_food_analysis_pipeline():
    analyzer = OptimizedFoodAnalyzer()
    nutrition_manager = NutritionManager()
    
    test_cases = [
        ("test_data/kimchi_stew.jpg", "김치찌개"),
        ("test_data/bibimbap.jpg", "비빔밥"),
        ("test_data/bulgogi.jpg", "불고기")
    ]
    
    for image_path, expected_food in test_cases:
        with open(image_path, 'rb') as f:
            result = analyzer.analyze_food(f)
            assert result['food_name'] == expected_food
            
            nutrition = nutrition_manager.get_nutrition_info(result['food_name'])
            assert nutrition is not None
            assert 'calories' in nutrition
