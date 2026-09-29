import re

with open('archives/Itinerary_Builder_App New.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Verify that the target segments exist in content
print("Has renderBoxesForSlot:", "renderBoxesForSlot" in content)
print("Has fl.type==='arrival'?:", "fl.type===`arrival`?`🛬`" in content or "fl.type===`arrival`" in content)

# Check exact string matches
search1 = "fl.type===`arrival`?`🛬`:fl.type===`transit`?`✈️`:`🛫`"
print("Search 1 found:", search1 in content)

search_dep_row = "(0,b.jsx)(`span`,{className:`text-lg select-none shrink-0`,children:`🛫`})"
print("Search dep row found:", search_dep_row in content)

search_arr_row = "(0,b.jsx)(`span`,{className:`text-lg select-none shrink-0`,children:`🛬`})"
print("Search arr row found:", search_arr_row in content)

search_tb_dep = "children:[`🛫`, `+ Dep`]"
print("Search tb dep found:", search_tb_dep in content)

search_tb_arr = "children:[`🛬`, `+ Arr`]"
print("Search tb arr found:", search_tb_arr in content)

search_bot_dep = "children:[`🛫`, `Add Departure Flight`]"
print("Search bot dep found:", search_bot_dep in content)

search_bot_arr = "children:[`🛬`, `Add Arrival Flight`]"
print("Search bot arr found:", search_bot_arr in content)
