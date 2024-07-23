import React from "react";
import {
    Image,
    StyleSheet,
    Text,
    TouchableOpacity,

} from "react-native";
import { colors, fontSizes } from "../constants";
const ButtonCommon = ({ tittle, onpress, hasIcon, styleButton, disabled }) => {
    return (
        <TouchableOpacity
            style={[
                styles.button,
                styleButton,
                hasIcon && {
                    flexDirection: "row",
                    justifyContent: 'center',
                    alignContent: 'center'
                },
                disabled && {
                    borderColor: colors.noColor,
                    backgroundColor: colors.disabledColor
                }
            ]}
            disabled={disabled}
            onPress={onpress}
        >
            <Text
                style={[
                    styles.tittle,
                    hasIcon && {
                        marginEnd: 20,
                        marginStart: 70,
                    },
                    disabled && {
                        color: colors.disableTextColor
                    }
                ]}>{tittle}</Text>
            {hasIcon && <Image
                style={styles.icon}
                source={require("../images/ic_next.png")}
                resizeMode="cover"
            ></Image>}
        </TouchableOpacity>
    )
}
const styles = StyleSheet.create({
    button: {
        borderWidth: 5,
        borderRadius: 15,
        borderColor: colors.colorBorderButton,

        width: 250,
        marginVertical: 5,
        backgroundColor: colors.colorButton,
        paddingVertical: 10,

    },
    tittle: {
        fontSize: fontSizes.h2,
        textAlign: 'center',
        fontWeight: '900',
        color: colors.white,
    },
    icon: {
        height: 30,
        width: 30,
        tintColor: colors.white,
        alignSelf: 'center',
        borderWidth: 10,
        marginStart: 40,

    }
})
export default ButtonCommon