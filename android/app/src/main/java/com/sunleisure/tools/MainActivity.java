package com.sunleisure.tools;

import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Get the WebView from the Capacitor bridge
        WebView webView = this.bridge.getWebView();
        WebSettings settings = webView.getSettings();

        // Force desktop-style layout: use a wide viewport (like a desktop browser)
        settings.setUseWideViewPort(true);

        // Load the page scaled to fit the screen width initially (zoom out to show full page)
        settings.setLoadWithOverviewMode(true);

        // Allow user to pinch-to-zoom
        settings.setSupportZoom(true);
        settings.setBuiltInZoomControls(true);

        // Hide the on-screen zoom buttons (we use pinch gesture only)
        settings.setDisplayZoomControls(false);
    }
}

