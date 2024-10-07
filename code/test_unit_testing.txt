import sys
import os
import pytest
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from .run_app import load_dataset, search_nutritional_values, plot_nutrition, reset_filters, save_results_to_csv

@pytest.fixture
def sample_data():
    data = {
        'food': ['Apple', 'Banana', 'Chicken Breast', 'Broccoli'],
        'Caloric Value': [52, 89, 165, 55],
        'Protein': [0.3, 1.1, 31, 4],
        'Fat': [0.2, 0.3, 3.6, 0.6],
        'Carbohydrates': [14,23,0,11]
    }
    return pd.DataFrame(data)

def test_load_dataset():
    df = load_dataset('./Food_Nutrition_Dataset.csv')
    assert isinstance(df, pd.DataFrame), "Loaded data is not a DataFrame"
    assert not df.empty, "Loaded DataFrame is empty"
    assert 'food' in df.columns, "Column 'food' not found in the DataFrame"

def test_search_nutritional_values(sample_data):
    filtered_df = search_nutritional_values(sample_data, protein=1)
    assert len(filtered_df) == 3, "Expected 3 results for protein >= 1"

    filtered_df = search_nutritional_values(sample_data, protein=0.5)
    assert len(filtered_df) == 3, "Expected 3 results for protein >= 0.5"

    filtered_df = search_nutritional_values(sample_data, protein=10)
    assert len(filtered_df) == 1, "Expected 3 results for protein >= 10"

    filtered_df = search_nutritional_values(sample_data, protein=60)
    assert len(filtered_df) == 0, "Expected 3 results for protein >= 60"

def test_plot_nutrition(sample_data):
    try:
        plot_nutrition(sample_data)
    except Exception as e:
        pytest.fail(f"plot_nutrition raised as an exception: {e}")

def test_reset_filters(sample_data):
    reset_df = reset_filters(sample_data)
    pd.testing.assert_frame_equal(reset_df, sample_data, "reset_filters did not return the original DataFrame")

def test_save_results_to_csv(sample_data,):
    test_file_path = 'test_filtered_results.csv'
    save_results_to_csv(sample_data, test_file_path)

    assert os.path.exists(test_file_path), f"CSV file was not created at {test_file_path}"
    if os.path.exists(test_file_path):
        os.remove(test_file_path)

    assert os.path.exists(test_file_path), "CSV file was not created"
    saved_df = pd.read_csv(test_file_path)
    pd.testing.assert_frame_equal(saved_df, sample_data, "Saved data does not match the original DataFrame")

    os.remove(test_file_path)

if __name__=="__main__":
    pytest.main()