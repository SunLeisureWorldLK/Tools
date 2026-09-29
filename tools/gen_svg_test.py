svg_tests_html = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Flight SVG Comparison</title>
<style>
  body { font-family: system-ui, -apple-system, sans-serif; padding: 40px; background: #f8fafc; }
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; }
  .card { background: white; padding: 24px; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
  .title { font-weight: bold; margin-bottom: 16px; color: #0f172a; font-size: 16px; }
  .row { display: flex; gap: 32px; align-items: flex-end; }
  .icon-box { display: flex; flex-direction: column; align-items: center; gap: 8px; font-size: 12px; font-weight: 700; letter-spacing: 0.05em; color: #334155; }
  .sample-badge { display: inline-flex; align-items: center; gap: 8px; padding: 6px 14px; border-radius: 9999px; font-size: 13px; font-weight: 700; margin-top: 16px; }
  .badge-dep { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }
  .badge-arr { background: #dbeafe; color: #1e40af; border: 1px solid #bfdbfe; }
</style>
</head>
<body>

<h1>Professional Flight Departure & Arrival Icons</h1>

<div class="grid">
  <!-- Design 1: Exact Airport Signage Silhouette (Matching User Reference) -->
  <div class="card">
    <div class="title">Design 1: Airport Runway Vector (Matches User Image Exactly)</div>
    <div class="row">
      <div class="icon-box">
        <!-- ARRIVAL -->
        <svg width="40" height="40" viewBox="0 0 24 24" fill="currentColor">
          <!-- Runway Line -->
          <path d="M2.5 19.5h19c.4 0 .7.3.7.7s-.3.8-.7.8h-19c-.4 0-.7-.4-.7-.8s.3-.7.7-.7z" />
          <!-- Airplane Descending (Pitch down 25 deg) -->
          <g transform="translate(12, 11) rotate(22) translate(-12, -11)">
            <path d="M4 11.5l3-3.5 6.5 1 4.5-5.5c.6-.7 1.5-.7 2 0 .4.5.3 1.2-.2 1.8l-3.5 5.5 4 .6 1.8-1.4c.4-.3.9-.3 1.2 0 .3.4.3.9 0 1.3l-1.5 2.2c-.3.4-.8.5-1.2.3l-5-.8-6.5 4.5c-.3.2-.7.3-1 .2l-3-1.5c-.5-.3-.7-.9-.4-1.4.1-.2.3-.3.5-.4l2-.9-3-.9z"/>
          </g>
        </svg>
        <span>ARRIVAL</span>
      </div>

      <div class="icon-box">
        <!-- DEPARTURE -->
        <svg width="40" height="40" viewBox="0 0 24 24" fill="currentColor">
          <!-- Runway Line -->
          <path d="M2.5 19.5h19c.4 0 .7.3.7.7s-.3.8-.7.8h-19c-.4 0-.7-.4-.7-.8s.3-.7.7-.7z" />
          <!-- Airplane Ascending (Pitch up 22 deg) -->
          <g transform="translate(12, 10) rotate(-22) translate(-12, -10)">
            <path d="M4 11.5l3-3.5 6.5 1 4.5-5.5c.6-.7 1.5-.7 2 0 .4.5.3 1.2-.2 1.8l-3.5 5.5 4 .6 1.8-1.4c.4-.3.9-.3 1.2 0 .3.4.3.9 0 1.3l-1.5 2.2c-.3.4-.8.5-1.2.3l-5-.8-6.5 4.5c-.3.2-.7.3-1 .2l-3-1.5c-.5-.3-.7-.9-.4-1.4.1-.2.3-.3.5-.4l2-.9-3-.9z"/>
          </g>
        </svg>
        <span>DEPARTURE</span>
      </div>
    </div>

    <div>
      <div class="sample-badge badge-dep">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M2.5 20h19c.4 0 .7.3.7.7s-.3.8-.7.8h-19c-.4 0-.7-.4-.7-.8s.3-.7.7-.7z"/><g transform="translate(12, 9) rotate(-22) translate(-12, -9)"><path d="M4 11.5l3-3.5 6.5 1 4.5-5.5c.6-.7 1.5-.7 2 0 .4.5.3 1.2-.2 1.8l-3.5 5.5 4 .6 1.8-1.4c.4-.3.9-.3 1.2 0 .3.4.3.9 0 1.3l-1.5 2.2c-.3.4-.8.5-1.2.3l-5-.8-6.5 4.5c-.3.2-.7.3-1 .2l-3-1.5c-.5-.3-.7-.9-.4-1.4.1-.2.3-.3.5-.4l2-.9-3-.9z"/></g></svg>
        Departure Flight
      </div>
      <div class="sample-badge badge-arr">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M2.5 20h19c.4 0 .7.3.7.7s-.3.8-.7.8h-19c-.4 0-.7-.4-.7-.8s.3-.7.7-.7z"/><g transform="translate(12, 10) rotate(22) translate(-12, -10)"><path d="M4 11.5l3-3.5 6.5 1 4.5-5.5c.6-.7 1.5-.7 2 0 .4.5.3 1.2-.2 1.8l-3.5 5.5 4 .6 1.8-1.4c.4-.3.9-.3 1.2 0 .3.4.3.9 0 1.3l-1.5 2.2c-.3.4-.8.5-1.2.3l-5-.8-6.5 4.5c-.3.2-.7.3-1 .2l-3-1.5c-.5-.3-.7-.9-.4-1.4.1-.2.3-.3.5-.4l2-.9-3-.9z"/></g></svg>
        Arrival Flight
      </div>
    </div>
  </div>

  <!-- Design 2: High-Detail Modern Jet with Rounded Nose -->
  <div class="card">
    <div class="title">Design 2: Modern Jet Silhouette with Runway</div>
    <div class="row">
      <div class="icon-box">
        <!-- ARRIVAL -->
        <svg width="40" height="40" viewBox="0 0 32 32" fill="currentColor">
          <!-- Runway -->
          <rect x="2" y="26" width="28" height="2" rx="1" />
          <!-- Jet descending -->
          <path d="M5.5 14.8c-.4.2-.6.7-.4 1.1l1.5 3.2 4.2-1.8-2.1-4.8 2.2-.9 4.3 4 4.5-1.9-1.3-6.8 2.3-1 2.8 7.3 3.6-1.5c1.8-.8 3.5-.1 4.1 1.4.6 1.4-.2 3-2 3.8l-19.3 8.2c-.5.2-1.1 0-1.3-.5l-1.8-3.9 2-4.8 1.4-1.8z" />
        </svg>
        <span>ARRIVAL</span>
      </div>

      <div class="icon-box">
        <!-- DEPARTURE -->
        <svg width="40" height="40" viewBox="0 0 32 32" fill="currentColor">
          <!-- Runway -->
          <rect x="2" y="26" width="28" height="2" rx="1" />
          <!-- Jet ascending -->
          <path d="M5.5 17.2c-.4-.2-.6-.7-.4-1.1l1.5-3.2 4.2 1.8-2.1 4.8 2.2.9 4.3-4 4.5 1.9-1.3 6.8 2.3 1 2.8-7.3 3.6 1.5c1.8.8 3.5.1 4.1-1.4.6-1.4-.2-3-2-3.8L9.5 5.2c-.5-.2-1.1 0-1.3.5l-1.8 3.9 2 4.8 1.4 1.8z" />
        </svg>
        <span>DEPARTURE</span>
      </div>
    </div>

    <div>
      <div class="sample-badge badge-dep">
        <svg width="18" height="18" viewBox="0 0 32 32" fill="currentColor"><rect x="2" y="26" width="28" height="2" rx="1"/><path d="M5.5 17.2c-.4-.2-.6-.7-.4-1.1l1.5-3.2 4.2 1.8-2.1 4.8 2.2.9 4.3-4 4.5 1.9-1.3 6.8 2.3 1 2.8-7.3 3.6 1.5c1.8.8 3.5.1 4.1-1.4.6-1.4-.2-3-2-3.8L9.5 5.2c-.5-.2-1.1 0-1.3.5l-1.8 3.9 2 4.8 1.4 1.8z"/></svg>
        Departure Flight
      </div>
      <div class="sample-badge badge-arr">
        <svg width="18" height="18" viewBox="0 0 32 32" fill="currentColor"><rect x="2" y="26" width="28" height="2" rx="1"/><path d="M5.5 14.8c-.4.2-.6.7-.4 1.1l1.5 3.2 4.2-1.8-2.1-4.8 2.2-.9 4.3 4 4.5-1.9-1.3-6.8 2.3-1 2.8 7.3 3.6-1.5c1.8-.8 3.5-.1 4.1 1.4.6 1.4-.2 3-2 3.8l-19.3 8.2c-.5.2-1.1 0-1.3-.5l-1.8-3.9 2-4.8 1.4-1.8z"/></svg>
        Arrival Flight
      </div>
    </div>
  </div>

  <!-- Design 3: Direct User Sketch Vector (Identical Silhouette) -->
  <div class="card">
    <div class="title">Design 3: Direct Match to User Photo</div>
    <div class="row">
      <div class="icon-box">
        <!-- ARRIVAL: nose down to bottom-right, tail top-left -->
        <svg width="44" height="44" viewBox="0 0 48 48" fill="none">
          <line x1="4" y1="40" x2="44" y2="40" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" />
          <path d="M6 21 L12 23 L18 17 L20.5 18 L18 25 L32 30 C35.5 31.2 37.5 33.5 36.5 35.5 C35.5 37.5 32.5 38 29 36.8 L15 31.8 L9 35.5 L6.5 34.5 L9.5 29.5 L6 27 Z" fill="currentColor" />
        </svg>
        <span>ARRIVAL</span>
      </div>

      <div class="icon-box">
        <!-- DEPARTURE: nose up to top-right, tail bottom-left -->
        <svg width="44" height="44" viewBox="0 0 48 48" fill="none">
          <line x1="4" y1="40" x2="44" y2="40" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" />
          <path d="M6 27 L12 25 L18 31 L20.5 30 L18 23 L32 18 C35.5 16.8 37.5 14.5 36.5 12.5 C35.5 10.5 32.5 10 29 11.2 L15 16.2 L9 12.5 L6.5 13.5 L9.5 18.5 L6 21 Z" fill="currentColor" />
        </svg>
        <span>DEPARTURE</span>
      </div>
    </div>

    <div>
      <div class="sample-badge badge-dep">
        <svg width="18" height="18" viewBox="0 0 48 48" fill="none"><line x1="4" y1="40" x2="44" y2="40" stroke="currentColor" stroke-width="3" stroke-linecap="round" /><path d="M6 27 L12 25 L18 31 L20.5 30 L18 23 L32 18 C35.5 16.8 37.5 14.5 36.5 12.5 C35.5 10.5 32.5 10 29 11.2 L15 16.2 L9 12.5 L6.5 13.5 L9.5 18.5 L6 21 Z" fill="currentColor" /></svg>
        Departure Flight
      </div>
      <div class="sample-badge badge-arr">
        <svg width="18" height="18" viewBox="0 0 48 48" fill="none"><line x1="4" y1="40" x2="44" y2="40" stroke="currentColor" stroke-width="3" stroke-linecap="round" /><path d="M6 21 L12 23 L18 17 L20.5 18 L18 25 L32 30 C35.5 31.2 37.5 33.5 36.5 35.5 C35.5 37.5 32.5 38 29 36.8 L15 31.8 L9 35.5 L6.5 34.5 L9.5 29.5 L6 27 Z" fill="currentColor" /></svg>
        Arrival Flight
      </div>
    </div>
  </div>
</div>

</body>
</html>
'''

with open('tools/test_svgs.html', 'w', encoding='utf-8') as f:
    f.write(svg_tests_html)
print("Created tools/test_svgs.html")
