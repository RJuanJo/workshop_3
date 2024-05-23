import pandas as pd

df1 = pd.read_csv("data/2015.csv")
df2 = pd.read_csv("data/2016.csv")
df3 = pd.read_csv("data/2017.csv")
df4 = pd.read_csv("data/2018.csv")
df5 = pd.read_csv("data/2019.csv")

def extract_and_combine_data():
    
    df1['Year'] = "2015"
    df2['Year'] = "2016"
    df3['Year'] = "2017"
    df4['Year'] = "2018"
    df5['Year'] = "2019"

    df1.rename(columns={
        'Happiness Rank': 'Happiness_Rank',
        'Happiness Score': 'Happiness_Score',
        'Economy (GDP per Capita)': 'Economy_GDP_per_Capita',
        'Health (Life Expectancy)': 'Health_Life_Expectancy',
        'Trust (Government Corruption)': 'Trust_Government_Corruption',
        'Dystopia Residual': 'Dystopia_Residual'
    }, inplace=True)

    df2.rename(columns={
        'Happiness Rank': 'Happiness_Rank',
        'Happiness Score': 'Happiness_Score',
        'Lower Confidence Interval': 'Lower_Confidence_Interval',
        'Upper Confidence Interval': 'Upper_Confidence_Interval',
        'Economy (GDP per Capita)': 'Economy_GDP_per_Capita',
        'Health (Life Expectancy)': 'Health_Life_Expectancy',
        'Trust (Government Corruption)': 'Trust_Government_Corruption',
        'Dystopia Residual': 'Dystopia_Residual'
    }, inplace=True)

    df3.rename(columns={
        'Happiness.Rank': 'Happiness_Rank',
        'Happiness.Score': 'Happiness_Score',
        'Whisker.high': 'Upper_Confidence_Interval',
        'Whisker.low': 'Lower_Confidence_Interval',
        'Economy..GDP.per.Capita.': 'Economy_GDP_per_Capita',
        'Health..Life.Expectancy.': 'Health_Life_Expectancy',
        'Trust..Government.Corruption.': 'Trust_Government_Corruption',
        'Dystopia.Residual': 'Dystopia_Residual'
    }, inplace=True)

    df4.rename(columns={
        'Overall rank': 'Happiness_Rank',
        'Country or region': 'Country',
        'Score': 'Happiness_Score',
        'GDP per capita': 'Economy_GDP_per_Capita',
        'Social support': 'Family',
        'Healthy life expectancy': 'Health_Life_Expectancy',
        'Freedom to make life choices': 'Freedom',
        'Perceptions of corruption': 'Trust_Government_Corruption'
    }, inplace=True)

    df5.rename(columns={
        'Overall rank': 'Happiness_Rank',
        'Country or region': 'Country',
        'Score': 'Happiness_Score',
        'GDP per capita': 'Economy_GDP_per_Capita',
        'Social support': 'Family',
        'Healthy life expectancy': 'Health_Life_Expectancy',
        'Freedom to make life choices': 'Freedom',
        'Perceptions of corruption': 'Trust_Government_Corruption'
    }, inplace=True)
    dfs = [df1, df2, df3, df4, df5]
    data = pd.concat(dfs, ignore_index=True)

    columns_to_drop = ['Standard Error', 'Dystopia_Residual', 'Lower_Confidence_Interval', 'Upper_Confidence_Interval']

    data = data.drop(columns=columns_to_drop)

    region_countries = {
        'North America': ['Canada', 'United States'],
        
        'Australia and New Zealand': ['New Zealand', 'Australia'],
        
        'Latin America and Caribbean': ['Costa Rica', 'Mexico', 'Brazil', 'Panama', 'Chile', 'Argentina', 'Uruguay', 
            'Colombia', 'Trinidad and Tobago', 'Trinidad & Tobago', 'El Salvador', 'Guatemala', 'Suriname', 'Jamaica', 'Dominican Republic', 
            'Nicaragua', 'Ecuador', 'Bolivia', 'Peru', 'Paraguay', 'Venezuela', 'Honduras', 'Haiti', 'Guatemala', 'Belize', 
            'Cuba', 'Puerto Rico'],
        
        'Europe' : ['Northern Cyprus', 'North Macedonia', 'North Cyprus'],
        'Central and Eastern Europe': ['Czech Republic', 'Slovakia', 'Poland', 'Hungary', 'Slovenia', 'Croatia', 'Bosnia and Herzegovina', 
            'Estonia', 'Lithuania', 'Latvia', 'Romania', 'Bulgaria', 'Serbia', 'Montenegro', 'Macedonia', 'Albania', 'Kosovo', 'Ukraine', 
            'Belarus', 'Moldova', 'Russia'],
        'Western Europe': ['Switzerland', 'Iceland', 'Denmark', 'Norway', 'Finland', 'Netherlands', 'Sweden', 
        'Luxembourg', 'Ireland', 'Belgium', 'United Kingdom', 'Austria', 'Germany', 'France', 'Malta', 'Spain', 
        'Italy', 'Cyprus', 'Portugal', 'Greece'],
        
        'Central Asia' : ['Uzbekistan', 'Kazakhstan', 'Turkmenistan', 'Kyrgyzstan', 'Tajikistan'],
        'South Asia' : ['Bhutan', 'Bangladesh', 'India', 'Nepal', 'Pakistan', 'Sri Lanka'],
        'Eastern Asia': ['Taiwan', 'Japan', 'South Korea', 'Hong Kong', 'Mongolia', 'China'],
        'Southeastern Asia': ['Singapore', 'Thailand', 'Vietnam', 'Malaysia', 'Indonesia', 'Philippines', 'Laos', 'Myanmar', 'Cambodia'],
        'Caucasus and Central Asia': ['Azerbaijan', 'Georgia'],
        'East Asia': ['Taiwan Province of China', 'Hong Kong S.A.R., China'],
        
        'Western Africa' : ['Ghana', 'Ivory Coast', 'Guinea'],
        'Eastern Africa' : ['Djibouti', 'Comoros'],
        'Sub-Saharan Africa': ['Mauritius', 'Nigeria', 'Somaliland region', 'Kenya', 'Zambia', 'Zimbabwe', 'Liberia', 'Namibia', 'Somalia', 'South Africa', 
            'Niger', 'Congo (Kinshasa)', 'Uganda', 'Mozambique', 'Senegal', 'Gabon', 'Tanzania', 
            'Madagascar', 'Central African Republic', 'Chad', 'Ethiopia', 'Mauritania', 'Malawi', 
            'Sierra Leone', 'Congo (Brazzaville)', 'Armenia', 'Botswana', 'Mali', 'Angola', 'Benin', 
            'Mauritania', 'Burkina Faso', 'Rwanda', 'Togo', 'Burundi', 'South Sudan', 'Gambia'],
        'Northern Africa and Middle East' : ['Egypt', 'Sudan'],
        'East Africa' : ['Somaliland Region'],
        'Middle East and Northern Africa': ['Israel', 'Cameroon', 'United Arab Emirates', 'Oman', 'Saudi Arabia', 'Kuwait', 'Bahrain', 'Qatar', 
            'Libya', 'Jordan', 'Lebanon', 'Tunisia', 'Turkey', 'Algeria', 'Morocco', 'Iran', 'Iraq', 
            'Palestinian Territories', 'Yemen', 'Syria', 'Afghanistan'],
        'Southern Africa' : ['Lesotho','Swaziland']
    }
    country_region_mapping = {country: region for region, countries in region_countries.items() for country in countries}

    data['Region'] = data['Country'].map(country_region_mapping)
    data = data.dropna(subset=['Trust_Government_Corruption'])
    return data

