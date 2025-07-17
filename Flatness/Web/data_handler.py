import pandas as pd
import io
import base64

def parse_csv(contents, sep=';'):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')), sep=sep)
    # Tu można dodać walidację kolumn, typów, usuwanie wartości NULL itd.
    return df