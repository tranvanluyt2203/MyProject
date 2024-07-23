import React, { useState } from "react";
import { Alert, Image, Keyboard, StyleSheet, Text, TextInput, TouchableOpacity, View } from "react-native";
import ButtonCommon from "./ButtonCommon";
import { colors, fontSizes, stylesCommon } from "../constants";

const RegisterScreen = (props) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [rePassword, setRePassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [showRePassword, setShowRePassword] = useState(false)
    const [error, setError] = useState('');


    const checkReEnterPassword = (password, rePassword) => {
        if (password != rePassword) setError("Password don't match")
        else setError("")
    }

    return (<View style={styles.register}>
        <Text style={styles.header}>Register</Text>
        <TextInput
            style={stylesCommon.input}
            placeholder="Enter your email"
            value={email}
            onChangeText={(text) => {
                setEmail(text);
            }}
        />
        <View style={stylesCommon.viewPassword}>
            <TextInput
                style={stylesCommon.input}
                placeholder="Enter your password"
                value={password}
                secureTextEntry={!showPassword}
                onChangeText={(value) => {
                    setPassword(value)
                    checkReEnterPassword(rePassword, value)
                }}
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
        <View style={stylesCommon.viewPassword}>
            <TextInput
                style={stylesCommon.input}
                placeholder="Re Enter your password"
                value={rePassword}
                secureTextEntry={!showRePassword}
                onChangeText={(value) => {
                    setRePassword(value)
                    checkReEnterPassword(password, value)
                }}
            />
            <TouchableOpacity
                style={stylesCommon.viewEye}
                onPress={() => setShowRePassword(!showRePassword)}
            >
                <Image
                    source={showRePassword ? require("../images/eye/ic_eyeHide.png") : require("../images/eye/ic_eyeOpen.png")}
                    style={stylesCommon.eye}
                />
            </TouchableOpacity>
        </View>
        {error && <Text style={styles.error}>{error}</Text>}
        <ButtonCommon
            tittle={"Register"}
            onpress={() => {
                Alert.alert("Login", `Email: ${email}\nPassword: ${password}\nRePassword: ${rePassword}`);
                Keyboard.dismiss();
            }}
            disabled={error == '' ? false : true}
            styleButton={[
                stylesCommon.styleBt,
                !error && { marginTop: 20 }
            ]}
        />
    </View>
    );
}
const styles = StyleSheet.create({
    header: {
        fontSize: fontSizes.h1,
        color: colors.colorHeader,
        fontWeight: '500',
        textAlign: 'center',
        marginVertical: 20,
    },
    register: {
        flexDirection: 'column',
        justifyContent: 'center',
        borderRadius: 20,
    },
    error: {
        color: colors.errorColor,
        textAlign: 'center',
        marginVertical: 5,
    },
})
export default RegisterScreen