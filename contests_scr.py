import requests
from bs4 import BeautifulSoup


signs = [
    "Koç", "Boğa", "İkizler", "Yengeç", "Aslan", "Başak",
    "Terazi", "Akrep", "Yay", "Oğlak", "Kova", "Balık"
]

sources = {
    "Hande Kazanova": {
        "url": "https://www.handekazanova.com/31-mart-06-nisan-2025-haftalik-burc-yorumlari/",
        "headers": {
            "User-Agent": "Mozilla/5.0 ...",
            "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Referer": "https://www.handekazanova.com/",
            "Connection": "keep-alive"
        }
    },
    "Indigo": {
        "url": "https://indigodergisi.com/2025/03/astroloji-31-mart-6-nisan-haftalik-burc-yorumlari/",
        "headers": {
            "User-Agent": "Mozilla/5.0 ...",
            "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Referer": "https://indigodergisi.com/",
            "Connection": "keep-alive"
        }
    },
    "Onedio": {
        "url": "https://onedio.com/haber/31-mart-6-nisan-2025-haftalik-burc-yorumlari-1283181",
        "headers": {
            "User-Agent": "Mozilla/5.0 ...",
            "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Referer": "https://tpc.googlesyndication.com/",
            "Connection": "keep-alive"
        }
    }
}

def o_scrap(soup):
    current_sign = None
    comments = {sign: "" for sign in signs}
    elements = soup.find_all(['h2', 'h3', 'p', 'strong'])
    for el in elements:
        text = el.get_text(strip=True)
        for sign in signs:
            if sign in text:
                current_sign = sign
                break
        if current_sign and text not in signs:
            comments[current_sign] += text + " "
    return comments

def i_scrap(soup):
    results = {sign: "" for sign in signs}
    for h3 in soup.find_all("h3"):
        title = h3.get_text(strip=True)
        for sign in signs:
            if sign in title:
                content = []
                for sibling in h3.find_next_siblings():
                    if sibling.name == "h3":
                        break
                    if sibling.name == "p":
                        content.append(sibling.get_text(strip=True))
                results[sign] = " ".join(content)
                break
    return results

def k_scrap(soup):
    results = {sign: "" for sign in signs}
    all_text = soup.get_text(" ", strip=True)
    for i in range(len(signs)):
        current = signs[i]
        next_sign = signs[i + 1] if i + 1 < len(signs) else None
        start = all_text.find(current)
        end = all_text.find(next_sign) if next_sign else None
        if start != -1:
            results[current] = all_text[start:end].strip()
    return results

def get_all_data():
    final_data = {sign: {} for sign in signs}
    for source_name, info in sources.items():
        response = requests.get(info["url"], headers=info["headers"])
        soup = BeautifulSoup(response.text, "html.parser")
        if source_name == "Hande Kazanova":
            parsed = k_scrap(soup)
        elif source_name == "Indigo":
            parsed = i_scrap(soup)
        elif source_name == "Onedio":
            parsed = o_scrap(soup)
        for sign in signs:
            final_data[sign][source_name] = parsed.get(sign, "")
    return final_data

