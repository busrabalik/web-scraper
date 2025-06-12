
import json                      
from datetime import datetime    
from contests_scr import get_all_data 


def save_data_with_date():
 try: 
    
    data = get_all_data()
    

    date_str = datetime.now().strftime("%Y-%m-%d")
    
    
    file_name = f"data_{date_str}.json"
    
    
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Data saved as {file_name}")

 except Exception as e:
    print("❌ Hata oluştu:", e)


if __name__ == "__main__":
    save_data_with_date()
