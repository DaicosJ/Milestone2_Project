import wx
import pandas as pd
from NutritionalDataBaseFrame import MainFrame

def load_dataset(file_path='.\Food_Nutrition_Dataset.csv'):
    df = pd.read_csv(file_path)
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

def reset_filters(df):
    return df

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None)
        self.frame.Show()
        self.dataframe = load_dataset()

        self.frame.m_button1.Bind(wx.EVT_BUTTON, self.on_search)
        self.frame.m_button2.Bind(wx.EVT_BUTTON, self.on_reset)
        
        return True
    
    def on_search(self, event):
        protein = self.frame.m_textCtrl1.GetValue()
        fat = self.frame.m_textCtrl2.GetValue()
        carbs = self.frame.m_textCtrl3.GetValue()
        calories = self.frame.m_textCtrl4.GetValue()
        
        print(f"Input Values - Protein: {protein}, Fat: {fat}, Carbs: {carbs}, Calories: {calories}")

        try:
            if protein == "" and fat == "" and carbs == "" and calories == "":
                wx.MessageBox("Please Enter at least one nutritional calue to search.", 'Input Required', wx.OK | wx.ICON_WARNING)
                return
            
            protein = float(protein) if protein else None
            fat = float(fat) if fat else None
            carbs = float(carbs) if carbs else None
            calories = float(calories) if calories else None

            print(f"DataFrame Columns: {self.dataframe.columns}")

            filtered_data = search_nutritional_values(self.dataframe, protein, fat, carbs, calories)
            if filtered_data.empty:
                wx.MessageBox("No results found", 'Info', wx.OK | wx.ICON_INFORMATION)
            else:
                results_str = filtered_data.to_string(index=False)
                self.frame.m_textCtrl13.SetValue(results_str)    
            
        except ValueError:
            wx.MessageBox('Please enter valid numerical values.', 'Error', wx.OK | wx.ICON_ERROR)
        except Exception as e:
            wx.MessageBox(f'An error occurred: {str(e)}', 'Error', wx.OK | wx.ICON_ERROR)
    
    def on_reset(self, event):
        self.frame.m_textCtrl1.SetValue("")
        self.frame.m_textCtrl2.SetValue("")
        self.frame.m_textCtrl3.SetValue("")
        self.frame.m_textCtrl4.SetValue("")
        self.dataframe = reset_filters(self.dataframe)

if __name__=="__main__":
    app = MyApp()
    app.MainLoop()