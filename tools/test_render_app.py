import subprocess
import os

with open('archives/Itinerary_Builder_App_Test.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Position at header_after so it renders right at the top of page 1!
sample_box = '''customBoxes:[{
  id: 1711111111111,
  title: "Flight Details & Schedule",
  content: "Please arrive at the airport at least 3 hours prior to departure with valid passport and travel documents.",
  position: "header_after",
  hasTitle: true,
  hasContent: true,
  fontSize: 15,
  padding: "normal",
  theme: "blue",
  flights: [
    {
      id: 1,
      type: "departure",
      airline: "SriLankan Airlines (UL 504)",
      departure: "BKK Bangkok Suvarnabhumi (09:15 AM)",
      arrival: "CMB Colombo Bandaranaike (11:30 AM)",
      info: "Date: 15 Oct 2026 | Baggage: 30kg | Terminal 1"
    },
    {
      id: 2,
      type: "arrival",
      airline: "SriLankan Airlines (UL 505)",
      departure: "CMB Colombo Bandaranaike (18:45 PM)",
      arrival: "BKK Bangkok Suvarnabhumi (23:55 PM)",
      info: "Date: 22 Oct 2026 | Baggage: 30kg | Terminal 1"
    }
  ]
}]'''

test_html = html.replace('customBoxes:[]', sample_box, 1)

with open('archives/Itinerary_Builder_App_Visual_Test.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
out_png = r'C:\Users\User\.gemini\antigravity-ide\brain\e0c95803-0cf0-43ed-8b88-17b065244aff\flight_card_page1.png'

abs_html = os.path.abspath('archives/Itinerary_Builder_App_Visual_Test.html')
file_url = 'file:///' + abs_html.replace('\\', '/')

cmd = [
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--window-size=1400,1200',
    f'--screenshot={out_png}',
    file_url
]

subprocess.run(cmd, capture_output=True, text=True)
print("Saved screenshot to:", out_png)
