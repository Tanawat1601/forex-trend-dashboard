Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import streamlit as st
... import pandas as pd
... from datetime import datetime
... 
... # สร้างข้อมูลตัวอย่าง
... data = {
...     'Symbol': ['EURUSD', 'USDJPY', 'GBPUSD', 'USDCHF', 'GBPJPY', 'CHFJPY'],
...     'EMA Trend': ['Uptrend', 'Uptrend', 'Downtrend', 'Uptrend', 'Downtrend', 'Sideway'],
...     'RSI': [65, 70, 45, 68, 39, 52],
...     'MACD': ['Bullish', 'Bullish', 'Bearish', 'Bullish', 'Bearish', 'Neutral'],
...     'Overall Trend': ['↑ Strong Up', '↑ Strong Up', '↓ Weak Down', '↑ Moderate Up', '↓ Strong Down', '→ Sideway']
... }
... df = pd.DataFrame(data)
... df['Last Checked'] = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
... 
... # UI
... st.set_page_config(page_title="Forex Trend Overview", layout="wide")
... st.title("📈 Forex Trend Dashboard (USD / CHF / GBP)")
... st.markdown(f"**Updated:** {df['Last Checked'][0]}")
... st.dataframe(df.drop(columns=["Last Checked"]), use_container_width=True)
... 
... st.markdown("---")
... st.subheader("📢 แนวทางการตีความ:")
... st.markdown("""
... - 🟢 **↑ Strong Up**: แนวโน้มขาขึ้นแข็งแรง เหมาะสำหรับหาโอกาส Buy  
... - 🔴 **↓ Strong Down**: แนวโน้มขาลงชัดเจน ระวังการ Buy สวนเทรนด์  
... - ⚠️ **→ Sideway**: ยังไม่ชัดเจน ควรรอดูเพิ่มเติมก่อนเข้าออเดอร์  
