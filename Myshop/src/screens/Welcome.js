import React, { } from "react";
import {
    SafeAreaView,
    StyleSheet,
    View
} from "react-native";
import { ButtonCommon } from "../components";
import { screenWidth } from "../utilies/Device";

const Welcome = (props) => {
    const { navigation } = props
    return (
        <SafeAreaView
            style={styles.container}
        >
            <View
                style={[
                    styles.viewImage,
                    {
                        width: screenWidth - 50,
                    }
                ]}
            >
            </View>
            <View style={styles.viewButton}>
                <ButtonCommon
                    onpress={
                        () => navigation.navigate('LoginRegister')
                    }
                    tittle={"Next"}
                    hasIcon={true}
                />
            </View>

        </SafeAreaView>

    )
}
const styles = StyleSheet.create({
    container: {
        flex: 1,
        margin: 10,
        flexDirection: "column",
        justifyContent: "space-around",
        alignItems: "center"
    },
    viewImage: {
        flex: 0.4,
        marginTop: 40,
        flexDirection: 'column',
        alignItems: 'center',
        backgroundColor: 'green'
    },

    viewButton: {
        flex: 0.4,
        flexDirection: "column",
        justifyContent: "flex-end",
        alignItems: "center",
        marginBottom: 30,
    },
})



export default Welcome