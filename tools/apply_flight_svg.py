import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('archives/Itinerary_Builder_App New.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the helper functions
helpers_code = '''let renderDepIcon=(sz=15,cls="")=>(0,b.jsxs)(`svg`,{width:sz,height:sz,viewBox:`0 0 24 24`,fill:`currentColor`,className:cls,children:[(0,b.jsx)(`rect`,{x:2,y:19,width:20,height:2,rx:1}),(0,b.jsx)(`g`,{transform:`translate(2, 3)`,children:(0,b.jsx)(`path`,{d:`M6.49 3.24L7.03 3.24L13.15 6.13L13.87 6.13L16.76 4.86L18.74 5.05L19.28 5.95L19.1 6.49L17.66 7.75L5.95 11.53L3.24 12.07L1.08 9.01L1.08 8.47L2.7 8.11L4.5 9.73L5.05 9.73L9.19 7.93L5.05 3.96L6.49 3.24Z`})})]});
let renderArrIcon=(sz=15,cls="")=>(0,b.jsxs)(`svg`,{width:sz,height:sz,viewBox:`0 0 24 24`,fill:`currentColor`,className:cls,children:[(0,b.jsx)(`rect`,{x:2,y:19,width:20,height:2,rx:1}),(0,b.jsx)(`g`,{transform:`translate(2, 3)`,children:(0,b.jsx)(`path`,{d:`M8.47 0.9L10.27 1.8L13.33 8.11L17.48 9.73L18.2 10.81L18.02 11.71L17.3 12.07L15.5 12.07L3.24 7.03L1.8 6.13L2.16 1.98L2.52 1.98L3.78 2.52L4.14 4.86L4.5 5.41L9.01 6.85L9.19 6.31L8.29 1.08L8.47 0.9Z`})})]});
let renderTransitIcon=(sz=15,cls="")=>(0,b.jsx)(`svg`,{width:sz,height:sz,viewBox:`0 0 24 24`,fill:`currentColor`,className:cls,children:(0,b.jsx)(`path`,{d:`M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z`})});
'''

# 1. Insert helper icons before boxThemes
target_themes = "let boxThemes={"
assert target_themes in content, "Could not find let boxThemes={"
new_content = content.replace(target_themes, helpers_code + target_themes, 1)

# 2. Replace toolbar quick add buttons
# Search:
# children:[`🛫`, `+ Dep`]
# children:[`🛬`, `+ Arr`]
target_tb_dep = "children:[`🛫`, `+ Dep`]"
replace_tb_dep = "children:[renderDepIcon(13, `shrink-0`), `+ Dep`]"
assert target_tb_dep in new_content, "Could not find target_tb_dep"
new_content = new_content.replace(target_tb_dep, replace_tb_dep, 1)

target_tb_arr = "children:[`🛬`, `+ Arr`]"
replace_tb_arr = "children:[renderArrIcon(13, `shrink-0`), `+ Arr`]"
assert target_tb_arr in new_content, "Could not find target_tb_arr"
new_content = new_content.replace(target_tb_arr, replace_tb_arr, 1)

# 3. Replace flight type badge icon:
# Target: (0,b.jsx)(`span`,{className:`text-sm select-none`,children:fl.type===`arrival`?`🛬`:fl.type===`transit`?`✈️`:`🛫`})
target_badge = "(0,b.jsx)(`span`,{className:`text-sm select-none`,children:fl.type===`arrival`?`🛬`:fl.type===`transit`?`✈️`:`🛫`})"
replace_badge = "(0,b.jsx)(`span`,{className:`select-none shrink-0 flex items-center justify-center`,children:fl.type===`arrival`?renderArrIcon(15):fl.type===`transit`?renderTransitIcon(15):renderDepIcon(15)})"
assert target_badge in new_content, "Could not find target_badge"
new_content = new_content.replace(target_badge, replace_badge, 1)

# 4. Replace Departure & Arrival row icons:
# Departure row:
# (0,b.jsx)(`span`,{className:`text-lg select-none shrink-0`,children:`🛫`})
# Arrival row:
# (0,b.jsx)(`span`,{className:`text-lg select-none shrink-0`,children:`🛬`})
target_dep_row = "(0,b.jsx)(`span`,{className:`text-lg select-none shrink-0`,children:`🛫`})"
replace_dep_row = "(0,b.jsx)(`span`,{className:`p-1.5 bg-amber-100/80 text-amber-800 rounded-md shrink-0 flex items-center justify-center shadow-xs`,children:renderDepIcon(18)})"
assert target_dep_row in new_content, "Could not find target_dep_row"
new_content = new_content.replace(target_dep_row, replace_dep_row, 1)

target_arr_row = "(0,b.jsx)(`span`,{className:`text-lg select-none shrink-0`,children:`🛬`})"
replace_arr_row = "(0,b.jsx)(`span`,{className:`p-1.5 bg-blue-100/80 text-blue-800 rounded-md shrink-0 flex items-center justify-center shadow-xs`,children:renderArrIcon(18)})"
assert target_arr_row in new_content, "Could not find target_arr_row"
new_content = new_content.replace(target_arr_row, replace_arr_row, 1)

# 5. Replace bottom Add Flight buttons:
# children:[`🛫`, `Add Departure Flight`]
# children:[`🛬`, `Add Arrival Flight`]
target_bot_dep = "children:[`🛫`, `Add Departure Flight`]"
replace_bot_dep = "children:[renderDepIcon(14, `shrink-0`), `Add Departure Flight`]"
assert target_bot_dep in new_content, "Could not find target_bot_dep"
new_content = new_content.replace(target_bot_dep, replace_bot_dep, 1)

target_bot_arr = "children:[`🛬`, `Add Arrival Flight`]"
replace_bot_arr = "children:[renderArrIcon(14, `shrink-0`), `Add Arrival Flight`]"
assert target_bot_arr in new_content, "Could not find target_bot_arr"
new_content = new_content.replace(target_bot_arr, replace_bot_arr, 1)

# 6. Sidebar quick add button:
target_side_btn = "children:[(0,b.jsx)(`span`,{className:`text-sm`,children:`✈️`}),`Add Flight Schedule Box`]"
replace_side_btn = "children:[(0,b.jsx)(`span`,{className:`text-sm shrink-0 flex items-center`,children:renderDepIcon(15)}),`Add Flight Schedule Box`]"
if target_side_btn in new_content:
    new_content = new_content.replace(target_side_btn, replace_side_btn, 1)
    print("Sidebar button updated with SVG!")

# Save to a temporary test file first
with open('archives/Itinerary_Builder_App_Test.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Saved archives/Itinerary_Builder_App_Test.html successfully!")
