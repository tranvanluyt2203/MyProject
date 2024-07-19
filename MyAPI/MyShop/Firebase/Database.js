// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCqTYT9d87vdO4Qi5xC6_QbB9gI7Bbzfp8",
  authDomain: "myshop-54fbc.firebaseapp.com",
  databaseURL: "https://myshop-54fbc-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "myshop-54fbc",
  storageBucket: "myshop-54fbc.appspot.com",
  messagingSenderId: "642274958778",
  appId: "1:642274958778:web:868f8b8656b41598c8d183",
  measurementId: "G-RXXGCHZRBK"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);