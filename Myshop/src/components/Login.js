import React, { useState } from "react";
import { Text, TextInput, TouchableOpacity, View, StyleSheet, Alert, Keyboard, Image } from "react-native";
import ButtonCommon from "./ButtonCommon";
import { colors, fontSizes, stylesCommon } from "../constants";

const LoginScreen = (props) => {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [showPassword, setShowPassword] = useState(false)
    const [error, setError] = useState('');


    return (<View style={styles.login}>
        <Text style={styles.header}>Login</Text>
        <TextInput
            style={stylesCommon.input}
            placeholder="Enter your email"
            value={email}
            onChangeText={setEmail}
        />
        <View style={stylesCommon.viewPassword}>
            <TextInput
                style={stylesCommon.input}
                placeholder="Enter your password"
                value={password}
                secureTextEntry={!showPassword}
                onChangeText={setPassword}
            />
            <TouchableOpacity
                style={stylesCommon.viewEye}
                onPress={() => setShowPassword(!showPassword)}
            >
                <Image
                    source={showPassword ? require("../images/eye/ic_eyeHide.png") : require("../images/eye/ic_eyeOpen.png")}
                    style={stylesCommon.eye}
                />
            </TouchableOpacity>
        </View>

        {error && <Text style={styles.error}>{error}</Text>}
        <TouchableOpacity
            style={stylesCommon.btForgot}
            onPress={() => navigation.navigate("ForgotPassword")}
        >
            <Text style={stylesCommon.forgot}>Forgot Password?</Text>
        </TouchableOpacity>
        <ButtonCommon
            tittle={"Login"}
            onpress={() => {
                Alert.alert("Login", `Email: ${email}\nPassword: ${password}`);
                Keyboard.dismiss();
            }}
            styleButton={stylesCommon.styleBt}
            disabled={error == '' ? false : true}
        />
    </View>
    );
}
const styles = StyleSheet.create({
    login: {
        flexDirection: 'column',
        justifyContent: 'center',
        borderRadius: 20,
    },
    header: {
        fontSize: fontSizes.h1,
        color: colors.colorHeader,
        fontWeight: '500',
        textAlign: 'center',
        marginVertical: 20,
    },
    error: {
        color: colors.errorColor,
        textAlign: 'center',
        marginVertical: 5,
    },

})
export default LoginScreen