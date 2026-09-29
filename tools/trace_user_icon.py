from PIL import Image

im = Image.open(r'C:\Users\User\.gemini\antigravity-ide\brain\e0c95803-0cf0-43ed-8b88-17b065244aff\.user_uploaded\media_1790682535652.png').convert('L')

def extract_boundary(box):
    grid = {}
    for y in range(box[1], box[3]+1):
        for x in range(box[0], box[2]+1):
            grid[(x, y)] = 1 if im.getpixel((x, y)) < 128 else 0
                
    start = None
    for y in range(box[1], box[3]+1):
        for x in range(box[0], box[2]+1):
            if grid.get((x, y)) == 1:
                start = (x, y)
                break
        if start:
            break
            
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    
    contour = [start]
    curr = start
    curr_back = 4
    
    while len(contour) < 2000:
        found = False
        start_dir = (curr_back + 1) % 8
        for i in range(8):
            d = (start_dir + i) % 8
            nx, ny = curr[0] + dx[d], curr[1] + dy[d]
            if grid.get((nx, ny), 0) == 1:
                curr = (nx, ny)
                contour.append(curr)
                curr_back = (d + 4) % 8
                found = True
                break
        if not found or curr == start:
            break
    return contour

def rdp(points, epsilon):
    if len(points) < 3:
        return points
    def point_line_dist(pt, start, end):
        if start == end:
            return ((pt[0]-start[0])**2 + (pt[1]-start[1])**2)**0.5
        n = abs((end[1]-start[1])*pt[0] - (end[0]-start[0])*pt[1] + end[0]*start[1] - end[1]*start[0])
        d = ((end[1]-start[1])**2 + (end[0]-start[0])**2)**0.5
        return n / d
    dmax = 0.0
    index = 0
    for i in range(1, len(points) - 1):
        d = point_line_dist(points[i], points[0], points[-1])
        if d > dmax:
            index = i
            dmax = d
    if dmax > epsilon:
        rec1 = rdp(points[:index+1], epsilon)
        rec2 = rdp(points[index:], epsilon)
        return rec1[:-1] + rec2
    else:
        return [points[0], points[-1]]

arr_pts = rdp(extract_boundary((20, 70, 125, 140)), 1.0)
dep_pts = rdp(extract_boundary((160, 80, 275, 140)), 1.0)

# Runway line in image is Y: 148..150. For left: X: 16..127. For right: X: 161..272.
# Let's normalize each half (plane + runway) to a 100x100 box or 24x24 box!
# Left bounds: X: 16..127 (width 111), Y: 75..151 (height 76)
# Right bounds: X: 161..272 (width 111), Y: 75..151 (height 76)
# Center them in a 120 x 100 box, or scale to 24 x 24!

def to_path(pts, offset_x, offset_y, scale):
    d = []
    for i, (x, y) in enumerate(pts):
        sx = round((x - offset_x) * scale, 2)
        sy = round((y - offset_y) * scale, 2)
        cmd = "M" if i == 0 else "L"
        d.append(f"{cmd}{sx} {sy}")
    d.append("Z")
    return "".join(d)

# Let's target a 24x24 viewBox:
# Scale factor: 20 / 111 = ~0.18
# Offset: left: x=16, y=70; right: x=161, y=70
scale_24 = 20.0 / 111.0
arr_plane_d = to_path(arr_pts, 16, 70, scale_24)
dep_plane_d = to_path(dep_pts, 161, 70, scale_24)

# Line in 24x24:
# Runway Y in image is 149. (149 - 70) * scale_24 = 79 * 0.18 = 14.22 -> let's put runway at y=21
# Let's inspect the exact dimensions and normalize properly.

print("Arrival Plane Path (24x24 approx):")
print(arr_plane_d)
print("\nDeparture Plane Path (24x24 approx):")
print(dep_plane_d)
