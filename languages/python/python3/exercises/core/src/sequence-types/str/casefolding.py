'''
1.1 Easy: Unicode Normalization & Casefolding

     * Goal: Implement normalize_and_casefold(s: str) -> str.
     * Description: Normalize a Unicode string using canonical decomposition/composition (NFC) and perform
       caseless matching transformation (casefold()).
     * Key Takeaway: Python strings are sequences of Unicode code points. Direct string equality == fails
       for canonical equivalents (e.g., u"\u00e9" vs u"e\u0301") unless normalized with
       unicodedata.normalize. casefold() provides aggressive caseless matching across non-ASCII scripts
       (e.g., German "  -> "ss").
     * Expected Behavior:
          + normalize_and_casefold("Straße") -> "strasse"
          + normalize_and_casefold("e\u0301") == normalize_and_casefold("\u00e9") -> True
'''
import unicodedata

def normalize_and_casefold(s: str) -> str:
    return unicodedata.normalize('NFC', s).casefold()
