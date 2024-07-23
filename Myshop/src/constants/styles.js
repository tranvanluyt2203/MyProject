import React from "react";
import { StyleSheet } from "react-native";
import colors from "./colors";
import fontSizes from "./fontSizes";
const stylesCommon = StyleSheet.create({
    viewPassword: {
        justifyContent:'center',
    },
    input: {
        borderWidth: 1,
        borderColor: colors.colorBorderTextInput,
        borderRadius: 10,
        height: 50,
        paddingVertical:5,
        paddingHorizontal:20,
        marginHorizontal: 20,
        marginVertical:5,
    },
    viewEye: {
        position: 'absolute',
        end:30,
    },
    eye: {
        width: 24,
        height: 24,
    },
    btForgot: {
        alignSelf: 'flex-end',
        marginEnd: 20,
        marginVertical:10
    },
    forgot: {
        color: colors.colorForpassword,
        fontSize: fontSizes.h4,
    },
    styleBt: {
        alignSelf: 'center',
        marginBottom:10 ,
        paddingVertical: 5,
        borderRadius: 10,
    },
})
export default stylesCommon