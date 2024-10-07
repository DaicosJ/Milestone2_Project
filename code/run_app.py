import wx
import pandas as pd
import matplotlib.pyplot as plt
from NutritionalDataBaseFrame import MainFrame

def load_dataset(file_path='./Food_Nutrition_Dataset.csv'):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    print(df.columns)
    return pd.read_csv(file_path)

def search_nutritional_values(df, protein=None, fat=None, carbs=None, calories=None):
    filtered_df=df
    if protein is not None:
        filtered_df = filtered_df[filtered_df['Protein'] >= protein]
    if fat is not None:
        filtered_df = filtered_df[filtered_df['Fat'] >= fat]
    if carbs is not None:
        filtered_df = filtered_df[filtered_df['Carbohydrates'] >= carbs]
    if calories is not None:
        filtered_df = filtered_df[filtered_df['Caloric Value'] >= calories]
    
    return filtered_df

def plot_nutrition(dataframe):
    values = [dataframe['Protein'].sum(), dataframe['Fat'].sum(), dataframe['Carbohydrates'].sum()]
    labels = ['Protein', 'Fat', 'Carbohydrates']
    
    if len(values) == len(labels):
        plt.bar(labels, values)
        plt.title('Nutritional Content')
        plt.ylabel('Grams')
        plt.show()

def reset_filters(df):
    return df

def save_results_to_csv(filtered_data, filepath='filtered_results.csv'):
    try:
        if not filtered_data.empty:
            filtered_data.to_csv('filtered_results.csv', index=False)
            print(f"Data successfully saved to {filepath}")
        else:
            raise ValueError("The Dataframe is empty, No data saved.")
    except:
        print(f"Error saving file {filepath}: ")

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None)
        self.frame.Show()
        self.dataframe = load_dataset()

        self.frame.m_button1.Bind(wx.EVT_BUTTON, self.on_search)
        self.frame.m_button2.Bind(wx.EVT_BUTTON, self.on_reset)
        self.frame.m_button3.Bind(wx.EVT_BUTTON, self.on_save_csv)
        
        return True
    
    def on_search(self, event):
        protein = self.frame.m_textCtrl1.GetValue()
        fat = self.frame.m_textCtrl2.GetValue()
        carbs = self.frame.m_textCtrl3.GetValue()
        calories = self.frame.m_textCtrl4.GetValue()

        if not all([protein, fat, carbs, calories]):
            wx.MessageBox('Please fill in all fields before searching', 'Error', wx.OK | wx.ICON_ERROR)
            return

        try:

            protein = float(protein) if protein else None
            fat = float(fat) if fat else None
            carbs = float(carbs) if carbs else None
            calories = float(calories) if calories else None

            filtered_data = search_nutritional_values(self.dataframe, protein, fat, carbs, calories)
            
            if not filtered_data.empty:
                self.filtered_data = filtered_data
                num_rows = filtered_data.shape[0]
                num_cols = 5

                current_rows = self.frame.m_grid1.GetNumberRows()
                if current_rows < num_rows:
                    self.frame.m_grid1.AppendRows(num_rows - current_rows)
                elif current_rows > num_rows:
                    self.frame.m_grid1.DeleteRows(0, current_rows - num_rows)
                
                current_cols = self.frame.m_grid1.GetNumberCols()
                if current_cols < num_cols:
                    self.frame.m_grid1.AppendCols(num_cols - current_cols)
                elif current_cols > num_cols:
                    self.frame.m_grid1.DeleteCols(0, current_cols - num_cols)
            
                self.frame.m_grid1.SetColLabelValue(0, 'food')
                self.frame.m_grid1.SetColLabelValue(1, 'Caloric Value')
                self.frame.m_grid1.SetColLabelValue(2, 'Protein')
                self.frame.m_grid1.SetColLabelValue(3, 'Fat')
                self.frame.m_grid1.SetColLabelValue(4, 'Carbohydrates')
            
                for row_num, (index, row) in enumerate(filtered_data.iterrows()):                    
                    self.frame.m_grid1.SetCellValue(row_num, 0, str(row['food']))
                    self.frame.m_grid1.SetCellValue(row_num, 1, str(row['Caloric Value']))
                    self.frame.m_grid1.SetCellValue(row_num, 2, str(row['Protein']))
                    self.frame.m_grid1.SetCellValue(row_num, 3, str(row['Fat']))
                    self.frame.m_grid1.SetCellValue(row_num, 4, str(row['Carbohydrates']))
            else:
                self.frame.m_grid1.ClearGrid()
                wx.MessageBox('Please enter valid numerical values.', 'Error', wx.OK | wx.ICON_INFORMATION)
        except ValueError:
            wx.MessageBox('Please enter valid numerical values.', 'Error', wx.OK | wx.ICON_ERROR)


    def on_reset(self, event):
        self.frame.m_textCtrl1.SetValue("")
        self.frame.m_textCtrl2.SetValue("")
        self.frame.m_textCtrl3.SetValue("")
        self.frame.m_textCtrl4.SetValue("")
        self.dataframe = reset_filters(self.dataframe)

        num_rows = self.frame.m_grid1.GetNumberRows()
        num_cols = self.frame.m_grid1.GetNumberCols()

        for row in range(num_rows):
            for col in range(num_cols):
                self.frame.m_grid1.SetCellValue(row, col, "")

    def on_save_csv(self, event):
        try:
            if not self.filtered_data.empty:
                save_results_to_csv(self.filtered_data)
                wx.MessageBox("Search results saved to filtered_results.csv", "Success", wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox("No search results to save.", "Error", wx.OK | wx.ICON_INFORMATION)
        except AttributeError:
                wx.MessageBox("Please perform a search before saving results.", "Error", wx.OK | wx.ICON_INFORMATION)

if __name__=="__main__":
    app = MyApp()
    app.MainLoop()