// firebase_init.js
// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCpY9ZhcJaRcHOWhPWKBEigb7Tw2_qOYEM",
  authDomain: "sun-leisure-world-portal.firebaseapp.com",
  projectId: "sun-leisure-world-portal",
  storageBucket: "sun-leisure-world-portal.firebasestorage.app",
  messagingSenderId: "630137017192",
  appId: "1:630137017192:web:f0dc5a77e74099ec6f7cdd"
};

// Initialize Firebase
if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}
const db = firebase.firestore();

// Global Admin Logger using Firestore
window.slwLogActivity = function(action) {
  try {
    const user = sessionStorage.getItem('slw_user_v3') || localStorage.getItem('slw_user_v3');
    if (!user) return; // Not logged in
    
    db.collection('slw_activity_logs').add({
      user: user,
      action: action,
      time: firebase.firestore.FieldValue.serverTimestamp()
    }).catch(e => console.error("Firestore Log Error:", e));
    
    // Also update last active
    if (action !== 'Logged Out') {
        window.slwSetUserOnline(user);
    }
    
  } catch (e) { console.error("Log err", e); }
};

// Global function to set user online status
window.slwSetUserOnline = function(user) {
  try {
    db.collection('slw_user_status').doc(user).set({
      lastActive: firebase.firestore.FieldValue.serverTimestamp(),
      explicitlyOffline: false
    }, { merge: true }).catch(e => console.error("Firestore Status Error:", e));
  } catch(e) {}
};

// Global function to set user offline status
window.slwSetUserOffline = function(user) {
  try {
    db.collection('slw_user_status').doc(user).set({
      explicitlyOffline: true
    }, { merge: true }).catch(e => console.error("Firestore Status Error:", e));
  } catch(e) {}
};

// Automatic heartbeat to keep user online while any tool is open
setInterval(() => {
  try {
    const user = sessionStorage.getItem('slw_user_v3') || localStorage.getItem('slw_user_v3');
    if (user && window.slwSetUserOnline) {
      window.slwSetUserOnline(user);
    }
  } catch(e) {}
}, 60000); // Every 60 seconds
