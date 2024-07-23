import React from 'react';
import {
  Text,
} from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { GestureHandlerRootView } from 'react-native-gesture-handler';
import Root from './Root';


const App = (props) => {
  return (
    // <Provider store={store}>
    // <LanguageProvider>
    <SafeAreaProvider>
      {/* <LoadderProvider> */}
      <GestureHandlerRootView style={{ flex: 1 }}>
        <Root />
      </GestureHandlerRootView>
      {/* </LoadderProvider> */}
    </SafeAreaProvider>
    // </LanguageProvider>
    // </Provider>
  );
}



export default App;
