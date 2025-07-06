import pandas as pd
from ydata_profiling import ProfileReport

# ...existing code...
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("data/lays_reviews_cleaned.csv")
print(df)
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("data/lays_reviews_cleaned.csv")
print(df)

profile = ProfileReport(df, title="Lays Reviews Cleaned Report")
profile.to_file("lays_reviews_cleaned_report.html")