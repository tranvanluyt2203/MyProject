import React, { useState } from "react";
import {
    SafeAreaView,
    StyleSheet,
    Text,
    View
} from "react-native";
import { TabView, SceneMap, TabBar } from 'react-native-tab-view';
import { colors, fontSizes } from "../../../constants";
import { screenHeight, screenWidth } from "../../../utilies/Device";
import { LoginScreen, RegisterScreen, ButtonCommon } from "../../../components";

const LoginRegister = (props) => {
    const { navigation } = props;

    const [index, setIndex] = useState(0);


    const Login = () => <LoginScreen />

    const Register = () => <RegisterScreen />

    const [routes] = useState([
        { key: 'login', title: 'Login' },
        { key: 'register', title: 'Register' },
    ]);

    const renderScene = SceneMap({
        login: Login,
        register: Register,
    });

    const renderTabBar = (props) => (
        <SafeAreaView style={styles.tab}>
            <TabBar
                {...props}
                indicatorStyle={styles.indicator}
                style={styles.tabBar}
                renderLabel={({ route, focused }) => (
                    <Text style={[styles.label, focused ? styles.labelFocused : styles.labelUnfocused]}>
                        {route.title}
                    </Text>
                )}
                pressColor={colors.noColor}
            />
        </SafeAreaView>
    );

    return (
        <SafeAreaView style={styles.container}>
            <View style={styles.emptyView}></View>
            <TabView
                navigationState={{ index, routes }}
                renderScene={renderScene}
                onIndexChange={setIndex}
                renderTabBar={renderTabBar}
            />
        </SafeAreaView>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        marginHorizontal: 20,
    },
    tab: {
        marginTop: screenHeight / 4.5-20,
    },
    emptyView: {
        height: screenHeight / 2,
        width: screenWidth - 40,
        backgroundColor: colors.backgroundForm,
        position: 'absolute',
        marginTop: screenHeight / 4.5 - 20,
        borderRadius: 20,
    },
    tabBar: {
        height: 50,
        borderTopRightRadius:20,
        borderTopLeftRadius:20,
    },
    indicator: {
        display: 'none',
    },
    label: {
        fontSize: fontSizes.h3,
        color: colors.white,
        fontWeight: '600',
        textAlign: 'center',
        paddingHorizontal: 10,
        paddingVertical: 5,
    },
    labelFocused: {
        color: colors.white,
    },
    labelUnfocused: {
        color: colors.colorUnforcus,
    },
});

export default LoginRegister;
