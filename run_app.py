import wx
import pandas as pd
from NutritionalDataBaseFrame import MainFrame


def load_dataset(file_path='Food_Nutrition_Dataset.csv'):
    return pd.read_csv(file_path)


def search_nutritional_values(df, protein=None, fat=None, carbs=None, calories=None):
    filtered_df = df
    if protein:
        filtered_df = filtered_df[filtered_df['Protein (g)'] >= protein]
    if fat:
        filtered_df = filtered_df[filtered_df['Fat (g)'] >= fat]
    if carbs:
        filtered_df = filtered_df[filtered_df['Carbohydrates (g)'] >= carbs]
    if calories:
        filtered_df = filtered_df[filtered_df['Calories (g)'] >= calories]

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

        try:
            protein = float(protein) if protein else None
            fat = float(fat) if fat else None
            carbs = float(carbs) if carbs else None
            calories = float(calories) if calories else None

            filtered_data = search_nutritional_values(self.dataframe, protein, fat, carbs, calories)
            print(filtered_data)

        except ValueError:
            wx.MessageBox('Please enter valid numerical values.', 'Error', wx.OK | wx.ICON_ERROR)

    def on_reset(self, event):
        self.frame.m_textCtrl1.SetValue("")
        self.frame.m_textCtrl2.SetValue("")
        self.frame.m_textCtrl3.SetValue("")
        self.frame.m_textCtrl4.SetValue("")
        self.dataframe = reset_filters(self.dataframe)


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()