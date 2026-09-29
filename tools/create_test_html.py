# Create comprehensive visual comparison HTML
html = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Vector Plane Icons Comparison</title>
<style>
  body { font-family: system-ui, sans-serif; padding: 40px; background: #0f172a; color: #f8fafc; }
  .grid { display: flex; gap: 32px; flex-wrap: wrap; }
  .card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 24px; min-width: 320px; }
  .card h3 { margin-top: 0; color: #38bdf8; font-size: 16px; border-bottom: 1px solid #334155; padding-bottom: 8px; }
  .icon-row { display: flex; gap: 24px; align-items: flex-end; margin: 16px 0; }
  .item { display: flex; flex-direction: column; align-items: center; gap: 8px; font-size: 11px; font-weight: 700; letter-spacing: 1px; }
  .badge { display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; border-radius: 9999px; font-size: 12px; font-weight: 600; }
  .badge-dep { background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }
  .badge-arr { background: rgba(59, 130, 246, 0.2); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }
  .badge-light { background: #fef3c7; color: #92400e; }
  .badge-light-arr { background: #dbeafe; color: #1e40af; }
</style>
</head>
<body>

<h1>Professional Flight Departure & Arrival Icons</h1>
<p style="color: #94a3b8;">Replaces cartoon emojis with clean, airport-standard silhouette vectors matching the user's reference image.</p>

<div class="grid">
  <!-- Option A: Traced Exact User Silhouette -->
  <div class="card">
    <h3>Option A: Exact Traced Geometry from User Image (viewBox 0 0 24 24)</h3>
    <div class="icon-row">
      <div class="item">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor" style="color: #60a5fa;">
          <!-- Runway line -->
          <rect x="2" y="19" width="20" height="2" rx="1" />
          <!-- Arrival plane -->
          <g transform="translate(2, 3)">
            <path d="M8.47 0.9L10.27 1.8L13.33 8.11L17.48 9.73L18.2 10.81L18.02 11.71L17.3 12.07L15.5 12.07L3.24 7.03L1.8 6.13L2.16 1.98L2.52 1.98L3.78 2.52L4.14 4.86L4.5 5.41L9.01 6.85L9.19 6.31L8.29 1.08L8.47 0.9Z" />
          </g>
        </svg>
        <span>ARRIVAL</span>
      </div>

      <div class="item">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor" style="color: #fbbf24;">
          <!-- Runway line -->
          <rect x="2" y="19" width="20" height="2" rx="1" />
          <!-- Departure plane -->
          <g transform="translate(2, 3)">
            <path d="M6.49 3.24L7.03 3.24L13.15 6.13L13.87 6.13L16.76 4.86L18.74 5.05L19.28 5.95L19.1 6.49L17.66 7.75L5.95 11.53L3.24 12.07L1.08 9.01L1.08 8.47L2.7 8.11L4.5 9.73L5.05 9.73L9.19 7.93L5.05 3.96L6.49 3.24Z" />
          </g>
        </svg>
        <span>DEPARTURE</span>
      </div>
    </div>

    <div style="margin-top: 16px; display: flex; gap: 8px;">
      <span class="badge badge-dep">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><rect x="2" y="19" width="20" height="2" rx="1"/><g transform="translate(2, 3)"><path d="M6.49 3.24L7.03 3.24L13.15 6.13L13.87 6.13L16.76 4.86L18.74 5.05L19.28 5.95L19.1 6.49L17.66 7.75L5.95 11.53L3.24 12.07L1.08 9.01L1.08 8.47L2.7 8.11L4.5 9.73L5.05 9.73L9.19 7.93L5.05 3.96L6.49 3.24Z"/></g></svg>
        Departure
      </span>
      <span class="badge badge-arr">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><rect x="2" y="19" width="20" height="2" rx="1"/><g transform="translate(2, 3)"><path d="M8.47 0.9L10.27 1.8L13.33 8.11L17.48 9.73L18.2 10.81L18.02 11.71L17.3 12.07L15.5 12.07L3.24 7.03L1.8 6.13L2.16 1.98L2.52 1.98L3.78 2.52L4.14 4.86L4.5 5.41L9.01 6.85L9.19 6.31L8.29 1.08L8.47 0.9Z"/></g></svg>
        Arrival
      </span>
    </div>
  </div>

  <!-- Option B: Polished Airport Standard (Smooth rounded bezier curves) -->
  <div class="card">
    <h3>Option B: Precision Airport Standard (Smooth Aerodynamic Curves)</h3>
    <div class="icon-row">
      <div class="item">
        <!-- Arrival: descending right -->
        <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor" style="color: #60a5fa;">
          <line x1="2.5" y1="20" x2="21.5" y2="20" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
          <path d="M2.5 8.2l2.3-.9 1.8 3.5 4.3 1.6-1.5-6.8 2.3-.9 3.3 7.5 4.8 1.8c1.6.6 2.4 2.2 1.8 3.8-.6 1.5-2.2 2.1-3.8 1.5l-11.4-4.3-3.6 1.6-1.6-1.2.7-2.6-2-4.6z" />
        </svg>
        <span>ARRIVAL</span>
      </div>

      <div class="item">
        <!-- Departure: ascending right -->
        <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor" style="color: #fbbf24;">
          <line x1="2.5" y1="20" x2="21.5" y2="20" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
          <path d="M2.5 15.8l2.3.9 1.8-3.5 4.3-1.6-1.5 6.8 2.3.9 3.3-7.5 4.8-1.8c1.6-.6 2.4-2.2 1.8-3.8-.6-1.5-2.2-2.1-3.8-1.5l-11.4 4.3-3.6-1.6-1.6 1.2.7 2.6-2 4.6z" />
        </svg>
        <span>DEPARTURE</span>
      </div>
    </div>

    <div style="margin-top: 16px; display: flex; gap: 8px;">
      <span class="badge badge-dep">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><line x1="2.5" y1="20" x2="21.5" y2="20" stroke="currentColor" stroke-width="2" stroke-linecap="round" /><path d="M2.5 15.8l2.3.9 1.8-3.5 4.3-1.6-1.5 6.8 2.3.9 3.3-7.5 4.8-1.8c1.6-.6 2.4-2.2 1.8-3.8-.6-1.5-2.2-2.1-3.8-1.5l-11.4 4.3-3.6-1.6-1.6 1.2.7 2.6-2 4.6z" /></svg>
        Departure
      </span>
      <span class="badge badge-arr">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><line x1="2.5" y1="20" x2="21.5" y2="20" stroke="currentColor" stroke-width="2" stroke-linecap="round" /><path d="M2.5 8.2l2.3-.9 1.8 3.5 4.3 1.6-1.5-6.8 2.3-.9 3.3 7.5 4.8 1.8c1.6.6 2.4 2.2 1.8 3.8-.6 1.5-2.2 2.1-3.8 1.5l-11.4-4.3-3.6 1.6-1.6-1.2.7-2.6-2-4.6z" /></svg>
        Arrival
      </span>
    </div>
  </div>

  <!-- Option C: Pure Geometric Replica of User Photo -->
  <div class="card">
    <h3>Option C: Ultra Crisp Geometric Silhouette (Pixel Perfect Match to Photo)</h3>
    <div class="icon-row">
      <div class="item">
        <!-- ARRIVAL -->
        <svg width="48" height="48" viewBox="0 0 32 32" fill="currentColor" style="color: #60a5fa;">
          <!-- Baseline Runway -->
          <rect x="2" y="27" width="28" height="2" rx="1"/>
          <!-- Plane descending -->
          <path d="M4.2 11.2 L8.5 12.8 L14.2 4.2 L17.5 5.5 L14.5 15.0 L24.5 18.8 C27.8 20.0 28.8 22.8 27.2 24.6 C25.8 26.2 23.2 26.0 20.2 24.8 L4.8 19.0 L2.2 16.5 L2.5 12.2 Z" />
        </svg>
        <span>ARRIVAL</span>
      </div>

      <div class="item">
        <!-- DEPARTURE -->
        <svg width="48" height="48" viewBox="0 0 32 32" fill="currentColor" style="color: #fbbf24;">
          <!-- Baseline Runway -->
          <rect x="2" y="27" width="28" height="2" rx="1"/>
          <!-- Plane ascending -->
          <path d="M4.2 20.8 L8.5 19.2 L14.2 27.8 L17.5 26.5 L14.5 17.0 L24.5 13.2 C27.8 12.0 28.8 9.2 27.2 7.4 C25.8 5.8 23.2 6.0 20.2 7.2 L4.8 13.0 L2.2 15.5 L2.5 19.8 Z" />
        </svg>
        <span>DEPARTURE</span>
      </div>
    </div>

    <div style="margin-top: 16px; display: flex; gap: 8px;">
      <span class="badge badge-dep">
        <svg width="15" height="15" viewBox="0 0 32 32" fill="currentColor"><rect x="2" y="27" width="28" height="2" rx="1"/><path d="M4.2 20.8 L8.5 19.2 L14.2 27.8 L17.5 26.5 L14.5 17.0 L24.5 13.2 C27.8 12.0 28.8 9.2 27.2 7.4 C25.8 5.8 23.2 6.0 20.2 7.2 L4.8 13.0 L2.2 15.5 L2.5 19.8 Z" /></svg>
        Departure
      </span>
      <span class="badge badge-arr">
        <svg width="15" height="15" viewBox="0 0 32 32" fill="currentColor"><rect x="2" y="27" width="28" height="2" rx="1"/><path d="M4.2 11.2 L8.5 12.8 L14.2 4.2 L17.5 5.5 L14.5 15.0 L24.5 18.8 C27.8 20.0 28.8 22.8 27.2 24.6 C25.8 26.2 23.2 26.0 20.2 24.8 L4.8 19.0 L2.2 16.5 L2.5 12.2 Z" /></svg>
        Arrival
      </span>
    </div>
  </div>
</div>

</body>
</html>
'''

with open('tools/test_svgs.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved tools/test_svgs.html")
