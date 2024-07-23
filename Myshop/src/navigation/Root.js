import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import {
    Welcome,
    LoginRegister,
    Profile,
    Splash,
    ForgotPassword
} from '../screens';

const Stack = createNativeStackNavigator();

const Root = (props) => {
    return (
        <NavigationContainer>
            <Stack.Navigator
                initialRouteName="Splash"
                screenOptions={{ headerShown: false }}
            >
                <Stack.Screen
                name = "Splash"
                component={Splash}/>
                <Stack.Screen
                    name="Welcome"
                    component={Welcome}
                />
                <Stack.Screen
                    name="Profile"
                    component={Profile}
                />
                <Stack.Screen
                    name="LoginRegister"
                    component={LoginRegister}
                />
                <Stack.Screen
                name="ForgotPassword"
                component={ForgotPassword}
                />
            </Stack.Navigator>
        </NavigationContainer>
    );
};

export default Root;
