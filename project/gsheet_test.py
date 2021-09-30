import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac
import emoji
import re

def strip_emoji(text):
    new_text = re.sub(emoji.get_emoji_regexp(), r"", text)
    return new_text


scopes = ["https://spreadsheets.google.com/feeds"]
json_path = 'C:\\Users\\jack\\business_program\\project\\pbc-recipe.json'

credentials = sac.from_json_keyfile_name(json_path, scopes)
gss_client = gspread.authorize(credentials)
sheet_key = '121u8inOw4UAGNyb70peVAAwgGGiO4K7ZfqZIHvM3cEQ'

gss_sheet = gss_client.open_by_key(sheet_key).sheet1

str = '滷味の人生哲學🔮不如放手更自由★oka'
str = strip_emoji(str)
print(str)
