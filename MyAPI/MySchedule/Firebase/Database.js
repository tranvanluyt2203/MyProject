// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyD1xLaVB0p3ZILA7Y1j_CIxqI2dPbMwqZA",
  authDomain: "myschedule-97187.firebaseapp.com",
  databaseURL: "https://myschedule-97187-default-rtdb.firebaseio.com",
  projectId: "myschedule-97187",
  storageBucket: "myschedule-97187.appspot.com",
  messagingSenderId: "729185053715",
  appId: "1:729185053715:web:228353c33ea70e3900a3e6",
  measurementId: "G-GSVNVCP63N"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);