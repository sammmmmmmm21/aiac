import re

def extract_mentions_hashtags(text):
    # Regex: match @ or # followed by word chars, ignore trailing punctuation
    mention_pattern = r'@(\w+)'
    hashtag_pattern = r'#(\w+)'
    mentions = re.findall(mention_pattern, text, re.IGNORECASE)
    hashtags = re.findall(hashtag_pattern, text, re.IGNORECASE)
    # Lowercase and deduplicate
    mentions = [m.lower() for m in mentions]
    hashtags = [h.lower() for h in hashtags]
    return mentions, hashtags

# --- Tests ---
def test_extract():
    cases = [
        # Basic
        ("Hello @alice check #AI and #Python with @Bob", (['alice','bob'], ['ai','python'])),
        # Punctuation
        ("Hi, @Alice! Try #Agri-Tech. @BOB, #Farmers.", (['alice','bob'], ['agri','farmers'])),
        # Multiple tags, mixed case
        ("@JohnDoe and @Jane_Doe #Harvest2024 #Soil_Health", (['johndoe','jane_doe'], ['harvest2024','soil_health'])),
        # Edge: trailing punctuation
        ("Check @user1, @user2. #Tag1! #Tag2?", (['user1','user2'], ['tag1','tag2'])),
        # No tags
        ("No tags here!", ([], [])),
        # Underscores and numbers
        ("@agri_tech #2024season", (['agri_tech'], ['2024season'])),
    ]
    for i, (inp, expected) in enumerate(cases):
        out = extract_mentions_hashtags(inp)
        print(f"Input: {inp}\nOutput: {out}\nExpected: {expected}\n")
        assert out == expected, f"Test {i} failed: got {out}, expected {expected}"
    print("All tests passed.")

if __name__ == "__main__":
    test_extract()