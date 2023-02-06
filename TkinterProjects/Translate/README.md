# Google Translator App 

Packages 
- TKinter
- Request

Translate Command 
```python
def translate():
    source_text = text_entry.get()
    target_language = select_lang.get()
    response = requests.get(
        f"https://translate.google.com/translate_a/single?client=gtx&sl=auto&tl={target_language}&dt=t&q={source_text}")
    result = response.json()[0][0][0]
    result_entry.config(text=result)
```
