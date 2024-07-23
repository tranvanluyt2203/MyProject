import React, { useEffect, useRef } from "react";
import {
    View,
    StyleSheet,
    StatusBar,
} from 'react-native';
import * as Animatable from 'react-native-animatable';

const Splash = (props) => {
    const { navigation } = props;
    const logoRef = useRef(null);

    useEffect(() => {
        logoRef.current.bounceInRight(2000);

        // Sau khi animation xuất hiện kết thúc, bắt đầu animation biến mất
        const fadeOutTimer = setTimeout(() => {
            logoRef.current.flipOutY(2000);
        }, 2000); // Đợi 2 giây (thời gian của animation xuất hiện) trước khi bắt đầu biến mất

        // Chuyển đến màn hình Welcome sau 4 giây (2 giây xuất hiện + 2 giây biến mất)
        const navigateTimer = setTimeout(() => {
            navigation.replace('Welcome');
        }, 4000);

        // Dọn dẹp timer khi component bị unmount
        return () => {
            clearTimeout(fadeOutTimer);
            clearTimeout(navigateTimer);
        };
    }, [navigation]);

    return (
        <View style={styles.container}>
            <StatusBar barStyle="light-content" backgroundColor="#0000FF" />
            <Animatable.Image
                ref={logoRef}
                source={require('../images/logo/logo.png')}
                style={styles.logo}
                animation="bounceInRight"
                duration={2000}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#0000FF', // Màu nền xanh
    },
    logo: {
        width: 150,
        height: 150,
        resizeMode: 'contain',
    },
});

export default Splash;
